<template>
  <!-- <div>
    <div class="row" id="top_box">
      <div class="col-2" style="line-height: 55px" @click="moveList">
        <img src="@/assets/icons/close_w.png" />
      </div>
      <h5 class="col-8" id="top_box_text">게시글 작성</h5>
      <div class="col-2"></div>
    </div>
  </div> -->
  <div class="row" id="top_box">
    <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="moveList"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-6" id="top_box_text">게시글 작성</h5>
    <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px">
      <!-- <button class="submit-btn" @click="sumbitReview">등록</button> -->
    </div>
  </div>
  <article-input-item type="regist"></article-input-item>
</template>

<script>
import ArticleInputItem from "./Items/ArticleInputItem.vue";
import { useRouter } from "vue-router";
export default {
  components: { ArticleInputItem },
  setup() {
    const router = useRouter();
    const moveList = () => {
      router.go(-1);
    };

    return {
      moveList,
    };
  },
};
</script>

<style scoped>
#top_box {
  height: 55px;
  margin: auto;

  color: white;
  background-color: #498d6d;
}

#top_box_text {
  /* display: flex; */
  text-align: center;
  line-height: 60px;
}
</style>
