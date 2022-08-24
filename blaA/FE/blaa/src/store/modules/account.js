// import jwt_decode from "jwt-decode";
import { login, findByToken } from "@/hooks/user.js";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

const accountStore = {
  namespaced: true,
  state: {
    isLogin: false,
    isLoginError: false,
    userInfo: null,
    kakaoUserInfo: {
      email: null,
      name: null,
      image: null,
    },
    kakaoLogin: false,
    signupUser: {
      email: null,
      password: null,
      name: null,
      nickname: null,
      tel: null,
      region: null,
      category: null,
      is_alba: false,
      image: null,
    },
    category: [],
    si: [],
    gu: [],
    dong: [],
    loginToken: null,
  },
  getters: {
    dong_list(state) {
      let dong = state.dong;
      dong.shift();
      return dong;
    },
    signup_user(state) {
      let signupUser = state.signupUser;
      return signupUser;
    },
  },
  mutations: {
    LOGIN: (state, isLogin) => {
      state.isLogin = isLogin;
    },
    LOGIN_ERROR: (state, isLoginError) => {
      state.isLoginError = isLoginError;
    },
    USER_INFO: (state, userInfo) => {
      state.isLogin = true;
      console.log("받아오는 userInfo : ", userInfo);
      state.userInfo = userInfo;
      console.log("state.userInfo : ", state.userInfo);
    },
    ADD_MY_CREW: (state, crewList) => {
      state.userInfo.crew = crewList;
      console.log("크루 추가 후 userInfo : ", state.userInfo);
    },
    ADD_NEW_CREW: (state, crew) => {
      state.userInfo.crew.push(crew);
      console.log(state.userInfo.crew);
    },
    SET_KAKAO_USER_INFO: (state, kakaoUserInfo) => {
      state.kakaoUserInfo.email = kakaoUserInfo.email;
      state.kakaoUserInfo.name = kakaoUserInfo.name;
      state.kakaoUserInfo.image = kakaoUserInfo.image;
    },
    KAKAO_LOGIN: (state, kakaoLogin) => {
      state.kakaoLogin = kakaoLogin;
    },
    SET_SIGNUP_EMAIL: (state, email) => {
      state.signupUser.email = email;
    },
    SET_SIGNUP_PASSWORD: (state, password) => {
      state.signupUser.password = password;
    },
    SET_SIGNUP_NAME: (state, name) => {
      state.signupUser.name = name;
    },
    SET_SIGNUP_NICKNAME: (state, nickname) => {
      state.signupUser.nickname = nickname;
    },
    SET_SIGNUP_TEL: (state, tel) => {
      state.signupUser.tel = tel;
    },
    SET_SIGNUP_REGION: (state, region) => {
      state.signupUser.region = region;
    },
    SET_SIGNUP_CATEGORY: (state, category) => {
      state.signupUser.category = category;
    },
    SET_SIGNUP_ALBA: (state, is_alba) => {
      state.signupUser.is_alba = is_alba;
    },
    SET_SIGNUP_IMAGE: (state, image) => {
      state.signupUser.image = image;
    },
    GET_SIGNUP_USER: (state, user) => {
      state.signupUser = user;
    },
    GET_CATEGORY_LIST: (state, payload) => {
      state.category = payload;
    },
    GET_SI_LIST: (state, payload) => {
      state.si = payload;
    },
    GET_GU_LIST: (state, payload) => {
      state.gu = payload;
    },
    GET_DONG_LIST: (state, payload) => {
      state.dong = payload;
    },
    SET_LOGIN_TOKEN: (state, token) => {
      state.loginToken = token;
    },
  },
  actions: {
    async userConfirm({ commit }, user) {
      await login(
        user,
        (response) => {
          if (response.status === 200) {
            let token = response.data["token"];
            commit("LOGIN", true);
            commit("LOGIN_ERROR", false);
            sessionStorage.setItem("token", token);
            commit("SET_LOGIN_TOKEN", token);

            console.log("로그인성공");
          } else {
            commit("LOGIN", false);
            commit("LOGIN_ERROR", true);
            console.log("로그인 실패");
          }
        },
        (error) => {
          console.log("error request status : ", error.request.status);
          if (error.response.status === 401) {
            if (user.email && user.password) {
              alert("아이디 또는 비밀번호가 틀립니다.");
            }
          }
          console.log(error);
        }
      );
    },
    async getUserInfo({ commit }, token) {
      // let decode_token = jwt_decode(token);
      console.log("token : ", token);
      await findByToken(
        token,
        (response) => {
          if (response.status === 200) {
            console.log("response : ", response);
            var userInfo = response.data.user;
            userInfo.token = userInfo.token.slice(2, -1);
            console.log("변경된 userInfo", userInfo);
            commit("USER_INFO", userInfo);
            console.log("userInfo : ", userInfo);
          } else {
            console.log("유저 정보 없음");
          }
        },
        (error) => {
          console.log("에러코드 : ", error.status);
          console.log("getUserInfo 에러", error);
        }
      );
    },
    getCategoryList(context) {
      axios.get(api.categorys.job()).then(({ data }) => {
        context.commit("GET_CATEGORY_LIST", data);
      });
    },
    getSiList(context) {
      axios.get(api.categorys.region()).then(({ data }) => {
        context.commit("GET_SI_LIST", data);
      });
    },
    getGuList(context, sido) {
      const sido_substr = sido.substr(0, 2);
      axios.get(api.categorys.region() + sido_substr + "/").then(({ data }) => {
        context.commit("GET_GU_LIST", data);
      });
    },
    getDongList(context, region) {
      const sido_substr = region.sido.substr(0, 2);
      const gugun_substr = region.gugun.substr(2, 2);
      axios
        .get(api.categorys.region() + sido_substr + "/" + gugun_substr + "/")
        .then(({ data }) => {
          context.commit("GET_DONG_LIST", data);
        });
    },
    async getMyCrewList(context, user_pk) {
      console.log("user_pk : ", user_pk);
      await axios
        .get(api.profile.myCrew(user_pk))
        .then((response) => {
          console.log("crew list : ", response.data);
          const crew = response.data;
          context.commit("ADD_MY_CREW", crew);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};

export default accountStore;
