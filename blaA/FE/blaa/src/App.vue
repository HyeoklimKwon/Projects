<template>
  <h1>메인페이지</h1>

  <div v-if="userInfo">
    <div v-if="isKakaoLogin">
      <p style="float: left">{{ userInfo.nickname }} 님</p>
      &nbsp;
      <img src="@/img/KakaoLogo.jpg" width="60" height="26" />
    </div>
    <div v-else>
      <p>{{ userInfo.nickname }} 님</p>
    </div>
    <br />

    <button @click.prevent="logout">로그아웃</button>
    <button @click.prevent="gochatroom">채팅하러가기</button>
    <button @click.prevent="gostory">오출완가기</button>
    <button @click.prevent="gosearch">유저정보검색하기</button>
    <button @click.prevent="goMyProfile">마이프로필</button>
    <button @click.prevent="gocrew">크루가기</button>
  </div>

  <div v-else>
    <p>로그인이 필요합니다.</p>
    <button type="button" @click="login">로그인</button>
    &nbsp;
    <button type="button" @click="kakaoLogin">카카오 로그인</button>
    &nbsp;
    <button @click="register">회원가입</button>
  </div>
  <router-view></router-view>
</template>

<script>
// import axios from 'axios';
import { useStore } from "vuex";
import { computed, onMounted } from "vue";
// import router from "@/router/index.js";
import { useRouter } from "vue-router";

export default {
  setup() {
    // // vuex store 사용법 예제
    const store = useStore();
    const router = useRouter();

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    const isKakaoLogin = computed(() => {
      return store.state.account.kakaoLogin;
    });

    const userInfo = computed(() => {
      return store.state.account.userInfo;
    });

    onMounted(() => {
      store.dispatch("account/doReadStateFromStorage");
    });

    const login = () => {
      router.push({ name: "login" });
    };

    const gochatroom = () => {
      router.push({ path: "/chatroom" });
    };

    const gostory = () => {
      router.push({ path: "/story" });
    };

    const gosearch = () => {
      router.push({ path: "/searchusers" });
    };

    const gocrew = () => {
      router.push({ path: "/crew" });
    };

    const goMyProfile = async () => {
      await store.dispatch("profile/getMyFollower", userInfo.value.user_pk);
      await store.dispatch("profile/getMyFollowing", userInfo.value.user_pk);
      router.push({ path: "/profile" });
    };

    const kakaoLogin = () => {
      const params = {
        redirectUri: "http://localhost:8080/kakao",
        // redirectUri: "http://127.0.0.1:8000/account/sign-in/kakao/callback",
      };
      window.Kakao.Auth.authorize(params);
    };

    const logout = () => {
      store.commit("account/LOGIN", false);
      store.commit("account/USER_INFO", null);
      sessionStorage.removeItem("token");
      store.commit("account/RESET_STORAGE");
      router.replace("/");
    };

    const register = () => {
      router.push({ name: "signup" });
    };

    return {
      isLogin,
      isKakaoLogin,
      userInfo,
      login,
      kakaoLogin,
      logout,
      register,
      gochatroom,
      gostory,
      gosearch,
      gocrew,
      goMyProfile,
    };
  },
};
</script>

<style>
#profile {
  width: 150px;
  height: 150px;
  border-radius: 70%;
  overflow: hidden;
}

#imgProfile {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
