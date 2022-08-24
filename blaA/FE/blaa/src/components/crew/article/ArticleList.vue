<template>
  <div v-if="articles.length < 1">
    <div class="board" style="text-align: center">
      <span>작성된 게시글이 없어요!</span>
    </div>
  </div>
  <div v-else>
    <article-list-item v-for="(article, i) in articles" :key="i" v-bind="article" :isMember="isMember" />
  </div>
</template>

<script>
import ArticleListItem from "@/components/crew/article/ArticleListItem.vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { onMounted, ref } from "vue";
export default {
  components: {
    ArticleListItem,
  },
  props: {
    isMember: Boolean,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();
    const articles = ref([]);

    onMounted(async () => {
      await store.dispatch("crew/getCrewArticle", route.params.crew_pk);
      articles.value = store.state.crew.articles;
    });

    return {
      articles,
    };
  },
};
</script>

<style scoped>
.board {
  padding: 10px;
  margin: 10px;
  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
}
</style>
