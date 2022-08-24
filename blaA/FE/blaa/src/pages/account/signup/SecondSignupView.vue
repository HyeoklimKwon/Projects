<template>
  <h3>회원가입 2단계</h3>
  <div id="signup">
    <br />
    <form>
      <input
        id="signup-email"
        type="email"
        v-model="user.email"
        placeholder="Enter email"
      />
      &nbsp;
      <button id="btnEmailCheck" @click.prevent="emailCheck">중복확인</button>
      <br />

      <b id="password-form">
        <input
          id="signup-password"
          type="password"
          autocomplete="off"
          v-model="user.password"
          placeholder="Enter password"
        />
        <br />

        <input
          id="signup-checkpassword"
          type="password"
          autocomplete="off"
          placeholder="Check password"
        />
        <br />
      </b>

      <input id="signup-name" v-model="user.name" placeholder="Enter name" />
      <br />

      <input id="signup-tel1" v-model="user.tel1" placeholder="Enter tel" />
      <b> - </b>
      <input id="signup-tel2" v-model="user.tel2" />
      <b> - </b>
      <input id="signup-tel3" v-model="user.tel3" />
    </form>
    <br /><br />
    <div>
      <button @click.prevent="before">이전</button> &nbsp;
      <button @click.prevent="next">다음</button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import { useCookies } from "vue3-cookies";
import router from "@/router/index.js";
import axios from "axios";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();
    const { cookies } = useCookies();

    const user = ref({
      email: null,
      password: null,
      name: null,
      tel1: null,
      tel2: null,
      tel3: null,
    });

    onMounted(() => {
      const kakaoLogin = store.state.account.kakaoLogin;
      console.log("kakaoLogin : ", kakaoLogin);
      if (kakaoLogin) {
        user.value.email = store.state.account.kakaoUserInfo.email;
        document.getElementById("signup-email").disabled = true;
        document.getElementById("btnEmailCheck");

        user.value.password = cookies.get("access-token");
        document.getElementById("signup-password").style.display = "none";
        document.getElementById("signup-checkpassword").style.display = "none";
        document.getElementById("password-form").innerHTML = "";

        user.value.name = store.state.account.kakaoUserInfo.name;
        document.getElementById("signup-name").disabled = true;
      }
    });

    const emailCheck = () => {
      if (user.value.email == null) {
        alert("먼저 이메일을 입력해주세요.");
      } else {
        console.log(user.value.email);
        const sendEmail = { email: user.value.email };
        axios
          .post(api.accounts.emailCheck(), sendEmail)
          .then((response) => {
            console.log(response.status);
            if (response.status === 200 || response.status === 201) {
              alert("사용 가능한 이메일입니다.");
            }
          })
          .catch((error) => {
            console.log("error : ", error);
            alert("이미 사용중인 이메일입니다.");
            user.value.email = null;
          });
      }
    };

    const before = () => {
      router.go(-1);
    };

    const next = () => {
      let err = true;
      let msg = "";

      err &&
        !user.value.email &&
        ((msg = "이메일을 입력해주세요"), (err = false));

      if (!store.state.account.kakaoLogin) {
        err &&
          !user.value.password &&
          ((msg = "비밀번호를 입력해주세요"), (err = false));
        err &&
          user.value.password.length < 6 &&
          ((msg = "비밀번호는 6자리 이상이어야 합니다."), (err = false));
        err &&
          user.value.password !=
            document.getElementById("signup-checkpassword").value &&
          ((msg = "비밀번호가 일치하지 않습니다."), (err = false));
      }

      err && !user.value.name && ((msg = "이름을 입력해주세요"), (err = false));

      if (!err) {
        alert(msg);
      } else {
        const tel =
          user.value.tel1 + "-" + user.value.tel2 + "-" + user.value.tel3;

        store.commit("account/SET_SIGNUP_EMAIL", user.value.email);
        store.commit("account/SET_SIGNUP_PASSWORD", user.value.password);
        store.commit("account/SET_SIGNUP_NAME", user.value.name);
        store.commit("account/SET_SIGNUP_TEL", tel);

        router.push({ name: "category" });
      }
    };

    return {
      user,
      emailCheck,
      before,
      next,
    };
  },
};
</script>

<style></style>
