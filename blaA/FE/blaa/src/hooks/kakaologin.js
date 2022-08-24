import axios from "axios";
import VueCookies from "vue3-cookies";

// const KakaoHeader = {
//   Autorization: "ef3fff1b178e80bed777a9b87ac2fff3",
//   "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
// };

const getKakaoToken = async (code) => {
  console.log("loginWithKakao");
  try {
    const data = {
      grant_type: "authorization_code",
      client_id: "0f5982ee3aa76733f951e5add93878c1",
      // redirect_uri: "http://127.0.0.1:8000/account/sign-in/kakao/callback",
      redirect_uri: "http://localhost:8080/kakao",
      code: code,
    };
    // const queryString = Object.keys(data)
    //   .map((k) => encodeURIComponent(k) + "=" + encodeURIComponent(data[k]))
    //   .join("&");
    // console.log(
    //   ("https://kauth.kakao.com/oauth/token",
    //   queryString,
    //   { headers: KakaoHeader })
    // );
    // const result = await axios.post(
    //   "https://kauth.kakao.com/oauth/token",
    //   queryString,
    //   { headers: KakaoHeader }
    // );
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

export { getKakaoToken, getKakaoUserInfo, refreshToken };
