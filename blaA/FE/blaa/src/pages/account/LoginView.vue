<template>
  <div id="login">
    <div style="display: table-cell; vertical-align: middle">
      <!-- <br /> -->
      <h1 id="login-text">로그인</h1>
      <br />
      <!-- <form>
        <label for="login-id"></label>
        <input
          id="login-id"
          type="email"
          v-model="user.email"
          placeholder="EMAIL"
        /> -->
      <!-- <b>{{ message }}</b> -->
      <!-- <small>{{ emailMessage }}</small> <br /><br />

        <label for="login-password"></label>
        <input
          id="login-password"
          type="password"
          v-model="user.password"
          placeholder="PASSWORD"
          autocomplete="off"
          @keyup.enter="confirm"
        />
        <small>{{ passwordMessage }}</small>
        <br /><br /> -->
      <!-- <b>{{ message }}</b> -->

      <!-- <div class="row">
          <b-button
            class="col-sm-12"
            pill
            variant="light"
            @click.prevent="confirm"
            ><b>로그인</b></b-button
          >

          <b-button class="col-sm-12" pill variant="light" @click="register"
            ><b>회원가입</b></b-button
          >
        </div>
      </form> -->

      <!-- <div class="find-account">
        <b class="find">아이디 찾기</b> &nbsp;
        <b class="find">비밀번호 찾기</b>
      </div> -->

      <br />
      <br />
      <div style="position: relative">
        <hr style="width: 25%; float: left" />
        <b style="font-size: 20px; text-align: center">소셜 로그인</b>
        <hr style="width: 25%; float: right" />
      </div>

      <br />
      <img
        id="login-kakao"
        src="@/img/KakaoLogo.png"
        @click.prevent="kakaoLogin"
      />
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { ref, computed } from "vue";
import router from "@/router/index.js";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();

    const user = ref({
      email: null,
      password: null,
    });

    const emailMessage = ref(null);
    const passwordMessage = ref(null);

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    const isLoginError = computed(() => {
      return store.state.account.isLoginError;
    });

    // store.dispatch("account/userConfirm");

    const confirm = async () => {
      let err = true;

      if (!user.value.email) {
        err = true;
        emailMessage.value = "이메일을 입력해주세요";
        setTimeout(() => {
          emailMessage.value = "";
          err = false;
        }, 3000);
      }

      if (!user.value.password) {
        err = true;
        passwordMessage.value = "비밀번호를 입력해주세요.";
        setTimeout(() => {
          passwordMessage.value = "";
          err = false;
        }, 3000);
      }

      if (!err) {
        return;
      } else {
        await store.dispatch("account/userConfirm", user.value);

        let token = sessionStorage.getItem("token");
        console.log("Login Token : ", token);
        if (isLogin.value) {
          await store.dispatch("account/getUserInfo", token);
          console.log("로그인 성공!!!!!");
          await store.dispatch(
            "account/getMyCrewList",
            store.state.account.userInfo.user_pk
          );
          router.push("/story");
        } else {
          console.log("isLogin : ", store.state.account.isLogin);
          console.log("isLoginError : ", store.state.account.isLoginError);
          console.log("로그인 안됨??????");
        }
      }
    };

    const register = () => {
      router.push({ name: "signup" });
    };

    const kakaoLogin = () => {
      const params = {
        redirectUri: "https://i7b209.p.ssafy.io/kakao",
        // redirectUri: "http://localhost:3000/kakao",
      };
      window.Kakao.Auth.authorize(params);
    };

    return {
      user,
      emailMessage,
      passwordMessage,
      isLoginError,
      isLogin,
      confirm,
      register,
      kakaoLogin,
    };
  },
};
</script>

<style scoped>
#login {
  padding: 40px;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  overflow: auto;
  text-align: center;
  display: table;
  width: 100%;
  height: 100%;

  -webkit-animation: fade-in 1.2s cubic-bezier(0.39, 0.575, 0.565, 1) both;
  animation: fade-in 1.2s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}

@-webkit-keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

#login-text {
  font-family: "Inter";
  font-style: normal;
  font-weight: 700;
  font-size: 35px;
  line-height: 42px;
  text-align: center;
}

label {
  float: left;
  font-family: "Inter";
  font-style: normal;
  font-weight: bold;
  color: black;
}

input {
  width: 100%;
  height: 50px;
  padding: 5px;
  border: solid 2px #d9d9d9;
  border-radius: 8px;
}

small {
  float: left;
  font-family: Inter;
  font-style: normal;
  font-size: 15px;
  color: red;
}

input::placeholder {
  color: #d9d9d9;
}

input:focus {
  border: 2px #eec95c solid;
  outline: none;
}

button {
  margin-bottom: 10px;
}

.row {
  padding: 10px;
}

.find-account {
  float: right;
  /* margin-top: 10px; */
}

.find {
  font-size: 12px;
  color: gray;
}

#login-kakao {
  width: 50px;
  height: 50px;
}
</style>
