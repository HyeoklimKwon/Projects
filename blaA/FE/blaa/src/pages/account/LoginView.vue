<template>
  <div id="login">
    <br />
    <form>
      <input
        id="login-id"
        type="email"
        v-model="user.email"
        placeholder="Enter email"
      />
      <br />
      <input
        id="login-userpw"
        type="password"
        autocomplete="off"
        v-model="user.password"
        placeholder="Enter Password"
      />
    </form>
    <br /><br />
    <div><button @click.prevent="confirm">Login</button> <br /></div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { ref, computed } from "vue";
import router from "@/router/index.js";

export default {
  setup() {
    const store = useStore();

    const user = ref({
      email: null,
      password: null,
    });

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    const isLoginError = computed(() => {
      return store.state.account.isLoginError;
    });

    // store.dispatch("account/userConfirm");

    const confirm = async () => {
      await store.dispatch("account/userConfirm", user.value);

      let token = sessionStorage.getItem("token");
      if (isLogin.value) {
        await store.dispatch("account/getUserInfo", token);
        console.log("로그인 성공!!!!!");
        router.push("/");
      } else {
        console.log("isLogin : ", store.state.account.isLogin);
        console.log("isLoginError : ", store.state.account.isLoginError);
        console.log("로그인 안됨??????");
      }
    };

    return {
      user,
      isLoginError,
      isLogin,
      confirm,
    };
  },
};
</script>

<style></style>
