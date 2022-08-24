<template>
  <div><p>삭제처리중...</p></div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();

    const dele = async () => {
      await store.dispatch("crew/deleteArticle", {
        crew_article_pk: route.params.crew_article_pk,
        crew_pk: route.params.crew_pk,
      });
    };

    dele();
  },
};
</script>

<style></style>
