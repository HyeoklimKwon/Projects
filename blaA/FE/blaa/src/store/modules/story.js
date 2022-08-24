import axios from 'axios'
import api from '@/api/api'
import {dataChange} from '@/hooks/dateChange'

export default {
  namespaced: true,
  state: {
    Token: sessionStorage.getItem('token'),
    stories: [],
    images: [],
    comments: [],
    currentStory: [],
  },
  mutations: {
    GET_IMAGES(state, payload) {
      state.images = payload
    },
    GET_CURRENT_STORY(state, payload) {
      const {
        yyyyMMdd
      } = dataChange()
      // 날짜 변환
      payload.created_at = yyyyMMdd(payload.created_at)
      state.currentStory = payload
    },
    DELETE_CURRENT_STORY(state) {
      state.currentStory = null
    },
    LIKE_CURRNET_STORY(state, payload) {
      state.currentStory.like_user = payload.like_user
      state.currentStory.like_user_count = payload.like_user_count
    },
    CREATE_COMMENT(state, payload) {
      const {
        yyyyMMdd
      } = dataChange()

      // 날짜 변환
      payload.created_at = yyyyMMdd(payload.created_at)
      // 작성자, 내용, 날짜가 객체로 들어감
      state.comments.push(payload)
    },
    GET_COMMENT(state, payload) {
      const {
        yyyyMMdd
      } = dataChange()

      // 날짜 변환
      payload.forEach(ele => {
        ele.created_at = yyyyMMdd(ele.created_at)
      })

      state.comments = payload
    },
    FIX_COMMENT(state, payload) {
      const idx = state.comments.findIndex(ele => {
        ele.comment_pk == payload.comment_pk
      })
      state.comments[idx] = payload.story_comment
    },
    DELETE_COMMENT(state, payload) {
      const idx = state.comments.findIndex(ele => ele.comment_pk == payload)
      state.comments.splice(idx, 1)
    }
  },
  actions: {
    // Story 목록 조회
    async getImages({commit, state}) {
      try {
        const res = await axios.get(api.story.story(), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_IMAGES',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },
    // 관심업종 검색
    async getCategory({commit, state}) {
      try {
        const res = await axios.get(api.story.story() + 'category/', {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_IMAGES',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },
    async getRegion({commit, state}) {
      try {
        const res = await axios.get(api.story.story() + 'region/', {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_IMAGES',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },
    async getFollow({commit, state}) {
      try {
        const res = await axios.get(api.story.story() + 'follow/', {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        console.log(res.data)
        commit('GET_IMAGES',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },
    async getCurrentStory({commit, state}, story_pk) {
      try {
        const res = await axios.get(api.story.detail(story_pk), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_CURRENT_STORY', res.data)
      } catch(error) {
        console.log(error)
      }
    },
    async deleteCurrentStory({commit, state}, story_pk) {
      try {
        await axios.delete(api.story.detail(story_pk), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('DELETE_CURRENT_STORY')
      } catch (error) {
        console.error(error)
      }
    },
    async likeStory({commit, state}, story_pk) {
      try {
        const res = await axios.post(api.story.like(story_pk), {},  {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('LIKE_CURRNET_STORY', res.data)
      } catch (error) {
        console.error(error)
      }
    },
    // 댓글을 가져오는 함수
    async getComment({commit, state}, story_pk) {
      try {
        const res = await axios.get(api.story.comment(story_pk), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_COMMENT', res.data)
      } catch(error) {
        console.log(error)
      }
    },
    // 댓글 생성 함수
    async createComment({commit, state}, content){
      try {
        // comment 생성 응답이 없어 임의로 작성
        // story.id를 추가적으로 입력해야됨
        const res = await axios.post(api.story.comment(content.story_pk), {
          story_comment: content.story_comment
          },
          {
            headers: {
              Authorization: `Bearer ${state.Token}`
            }
          })
        // 작성자, 내용, 날짜, 작성자 프로필을 요청하여 추가적으로 입력
        commit('CREATE_COMMENT', res.data)
      } catch (error) {
        console.log(error)
      }
    },
    async fixComment({commit, state}, data){
      const story_comment = data.story_comment
      try {
        const res = await axios.put(api.story.commentChange(data.comment_pk),{
          story_comment: story_comment
        }, {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('FIX_COMMENT', res.data)
      } catch (error) {
        console.error(error)
      }
    },
    async deleteComment({commit, state}, comment_pk){
      try {
        await axios.delete(api.story.commentChange(comment_pk), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('DELETE_COMMENT', comment_pk)
      } catch (error) {
        console.error(error)
      }
    }
  },
  getters: {
  },
};
