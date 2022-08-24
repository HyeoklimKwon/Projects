<template>
  <div></div>
</template>

<script>
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const store = useStore();

    const token = sessionStorage.getItem("token");

    // axios.get(api.profile.myCrew(route.params.user_pk), {
    //   headers: {
    //     Authorization: `Bearer ${token}`,
    //   },
    // })
    store.dispatch("profile/getMyCrew", route.params.user_pk);

    return {};
  },
};
</script>

<style></style>
