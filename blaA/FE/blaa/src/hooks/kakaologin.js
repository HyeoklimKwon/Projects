import axios from "@/api/axios.js";
import VueCookies from "vue3-cookies";

const getKakaoToken = async (code) => {
  console.log("loginWithKakao");
  try {
    const data = {
      grant_type: "authorization_code",
      client_id: process.env.VUE_APP_KAKAO_REST_API,
      redirect_uri: "https://i7b209.p.ssafy.io/kakao",
      // redirect_uri: "http://localhost:3000/kakao",
      code: code,
    };
    console.log("data.client_id : ", data.client_id);
    const result = await axios.post(
      "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=" +
        data.client_id +
        "&redirect_uri=" +
        data.redirect_uri +
        "&code=" +
        data.code
    );
    console.log("카카오 토큰", result);
    return result;
  } catch (e) {
    return e;
  }
};

const getKakaoUserInfo = async () => {
  let data = "";
  await window.Kakao.API.request({
    url: "/v2/user/me",
    success: function (response) {
      data = response;
    },
    fail: function (error) {
      console.log(error);
    },
  });
  console.log("카카오 계정 정보", data);

  return data;
};

const refreshToken = async () => {
  try {
    const { result } = (await axios.get("/refreshToken")).data;
    VueCookies.set("access-token", result.access_token);
    console.log("Refresh API 성공", result);
    return result;
  } catch (e) {
    console.log(e);
  }
};

const kakaoLogout = () => {
  window.Kakao.isInitialized();

  if (!window.Kakao.Auth.getAccessToken()) {
    console.log("Not logged in");
    return;
  }

  window.Kakao.Auth.logout(function () {
    console.log(window.Kakao.Auth.getAccessToken());
  });
};

const deleteKakaoAccount = () => {
  window.Kakao.isInitialized();

  window.Kakao.API.request({
    url: "/v1/user/unlink",
    success: function (response) {
      console.log(response);
    },
    fail: function (error) {
      console.log(error);
    },
  });
};

export {
  getKakaoToken,
  getKakaoUserInfo,
  refreshToken,
  kakaoLogout,
  deleteKakaoAccount,
};
