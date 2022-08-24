<template>
  <h3>내 스토리</h3>

  <div v-for="story in mystory" :key="story.story_pk">
    <hr />
    <h5>
      <b>{{ story.created_at }}</b>
    </h5>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const store = useStore();

    const myStory = store.state.profile.myStory;
    console.log("myStory : ", myStory);

    return {
      myStory,
    };
  },
};
</script>

<style></style>
