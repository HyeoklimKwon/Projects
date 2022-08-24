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
      state.userInfo = userInfo;
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
    SAVE_STATE_TO_STORAGE: (state) => {
      console.log("state.userInfo : ", state.userInfo);
      sessionStorage.setItem("login-userInfo", JSON.stringify(state.userInfo));
      sessionStorage.setItem("login-token", state.loginToken);
    },
    READ_STATE_FROM_STORAGE: (state) => {
      if (JSON.parse(sessionStorage.getItem("login-userInfo")) != null) {
        state.userInfo = JSON.parse(sessionStorage.getItem("login-userInfo"));
      }
      if (sessionStorage.getItem("login-token") != null) {
        state.loginToken = sessionStorage.getItem("login-token");
      }
    },
    RESET_STORAGE: (state) => {
      state.userInfo = null;
      state.loginToken = "";
      sessionStorage.removeItem("login-userInfo");
      sessionStorage.removeItem("login-token");
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
            alert("아이디 또는 비밀번호가 틀립니다.");
          }
          console.log(error);
        }
      );
    },
    getUserInfo({ commit }, token) {
      // let decode_token = jwt_decode(token);
      console.log("token : ", token);
      findByToken(
        token,
        (response) => {
          if (response.status === 200) {
            console.log("response : ", response);
            commit("USER_INFO", response.data.user);
            console.log("userInfo : ", response.data.user);
            commit("SAVE_STATE_TO_STORAGE");
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
    doReadStateFromStorage({ commit }) {
      commit("READ_STATE_FROM_STORAGE");
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
  },
};

export default accountStore;
