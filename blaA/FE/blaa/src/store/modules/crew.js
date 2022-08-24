import axios from "@/api/axios.js";
import api from "@/api/api";
import router from "@/router/index";
import { dataChange } from "@/hooks/dateChange";

export default {
  namespaced: true,
  state: {
    Token: sessionStorage.getItem("token"),
    AllCrews: [],
    myCrews: [],
    articles: [],
    article: [],
    crewInfo: [],
    members: [],
    requestlist: [],
    comments: [],
  },
  mutations: {
    GET_ALL_CREWS(state, payload) {
      state.AllCrews = payload;
    },
    GET_MY_CREW(state, payload) {
      state.myCrews = payload;
    },
    IS_BUSINESS(state, payload) {
      state.crewInfo.is_business = payload;
    },
    SET_CREW_INFO(state, payload) {
      state.crewInfo = payload;
    },
    GET_CREW_ARTICLES(state, payload) {
      state.articles = payload;
    },
    GET_ARTICLE_DETAIL(state, payload) {
      state.article = payload;
    },
    GET_CREW_MEMBERS(state, payload) {
      state.members = payload;
    },
    GET_REQUEST_LIST(state, payload) {
      state.requestlist = payload;
    },
    GET_COMMENTS(state, payload) {
      state.comments = payload;
    },
    SET_COMMENTS(state, payload) {
      const { yyyyMMdd } = dataChange();
      // 날짜 변환
      payload.created_at = yyyyMMdd(payload.created_at);
      // 작성자, 내용, 날짜가 객체로 들어감
      state.comments.push(payload);
    },
    DELETE_COMMENT(state, payload) {
      const idx = state.comments.findIndex((ele) => ele.crew_comment_pk == payload);
      state.comments.splice(idx, 1);
    },
  },
  actions: {
    ///////////////////////////Crew Article/////////////////////////////////
    async getCrewArticle({ commit, state }, crew_pk) {
      try {
        const instance = await axios.get(api.crew.articles(crew_pk));
        commit("GET_CREW_ARTICLES", instance.data.results);
      } catch (error) {
        console.log(error);
      }
    },
    async getArticleDetail({ commit, state }, crew_article_pk) {
      try {
        const instance = await axios.get(api.crew.article(crew_article_pk));
        commit("GET_ARTICLE_DETAIL", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async registArticle({ state }, payload) {
      console.log("전송되는 데이터: ", payload.article);
      // console.log(payload.crew_pk);
      // // console.log(payload.article);
      // for (var value of payload.article.values()) {
      //   console.log("밸류: ", value);
      // }
      try {
        const instance = await axios.post(api.crew.articles(payload.crew_pk), payload.article);
        if (instance.status == 200 || instance.status == 201) {
          alert("새 글이 등록되었습니다.");
          router.push({ name: "articledetail", params: { crew_article_pk: instance.data.crew_article_pk } });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async modifyArticle({ state }, payload) {
      try {
        const instance = await axios.put(api.crew.article(payload.crew_article_pk), payload.article);
        if (instance.status == 200 || instance.status == 201) {
          alert("수정이 완료되었습니다.");
          router.push({ name: "articledetail", params: { crew_article_pk: instance.data.crew_article_pk } });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async deleteArticle({ state }, payload) {
      console.log(payload);
      console.log(payload.crew_article_pk, "번째 글 삭제");
      console.log(state.Token);
      try {
        const instance = await axios.delete(api.crew.article(payload.crew_article_pk));
        console.log(instance);
        if (instance.status == 200 || instance.status == 201 || instance.status == 204) {
          alert("삭제가 완료되었습니다.");
          router.push({ name: "crewboard", params: { crew_pk: payload.crew_pk } });
        }
      } catch (error) {
        console.log(error);
      }
    },
    ///////////////////////////Crew Info/////////////////////////////////
    async getCrewInfo({ commit, state }, crew_pk) {
      try {
        const instance = await axios.get(api.crew.crewInfo(crew_pk));
        commit("SET_CREW_INFO", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async registcrew({ commit }, crewData) {
      try {
        const instance = await axios.post(api.crew.crew(), crewData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        console.log(instance);
        if (instance.status == 201 || instance.status == 200) {
          alert("크루 생성이 완료되었습니다.");
          router.push({ name: "crewboardmember", params: { crew_pk: instance.data.crew_pk } });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async modifyCrew({ state }, payload) {
      console.log("payload", payload);
      console.log(payload.crew_pk);
      console.log(payload.crew);
      try {
        const instance = await axios.patch(api.crew.crewInfo(payload.crew_pk), payload.crew, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        if (instance.status == 200 || instance.status == 201) {
          alert("수정이 완료되었습니다.");
          router.push({ name: "crewdetail", params: { crew_pk: payload.crew_pk } });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async deleteCrew({ state }, crew_pk) {
      console.log(crew_pk);
      try {
        await axios.delete(api.crew.crewInfo(crew_pk));
        alert("삭제가 완료되었습니다.");
      } catch (error) {
        console.log(error);
      }
    },
    async allcrewlist({ commit, state }) {
      try {
        const instance = await axios.get(api.crew.crew());
        commit("GET_ALL_CREWS", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async getCrewMembers({ commit, state }, crew_pk) {
      try {
        const instance = await axios.get(api.crew.members(crew_pk));
        console.log(instance.data.results);
        commit("GET_CREW_MEMBERS", instance.data.results);
      } catch (error) {
        console.log(error);
      }
    },
    ///////////////////////////Crew Join/////////////////////////////////
    async crewJoin({ state }, crew_pk) {
      try {
        const instance = await axios.post(api.crew.sign(crew_pk), {});
        if (instance.status == 201 || instance.status == 200) {
          alert("가입 신청이 완료되었습니다.");
        }
      } catch (error) {
        console.log(error.response.data.message);
        console.log(error.response.status);
        if (error.response.status == 409) {
          alert("이미 가입된 크루입니다.");
        } else if (error.response.status == 400) {
          alert("가입 승인 처리중입니다.");
        }
      }
    },
    async getRequestList({ commit, state }, payload) {
      try {
        const instance = await axios.get(api.crew.invitelist(payload.crew_pk, payload.type));
        commit("GET_REQUEST_LIST", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async acceptRequest({ state }, payload) {
      console.log(payload);
      try {
        const instance = await axios.post(api.crew.accept(payload.crew_pk, payload.user_pk));
        console.log(instance);
        if (instance.status == 200) {
          alert("가입 처리가 완료되었습니다.");
        }
      } catch (error) {
        console.log(error);
      }
    },
    async denyRequest({ state }, payload) {
      console.log(payload);
      try {
        const instance = await axios.post(api.crew.deny(payload.crew_pk, payload.user_pk));
        console.log(instance);
        if (instance.status == 200) {
          alert("가입 신청이 거절되었습니다.");
          router.go({
            name: "crewmemberrequestlist",
            query: { crew_pk: payload.crew_pk },
          });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async leaveCrew({ state }, crew_pk) {
      console.log(crew_pk);
      try {
        const instance = await axios.post(api.crew.leave(crew_pk));
        console.log(instance.status);
      } catch (error) {
        console.log(error);
      }
    },
    /////////////////////Crew Article Comment/////////////////////
    async createComment({ commit }, payload) {
      console.log(payload);
      console.log(payload.comment_content);
      try {
        const instance = await axios.post(api.crew.comment(payload.crew_article_pk), {
          comment_content: payload.comment_content,
        });
        commit("SET_COMMENTS", instance.data);
        console.log(instance);
      } catch (error) {
        console.log(error);
      }
    },
    async getComment({ commit }, crew_article_pk) {
      try {
        const instance = await axios.get(api.crew.comment(crew_article_pk));
        console.log(instance.data);
        commit("GET_COMMENTS", instance.data.results);
      } catch (error) {
        console.log(error);
      }
    },
    async deleComment({ commit }, crew_comment_pk) {
      try {
        const instance = await axios.get(api.crew.commentUpdate(crew_comment_pk));
        console.log(instance.data);
        console.log(instance.status);
        commit("DELETE_COMMENT", crew_comment_pk);
        if (instance.status == 200) {
          alert("삭제가 완료되었습니다.");
        }
      } catch (error) {
        console.log(error);
      }
    },
    async getMyCrews(context, user_pk) {
      await axios
        .get(api.profile.myCrew(user_pk), {})
        .then((response) => {
          console.log("crew response", response);
          context.commit("GET_MY_CREW", response.data.results);
        })
        .catch((err) => {
          console.log("crew error : ", err);
        });
    },
  },
  getters: {},
};
