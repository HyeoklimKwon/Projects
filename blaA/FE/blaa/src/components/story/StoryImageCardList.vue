<template>
  <div class="wrapper">
    <div class="cards" v-if="images">
      <StroyImageCard v-for="image in images" :key="image.story_pk" :image="image" />
    </div>
    <div class="cards-loading" v-else>Loading image....</div>
  </div>
</template>

<script>
// import { useStore } from 'vuex'
import StroyImageCard from "@/components/story/StoryImageCard.vue";
import { computed, onBeforeMount, ref } from "vue";
import $ from "jquery";

export default {
  components: {
    StroyImageCard,
  },
  props: {
    images: {
      type: Array,
      required: true,
    },
  },
  setup() {},
};
</script>

<style scoped>
.wrapper .cards {
  display: grid;
  /* 행, 열간격 설정 */
  column-gap: 15px;
  row-gap: 10px;
  /* 행 갯수와 크기 설정, 추후에 모바일 크기에 따라서 조정 or 반응형으로 설정하면 될듯 */
  grid-template-columns: 45% 45%;
  justify-content: center;
  max-width: var(--card-container-width / 2);
}
</style>
