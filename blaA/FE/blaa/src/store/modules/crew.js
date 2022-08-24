import axios from "@/api/axios.js";
import api from "@/api/api";
import router from "@/router/index";

export default {
  namespaced: true,
  state: {
    Token: sessionStorage.getItem("token"),
    AllCrews: [],
    articles: [],
    article: [],
    crewInfo: [],
    members: [],
    requestlist: [],
  },
  mutations: {
    GET_ALL_CREWS(state, payload) {
      state.AllCrews = payload;
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
  },
  actions: {
    ///////////////////////////Crew Article/////////////////////////////////
    async getCrewArticle({ commit, state }, crew_pk) {
      try {
        const instance = await axios.get(api.crew.articles(crew_pk));
        commit("GET_CREW_ARTICLES", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async getArtileDetail({ commit, state }, crew_article_pk) {
      try {
        const instance = await axios.get(api.crew.article(crew_article_pk));
        commit("GET_ARTICLE_DETAIL", instance.data);
      } catch (error) {
        console.log(error);
      }
    },
    async registArticle({ state }, payload) {
      // console.log(payload.crew_pk);
      // console.log(payload.article);
      try {
        await axios.post(api.crew.articles(payload.crew_pk), payload.article);
      } catch (error) {
        console.log(error);
      }
    },
    async modifyArticle({ state }, payload) {
      try {
        await axios.put(api.crew.article(payload.crew_article_pk), payload.article);
      } catch (error) {
        console.log(error);
      }
    },
    async deleteArticle({ state }, crew_article_pk) {
      console.log(crew_article_pk, "번째 글 삭제");
      console.log(state.Token);
      try {
        await axios.delete(api.crew.article(crew_article_pk));
        alert("삭제가 완료되었습니다.");
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
    async registcrew({ state }, crewData) {
      try {
        await axios.post(api.crew.crew(), crewData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        console.log("전송");
      } catch (error) {
        console.log(error);
      }
    },
    async modifyCrew({ state }, payload) {
      console.log("payload", payload);
      console.log(payload.crew_pk);
      console.log(payload.crew);
      try {
        await axios.put(api.crew.crewInfo(payload.crew_pk), payload.crew);
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
        commit("GET_CREW_MEMBERS", instance.data);
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
  },
  getters: {},
};
