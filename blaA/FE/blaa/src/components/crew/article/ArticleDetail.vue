<template>
  <div class="row" id="top_box">
    <div class="col-2" id="top_box_text" @click="moveBack">
      <img src="@/assets/icons/arrow-left.png" />
    </div>
    <h5 class="col-8" id="top_box_text">게시글</h5>
    <div class="col-2" id="top_box_text"></div>
  </div>
  <div style="padding: 20px 20px 0px 20px">
    <div>
      <h3 id="title_text" style="margin: 0; font-weight: 800">
        {{ article.crew_title }}
      </h3>
      <div class="row">
        <div id="profile" class="col-2" style="padding-bottom: 10px">
          <img
            class="imgProfile"
            :src="article.profile"
            width="40"
            height="40"
            style="float: right; margin-top: 15px; padding-right: 0"
          />
        </div>
        <div
          class="col-10 d-flex justify-content-between"
          style="padding-top: 10px; padding-left: 0"
        >
          <div>
            <p id="semi_title_text" style="margin: 0">
              {{ article.nickname }}
            </p>
            <p id="small_title_text">{{ yyyyMMdd(article.created_at) }}</p>
          </div>
          <div v-if="article.user == now_user" style="margin: auto 0">
            <span
              @click="isUpdtae = !isUpdate"
              style="font-size: 30px"
              class="material-symbols-outlined"
              >menu</span
            >
            <div id="update" v-if="isUpdtae">
              <button class="button" @click="articlemodify">수정</button>
              <button class="button" @click="articledele">삭제</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <hr style="margin: 0" />

  <div style="padding: 20px 20px 0px 20px">
    <div>
      <div style="font-size: 13px">{{ article.crew_content }}</div>
      <template v-for="image in article.images" :key="image">
        <img class="contentImg" :src="host + image.article_picture" />
        {{ image.crew_article_pk }}
      </template>
    </div>
  </div>
  <hr />

  <div style="padding: 0px 20px 0px 20px">
    <comment-list></comment-list>
  </div>
</template>

<script>
import { dataChange } from "@/hooks/dateChange";
import { useStore } from "vuex";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import CommentList from "@/components/crew/article/Comment/CommentList.vue";
export default {
  components: {
    CommentList,
  },
  setup() {
    const { yyyyMMdd } = dataChange();
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const article = ref([]);
    const host = ref("https://i7b209.p.ssafy.io");
    const now_user = store.state.account.userInfo.user_pk;
    const isUpdtae = ref(false);

    onMounted(async () => {
      await store.dispatch(
        "crew/getArticleDetail",
        route.params.crew_article_pk
      );
      article.value = store.state.crew.article;
      console.log("이미지", article.value.images);
    });

    const articlemodify = () => {
      router.push({ name: "articlemodify" });
    };

    const articledele = () => {
      if (confirm("삭제하시겠습니까?")) {
        router.replace({
          name: "articledelete",
          params: { crew_article_pk: route.params.crew_article_pk },
        });
      }
    };

    const moveBack = () => {
      router.go(-1);
    };

    return {
      article,
      articlemodify,
      articledele,
      host,
      moveBack,
      yyyyMMdd,
      now_user,
      isUpdtae,
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

#update {
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
  width: 70px;
  overflow: hidden;
  border: 1px black solid;
  right: 20px;
  border-radius: 12px;
  padding: 5px;
  z-index: 10;
  -webkit-animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
  animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

@-webkit-keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}
@keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}

.button {
  border: 0;
  background-color: white;
  padding: 4px;
  cursor: pointer;
}

.contentImg {
  width: 100%;
}

#profile {
  width: 50px;
  height: 50px;
  border-radius: 70%;
  overflow: hidden;
}

.imgProfile {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
