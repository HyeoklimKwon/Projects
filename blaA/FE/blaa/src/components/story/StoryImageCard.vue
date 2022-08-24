<template>
  <!-- 작성자프로필, 제목, 작성자와 좋아요 현황 추가해야 됨 -->
    <div
    v-if="image.story_picture"
    class="grid-item"
    :style="{
      height: tH.value + 'px',
      gridRowEnd: gap.value,
    }"
  >
    <div @click="moveToDetail" style="cursor: pointer">
      <img :src="host + image.story_picture" class="image" :style="{ width: '100%', borderRadius: '10px' }" />
    </div>
    <div class="storyInfo">
      <div class="row">
        <div class="col-2">
          <img v-if="image"
            :src="host + image.user_pk.image"
            alt="프로필"
            @click="moveToProfile"
            style="width: 34px; height: 34px; cursor: pointer; border-radius: 50%; object-fit: cover"
          />
        </div>
        <div class="col-10">
          <div style="padding-left: 10px; padding-right: 5px; width: 100%">
            <p style="font-size: 12px">{{ image.story_title }}</p>
            <!-- created at 현재 시간이랑 비교 -->
            <div class="userInfo">
              <div style="font-size: 10px">{{ image.user_pk.nickname }}</div>
              <div style="font-size: 10px">{{ image.created_at }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
import { ref, computed } from "vue";
import { round } from "mathjs";
import { useRouter } from "vue-router";
import $ from "jquery";
import api from "@/api/api";

export default {
  components: {},
  props: {
    image: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const router = useRouter();
    const tH = ref(0);
    const gap = ref("");
    const width = ref(0);
    const height = ref(0);
    // 로컬에서는 해당 형식으로 작동
    const host = ref("https://i7b209.p.ssafy.io");
    const time = ref("");
    // const host = ref(api.story.host());

    // 이미지 크기 설정
    $(document).ready(function () {
      $("<img/>")
        .attr("src", host.value + props.image.story_picture)
        .on("load", function () {
          width.value = this.naturalWidth;
          height.value = this.naturalHeight;

          const windowWidth = window.innerWidth / (20 / 9);

          tH.value = computed(() => {
            return round(height.value / (width.value / windowWidth) + 48);
          });

          gap.value = computed(() => {
            return `span ${round(tH.value.value / 10)}`;
          });
        });
    });

    $(window).resize(function () {
      const windowWidth = window.innerWidth / (20 / 9);

      tH.value = computed(() => {
        return round(height.value / (width.value / windowWidth) + 48);
      });

      gap.value = computed(() => {
        return `span ${round(tH.value.value / 10)}`;
      });
    });

    const moveToProfile = () => {
      router.push({
        name: "userProfile",
        params: {
          user_pk: props.image.user_pk.user_pk,
        },
      });
    };

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
      moveToProfile,
    };
  },
};
</script>

<style scoped>
.storyInfo {
  display: flex;
  grid-template-columns: 25% 75%;
  margin-top: 5px;
}

p {
  margin: 0;
  font-size: 16px;
  font-weight: bold;
}

.userInfo {
  margin-top: 2px;
  display: flex;
  justify-content: space-between;
  font-size: 12px;
}
</style>
