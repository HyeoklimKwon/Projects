<template>
  <div>
    <h3>회원정보수정페이지</h3>

    <input id="update-email" type="email" disabled />
    <input id="update-password" type="password" v-model="something" />
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const userInfo = store.state.account.userInfo;

    const updatePassword = {
      old_password: null,
      password: null,
      password2: null,
    };

    const updateUserInfo = {};

    const checkPassword = () => {
      var password = prompt("비밀번호를 입력해주세요!");

      axios
        .post(api.accounts.login(), {
          email: userInfo.email,
          password: password,
        })
        .then((response) => {
          console.log("유저 정보 조회 성공 : ", response);
        })
        .catch((err) => {
          console.log("유저 정보 조회 실패 : ", err);
          router.go(-1);
          alert("비밀번호가 틀립니다!");
          checkPassword();
        });
    };

    if (!store.state.account.kakaoLogin) {
      checkPassword();
    }

    return {
      updatePassword,
      checkPassword,
    };
  },
};
</script>

<style></style>
