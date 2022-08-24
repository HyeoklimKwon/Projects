<template>
  <div>
    <div class="row" id="top_box">
      <div class="col-2" id="top_box_text" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
      <h5 class="col-8" id="top_box_text">게시글</h5>
      <div class="col-2" id="top_box_text"><img src="@/assets/icons/search.png" /></div>
    </div>
    <article-list></article-list>
    <div class="plusbutton" @click="moveRegist">
      <img src="@/assets/icons/edit_btn_w.png" />
    </div>
  </div>
</template>

<script>
import ArticleList from "@/components/crew/article/ArticleList.vue";
import { useRouter } from "vue-router";
export default {
  components: {
    ArticleList,
  },
  setup() {
    const router = useRouter();
    const moveRegist = () => {
      router.push({ name: "articleregist" });
    };
    const back = () => {
      router.go(-1);
    };
    return {
      moveRegist,
      back,
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
  line-height: 55px;
}

.rectangle {
  position: fixed;
  width: 50px;
  height: 50px;
  top: 700px; /* 윗쪽 끝에서부터의 거리 */
  right: 50%;
  margin-right: -170px; /* 가운데를 기준으로 오른쪽 거리 */
  z-index: 99;

  background: #498d6d;
  border-radius: 50%;
}

.plusbutton {
  position: fixed;
  z-index: 10;
  bottom: 80px;
  right: 20px;
  width: 50px;
  height: 50px;
  color: black;
  border-radius: 50%;
  margin: 10px;
}
</style>
