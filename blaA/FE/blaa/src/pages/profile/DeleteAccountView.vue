<template>
  <div></div>
</template>

<script>
import axios from "@/api/axios.js";
import api from "@/api/api";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { deleteKakaoAccount } from "@/hooks/kakaologin.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    var result = confirm("정말로 탈퇴하시겠습니까?");

    async () => {
      if (result) {
        console.log(api.profile.myInfo(route.params.user_pk));
        await axios
          .delete(api.profile.myInfo(route.params.user_pk))
          .then((response) => {
            console.log("response : ", response);
            deleteKakaoAccount();
            alert("탈퇴가 완료되었습니다.");
            store.commit("account/LOGIN", false);
            store.commit("account/USER_INFO", null);
            sessionStorage.removeItem("token");
            router.replace("/");
          })
          .catch((err) => {
            alert("회원 탈퇴 에러");
            console.log(err);
          });
      } else {
        router.go(-1);
      }
    };

    return {};
  },
};
</script>

<style></style>
