<template>
  <div>크루 삭제 처리중. . .</div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();

    const dele = async () => {
      await store.dispatch("crew/deleteCrew", route.params.crew_pk);
      await store.dispatch("account/getMyCrewList", store.state.account.userInfo.user_pk);
      router.push({ name: "allcrewlist" });
    };

    dele();
  },
};
</script>

<style></style>
