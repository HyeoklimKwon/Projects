<template>
  <div>
    <h2>카카오 로그인 페이지</h2>
  </div>
</template>

<script>
import { getKakaoToken, getKakaoUserInfo } from "@/hooks/kakaologin.js";
import { useRoute } from "vue-router";
import { useCookies } from "vue3-cookies";
import { useStore } from "vuex";
import { computed } from "vue";
import router from "@/router/index.js";
import axios from "axios";
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



      axios
        .post(api.accounts.emailCheck(), emailCheck)
        .then(() => {
          alert("회원가입 페이지로 이동");
          router.push({ name: "choice" });
        })
        .catch(() => {

          console.log("email : ", store.state.account.kakaoUserInfo.email);
          axios
            .post(api.accounts.kakaoLogin(), emailCheck)
            .then((response) => {
              if (response.status === 200) {
                console.log("accounts/kakao 성공 : ", response);

                const token = response.data.token;
                console.log("kakao token : ", token);
                store.commit("account/LOGIN", true);
                store.commit("account/LOGIN_ERROR", false);
                sessionStorage.setItem("token", token);
                store.commit("account/SET_LOGIN_TOKEN", token);
                console.log("로그인 성공");
                alert("카카오 로그인 완료!");
                store.dispatch("account/getUserInfo", token);
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


          alert("카카오 로그인 완료!");
          router.replace("/");
        });
    };

    const setUserInfo = async () => {
      const data = await getKakaoUserInfo();
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

<style></style>
