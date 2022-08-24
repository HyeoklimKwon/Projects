<template>
  <br />
  <div v-if="isFollower">
    <h3><b>팔로워 페이지</b></h3>
    <hr />
    <div class="container">
      <div
        v-for="follower in followerList.results"
        :key="follower.user_pk"
        style="width: 100%"
      >
        <div class="d-flex justify-content-between row">
          <img
            :src="follower.image"
            style="width: 5rem; height: 3.5rem; border-radius: 50%"
            @click="userProfile(follower.user_pk)"
          />
          <h5 class="col-9 mt-3 mb-0" style="font-weight: bold">
            {{ follower.nickname }}
          </h5>
        </div>
        <hr />
      </div>
    </div>
  </div>

  <div v-else>
    <h3><b>팔로잉 페이지</b></h3>
    <hr />
    <div
      class="container"
      v-for="following in followingList.results"
      :key="following.user_pk"
      style="width: 100%"
    >
      <div class="d-flex justify-content-between row">
        <img
          :src="following.image"
          style="width: 5rem; height: 3.5rem; border-radius: 50%"
          @click="userProfile(following.user_pk)"
        />
        <h5 class="col-9 mt-3 mb-0" style="font-weight: bold">
          {{ following.nickname }}
        </h5>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref, computed, onBeforeMount } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    const followerList = store.state.profile.followerList;
    const followingList = store.state.profile.followingList;

    const currentPage = ref(1);
    const numberOfPages = ref(1);

    if (route.params.followType === "follower") {
      followerList.value = store.state.profile.followerList;
      // store.dispatch("profile/getFollowerList", route.params.user_pk);
      console.log("followerList : ", followerList.value);
    } else {
      followingList.value = store.state.profile.followingList;
      console.log("followingList : ", followingList.value);
    }

    const isFollower = computed(() => {
      if (route.params.followType === "follower") {
        return true;
      }
      return false;
    });

    const getMoreList = async (page = currentPage.value) => {
      const data = {
        page: currentPage.value,
        user_pk: route.params.user_pk,
      };

      if (isFollower.value) {
        await store.dispatch("profile/getFollowerList", data);
        numberOfPages.value = computed(() => {
          return Math.ceil(followerList.value.count / 10);
        });
      } else {
        await store.dispatch("profile/getFollowingList", data);
        numberOfPages.value = computed(() => {
          return Math.ceil(followingList.value.count / 10);
        });
      }
    };

    window.onscroll = function (e) {
      if (numberOfPages.value.value > currentPage.value) {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
          setTimeout(function () {
            if (numberOfPages.value.value > currentPage.value) {
              currentPage.value += 1;

              getMoreList();
            }
          }, 1000);
        }
      }
    };

    const userProfile = (user_pk) => {
      console.log("다른 유저 프로필 페이지 이동");
      router.push({
        name: "userProfile",
        params: {
          user_pk: user_pk,
        },
      });
    };

    getMoreList();

    return {
      followerList,
      followingList,
      isFollower,
      getMoreList,
      currentPage,
      numberOfPages,
      userProfile,
    };
  },
};
</script>

<style></style>
