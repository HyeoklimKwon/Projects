<template>
  <div v-if="articles.length > 0">
    <div v-for="(article, i) in articleFilter" :key="i">
      <div class="card-view" @click="moveToArticle(article.crew_article_pk)">
        <div class="oneline">
          <p class="card_text">{{ article.crew_title }}</p>
          <div class="card_text" style="text-align: end">|</div>
          <div class="card_text2" style="margin-right: 10px">{{ article.nickname }}</div>
        </div>
      </div>
    </div>
  </div>
  <div v-else></div>
</template>

<script>
import { onMounted, ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();
    const articles = ref([]);

    const getArticle = async () => {
      await store.dispatch("crew/getCrewArticle", route.params.crew_pk);
      articles.value = store.state.crew.articles;
    };

    const articleFilter = computed(() => {
      if (articles.value.length > 0) {
        return articles.value.filter((item) => {
          return item.crew_pin == true;
        });
      } else {
        return 0;
      }
    });

    getArticle();

    const moveToArticle = (crew_article_pk) => {
      router.push({ name: "articledetail", params: { crew_article_pk: crew_article_pk } });
    };

    return {
      articleFilter,
      articles,
      moveToArticle,
    };
  },
};
</script>

<style scoped>
.card-view {
  width: 90%;
  height: 50px;
  margin: auto;

  margin-bottom: 5px;

  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
  /* border-radius: 20px; */
}

.card_text {
  font-weight: 600;
  padding: 5px;
  line-height: 40px;
  margin-left: 10px;
}

.oneline {
  display: grid;
  grid-template-columns: 50% 20% 30%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.card_text2 {
  font-family: "Pretendard-ExtraLight";
  /* font-weight: 600; */
  padding: 5px;
  line-height: 40px;
}
</style>
