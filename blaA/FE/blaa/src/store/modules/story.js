import axios from "@/api/axios.js";
import api from "@/api/api";
import { dataChange } from "@/hooks/dateChange";

export default {
  namespaced: true,
  state: {
    Token: sessionStorage.getItem("token"),
    stories: [],
    images: [],
    comments: [],
    currentStory: [],
    // 현재 상태를 저장하는 변수
    isState: '',
    totalCount: 0,
  },
  mutations: {
    GET_IMAGES(state, payload) {
      const {
        howNow
      } = dataChange()

      state.totalCount = payload.count[0]['count']
      if (state.isState == payload.isState.value && payload.page != 1) {
        for (let i=0; i < payload.data.length; i++) {
          payload.data[i].created_at = howNow(payload.data[i].created_at)
          state.images.push(payload.data[i])
        }
        console.log(state.images)
      } else {
        state.isState = payload.isState.value
        state.images = []
        for (let i=0; i < payload.data.length; i++) {
          payload.data[i].created_at = howNow(payload.data[i].created_at)
          state.images.push(payload.data[i])
        }
      }
    },
    GET_CURRENT_STORY(state, payload) {
      const { howNow } = dataChange();
      // 날짜 변환
      payload.created_at = howNow(payload.created_at);
      state.currentStory = payload;
    },
    DELETE_CURRENT_STORY(state) {
      state.currentStory = null;
    },
    LIKE_CURRNET_STORY(state, payload) {
      state.currentStory.like_user = payload.like_user;
      state.currentStory.like_user_count = payload.like_user_count;
    },
    CREATE_COMMENT(state, payload) {
      const { howNow } = dataChange();
      // 날짜 변환
      payload.created_at = howNow(payload.created_at);
      // 작성자, 내용, 날짜가 객체로 들어감
      state.comments.push(payload);
    },
    GET_COMMENT(state, payload) {
      const { howNow } = dataChange();
      // 날짜 변환
      if (payload) {
        payload.forEach((ele) => {
          ele.created_at = howNow(ele.created_at);
        });
      } 

      state.comments = payload;
    },
    FIX_COMMENT(state, payload) {
      const idx = state.comments.findIndex(
        (ele) => ele.comment_pk == payload.comment_pk
      );
      state.comments[idx].story_comment = payload.story_comment;
    },
    DELETE_COMMENT(state, payload) {
      const idx = state.comments.findIndex((ele) => ele.comment_pk == payload);
      state.comments.splice(idx, 1);
    },
  },
  actions: {
    // Story 목록 조회
    async getImages({ commit, state }, data) {
      try {
        const res = await axios.get(api.story.story(), {
          params: {
            page: data.page
          }
        });
        const send = {
          count: res.data.splice(-1,1),
          data: res.data,
          isState: data.isState,
          page: data.page
        }
        commit("GET_IMAGES", send);
      } catch (error) {
        // 에러 발생시
        console.log(error);
      }
    },
    // 관심업종 검색
    async getCategory({ commit, state }, data) {
      try {
        const res = await axios.get(api.story.story() + "category/", {
          params: {
            page: data.page
          }
        });
        const send = {
          count: res.data.splice(-1,1),
          data: res.data,
          isState: data.isState,
          page: data.page
        }
        console.log('업종', res.data)
        commit("GET_IMAGES", send);
      } catch (error) {
        // 에러 발생시
        console.log(error);
      }
    },
    async getRegion({ commit, state }, data) {
      try {
        const res = await axios.get(api.story.story() + "region/", {
          params: {
            page: data.page
          }
        });
        const send = {
          count: res.data.splice(-1,1),
          data: res.data,
          isState: data.isState,
          page: data.page
        }
        console.log('지역', res.data)
        commit("GET_IMAGES", send);
      } catch (error) {
        // 에러 발생시
        console.log(error);
      }
    },
    async getFollow({ commit, state }, data) {
      try {
        const res = await axios.get(api.story.story() + "follow/", {
          params: {
            page: data.page
          }
        });
        console.log('팔로우', res.data)
        const send = {
          count: res.data.splice(-1,1),
          data: res.data,
          isState: data.isState,
          page: data.page
        }

        commit("GET_IMAGES", send);
      } catch (error) {
        // 에러 발생시
        console.log(error);
      }
    },
    async getHashtag({ commit, state }, page) {
      try {
        const res = await axios.get(api.story.hashtag(), {
          params: {
            page: page.page,
            id: page.hashtag_content,
          }
        })
        const res2 = await axios.get(api.story.hashtag(), {
          params: {
            page: page.page,
            id: page.hashtag_content,
          }
        })

        let result = []

        if (res.data[-1] == Number) {
          result = res.data
        } else {
          result = res2.data
        }
        const count = result.splice(-1,1)
        
        const array = []
        result.forEach(ele => {
          array.push(ele['story_pk'])
        })

        const send = {
          count: count,
          data: array,
          isState: page.isState,
          page: page.page
        }

        commit('GET_IMAGES', send)
      } catch(error) {
        console.log(error)
      }
    },
    async getCurrentStory({ commit, state }, story_pk) {
      try {
        const res = await axios.get(api.story.detail(story_pk));
        // 댓글 가져옴
        commit("GET_CURRENT_STORY", res.data)
      } catch (error) {
        console.log(error);
      }
    },
    async deleteCurrentStory({ commit, state }, story_pk) {
      try {
        await axios.delete(api.story.detail(story_pk));
        commit("DELETE_CURRENT_STORY");
      } catch (error) {
        console.error(error);
      }
    },
    async likeStory({ commit, state }, story_pk) {
      try {
        const res = await axios.post(
          api.story.like(story_pk),
          {}
        );
        commit("LIKE_CURRNET_STORY", res.data);
      } catch (error) {
        console.error(error);
      }
    },
    // 댓글을 가져오는 함수
    async getComment({ commit, state }, story_pk) {
      try {
        const res2 = await axios.get(api.story.comment(story_pk))
        const res = await axios.get(api.story.comment(story_pk))
        let data = []
        if (res.data.length) {
          if(res2.data[0].created_at) {
            data = res2.data
          } else {
            data = res.data
          }
        }
        
        commit("GET_COMMENT", data);
      } catch (error) {
        console.log(error);
      }
    },
    // 댓글 생성 함수
    async createComment({ commit, state }, content) {
      try {
        // comment 생성 응답이 없어 임의로 작성
        // story.id를 추가적으로 입력해야됨
        const res = await axios.post(
          api.story.comment(content.story_pk),
          {
            story_comment: content.story_comment,
          }
        );
        // 작성자, 내용, 날짜, 작성자 프로필을 요청하여 추가적으로 입력
        commit("CREATE_COMMENT", res.data);
      } catch (error) {
        console.log(error);
      }
    },
    async fixComment({ commit, state }, data) {
      const story_comment = data.story_comment;
      try {
        const res = await axios.put(
          api.story.commentChange(data.comment_pk),
          {
            story_comment: story_comment,
          }
        );
        commit("FIX_COMMENT", res.data);
      } catch (error) {
        console.error(error);
      }
    },
    async deleteComment({ commit, state }, comment_pk) {
      try {
        await axios.delete(api.story.commentChange(comment_pk));
        console.log('삭제')
        commit("DELETE_COMMENT", comment_pk);
      } catch (error) {
        console.error(error);
      }
    },
  },
  getters: {},
};
