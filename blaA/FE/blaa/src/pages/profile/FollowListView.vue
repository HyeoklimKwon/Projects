<template>
  <br />
  <div v-if="followerList">
    <h3><b>팔로워 페이지</b></h3>
    <hr />
    <div v-for="follower in followers" :key="follower.user_pk"></div>
  </div>
  <div v-else>
    <h3><b>팔로잉 페이지</b></h3>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import api from "@/api/api.js";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { computed } from "vue";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    // if(route.params.followType === "follower") {
    //   store.dispatch("profile/getMyFollower")
    // } else {

    // }

    const followerList = computed(() => {
      if (route.params.followType === "follower") {
        return true;
      }
      return false;
    });

    return {
      followerList,
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
