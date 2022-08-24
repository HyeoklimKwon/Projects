<template>
  <div style="margin-bottom: 8px; font-weight: 700;">댓글 : {{ comments.length }}</div>
  <ul v-if="comments.length" style="padding: 0;">
    <CommentListItem v-for="(comment, i) in comments" :key="i" :comment="comment" />
  </ul>
  <p v-else>댓글이 아직 없어요!</p>
  <comment-form></comment-form>
</template>

<script>
import { onMounted } from "@vue/runtime-core";
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { ref } from "vue";
import CommentListItem from "@/components/crew/article/Comment/CommentListItem.vue";
import CommentForm from "@/components/crew/article/Comment/CommentForm.vue";

export default {
  components: {
    CommentListItem,
    CommentForm,
  },
  setup() {
    const store = useStore();
    const route = useRoute();
    const comments = ref([]);

    onMounted(async () => {
      console.log(route.params.crew_article_pk);
      await store.dispatch("crew/getComment", route.params.crew_article_pk).then(() => {
        comments.value = store.state.crew.comments;
      });
    });

    return {
      comments,
    };
  },
};
</script>

<style scoped>
ul {
  list-style: none;
}
</style>
