<template>
  <div class="layerPopup">
    <!-- <div class="spinner"></div> -->
  </div>
</template>

<script>
import { getKakaoToken, getKakaoUserInfo } from "@/hooks/kakaologin.js";
import { useRoute } from "vue-router";
import { useCookies } from "vue3-cookies";
import { useStore } from "vuex";
import { computed } from "vue";
import router from "@/router/index.js";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const { cookies } = useCookies();
    const store = useStore();

    const setKakaoToken = async () => {
      console.log("카카오 인증 코드", route.query.code);
      const { data } = await getKakaoToken(route.query.code);
      if (data.error) {
        alert("카카오톡 로그인 오류입니다.");
        router.push({ name: "login" });
        return;
      }
      window.Kakao.Auth.setAccessToken(data.access_token);
      cookies.set("access-token", data.access_token, "1d");
      cookies.set("refresh-token", data.refresh_token, "1d");
      await setUserInfo();

      const emailCheck = { email: store.state.account.kakaoUserInfo.email };

      await axios
        .post(api.accounts.emailCheck(), emailCheck)
        .then(() => {
          alert("회원가입 페이지로 이동");
          // store.commit("account/KAKAO_LOGIN", false);
          router.push({ name: "choice" });
        })
        .catch(async () => {
          console.log("email : ", store.state.account.kakaoUserInfo.email);
          await axios
            .post(api.accounts.kakaoLogin(), emailCheck)
            .then(async (response) => {
              if (response.status === 200) {
                console.log("accounts/kakao 성공 : ", response);
                console.log("accounts/kakao data : ", response);
                const token = response.data.token;
                console.log("kakao token : ", token);
                store.commit("account/LOGIN", true);
                store.commit("account/LOGIN_ERROR", false);
                sessionStorage.setItem("token", token);
                store.commit("account/SET_LOGIN_TOKEN", token);

                await store.dispatch("account/getUserInfo", token);
                console.log("user_info : ", store.state.account.userInfo);

                console.log("로그인 성공");

                await store.dispatch(
                  "account/getMyCrewList",
                  store.state.account.userInfo.user_pk
                );
                // alert("카카오 로그인 완료!");

                router.push("/story");
              } else {
                store.commit("account/LOGIN", false);
                store.commit("account/LOGIN_ERROR", true);
                console.log("로그인 실패");
              }
            })
            .catch((err) => {
              console.log("accounts/kakao 실패 : ", err);
              if (err.response.status === 401) {
                alert("아이디 또는 비밀번호가 틀립니다.");
              }
            });
        });
    };

    const setUserInfo = async () => {
      const data = await getKakaoUserInfo();
      console.log("data : ", data);
      const kakaoUserInfo = {
        email: data.kakao_account.email,
        name: data.kakao_account.profile.nickname,
        image: data.kakao_account.profile.profile_image_url,
      };
      store.commit("account/KAKAO_LOGIN", true);
      store.commit("account/SET_KAKAO_USER_INFO", kakaoUserInfo);
    };

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    const isLoginError = computed(() => {
      return store.state.account.isLoginError;
    });

    if (route.query.code) {
      setKakaoToken();
    }

    return {
      setKakaoToken,
      setUserInfo,
      isLogin,
      isLoginError,
    };
  },
};
</script>

<style scoped>
/* .layerPopup {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 1000;
  justify-content: center;
  align-items: center;
  margin: -30px 0 0 -30px;
}
.spinner {
  position: absolute;
  top: 50%;
  left: 50%;
  border: 8px solid #f3f3f3; /* Light grey */
/* border-top: 8px solid #3498db; Blue */
/* border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spinner 2s linear infinite;
}
@keyframes spinner {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
} */
</style>
