<template>
  <!-- <div class="header">
    <div v-if="userInfo">
      <div v-if="isKakaoLogin">
        <p style="float: left">{{ userInfo.nickname }} 님</p>
        &nbsp;
        <img src="@/img/KakaoLogo.png" width="60" height="26" />
      </div>
      <div v-else>
        <p>{{ userInfo.nickname }} 님</p>
      </div>
    </div>
    <div v-else>
      <p>로그인이 필요합니다.</p>
      <button type="button" @click="login">로그인</button>
      &nbsp;
      <button type="button" @click="kakaoLogin">카카오 로그인</button>
      &nbsp;
      <button @click="register">회원가입</button>
    </div>
  </div> -->
  <div class="header"></div>
</template>

<script>
import { useStore } from "vuex";
import { computed, onMounted } from "vue";
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

    const login = () => {
      router.push({ name: "login" });
    };

    const kakaoLogin = () => {
      const params = {
        redirectUri: "https://i7b209.p.ssafy.io/kakao",
        // redirectUri: "http://127.0.0.1:8000/account/sign-in/kakao/callback",
      };
      window.Kakao.Auth.authorize(params);
    };

    // const logout = () => {
    //   store.commit("account/LOGIN", false);
    //   store.commit("account/USER_INFO", null);
    //   sessionStorage.removeItem("token");
    //   store.commit("account/RESET_STORAGE");
    //   router.replace("/");
    // };

    const register = () => {
      router.push({ name: "signup" });
    };

    return {
      isLogin,
      isKakaoLogin,
      userInfo,
      login,
      kakaoLogin,

      register,
    };
  },
};
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 364px;
  height: 24px;
}
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
