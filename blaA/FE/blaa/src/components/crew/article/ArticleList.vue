<template>
  <div>
    <h2>글 목록</h2>
    <table>
      <article-list-item v-for="(article, i) in articles.results" :key="i" v-bind="article" />
    </table>
    <button @click="moveRegist">글쓰기</button>
  </div>
</template>

<script>
import ArticleListItem from "@/components/crew/article/ArticleListItem.vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";
export default {
  components: {
    ArticleListItem,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();
    const articles = ref([]);
    // const Articles = reactive({
    //   crew_article_pk: "",
    //   images: [],
    //   created_at: "",
    //   updated_at: "",
    //   crew_title: "",
    //   crew_content: "",
    //   crew_private: "",
    //   crew_pin: "",
    //   crew: "",
    // });

    const getArticles = async () => {
      await store.dispatch("crew/getCrewArticle", route.params.crew_pk);
      articles.value = store.state.crew.articles;
    };

    const moveRegist = () => {
      router.push({ name: "articleregist" });
    };
    getArticles();
    return {
      articles,
      getArticles,
      moveRegist,
    };
  },
};
</script>

<style scoped></style>
