<template>
  <!-- 작성자프로필, 제목, 작성자와 좋아요 현황 추가해야 됨 -->
  <div
    class="grid-item"
    :style="{
      height: tH + 'px',
      gridRowEnd: gap,
      backgroundColor: 'gray',
      borderRadius: '10px',
    }"
  >
    <div class="image" @click="moveToDetail" style="cursor: pointer">
      <img :src="host + image.story_picture" class="image" :style="{ width: '100%' }" />
      <span>{{ image.user_pk.nickname }}</span>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { round } from "mathjs";
import { useRouter } from "vue-router";
// import api from '@/api/api'

export default {
  props: {
    image: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const router = useRouter();
    const tH = ref(null);
    const gap = ref(null);
    const host = ref("http://localhost:8000");

    tH.value = round(props.image.height / (props.image.width / 200)) + 30;
    gap.value = round(tH.value / 10);
    gap.value = `span ${gap.value}`;

    const moveToDetail = () => {
      console.log(props.image);
      router.push({
        name: "detailStory",
        params: {
          story_pk: props.image.story_pk,
        },
      });
    };

    return {
      tH,
      gap,
      moveToDetail,
      host,
    };
  },
};
</script>

<style></style>
