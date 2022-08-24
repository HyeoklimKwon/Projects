<template>
  <div>글 디테일</div>
  {{ $route.params.crew_article_pk }}번 글

  <div>
    <h2>제목 : {{ article.crew_title }}</h2>
    <p>내용 : {{ article.crew_content }}</p>
    <p>작성자: {{ article.user }}</p>
    <template v-for="image in article.images" :key="image"> <img :src="host + image.article_picture" width="200" /> </template><br />
    <!-- <p>{{ article.images.article_picture }}</p> -->
    <button @click="articlemodify">수정</button>
    <button @click="articledele">삭제</button>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const article = ref([]);
    const host = ref("http://localhost:8000");

    const getDetail = async () => {
      await store.dispatch("crew/getArtileDetail", route.params.crew_article_pk);
      article.value = store.state.crew.article;
    };

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

    getDetail();

    return {
      article,
      getDetail,
      articlemodify,
      articledele,
      host,
    };
  },
};
</script>

<style></style>
