<template>
  <div>탈퇴 처리중 ...</div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();

    const leader_pk = store.state.crew.crewInfo.crew_leader_pk;
    const user_pk = store.state.account.userInfo.user_pk;

    const dele = async () => {
      await store.dispatch("crew/leaveCrew", route.params.crew_pk);
      router.push({ name: "allcrewlist" });
    };

    if (leader_pk == user_pk) {
      alert("크루장은 탈퇴가 불가능합니다.");
      router.push({ name: "crewdetail", params: { crew_pk: route.params.crew_pk } });
    } else {
      dele();
    }
  },
};
</script>

<style></style>
