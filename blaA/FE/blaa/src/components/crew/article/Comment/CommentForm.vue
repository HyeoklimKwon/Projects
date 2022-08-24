<template>
<div id="contain">
  <div class="comment-form">
    <input type="text" v-model="comment" placeholder="댓글을 입력해주세요" />
    <button @click="CommentCreate">등록</button>
  </div>
</div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";

export default {
  setup() {
    const comment = ref("");
    const store = useStore();
    const route = useRoute();

    const CommentCreate = () => {
      store.dispatch("crew/createComment", {
        comment_content: comment.value,
        crew_article_pk: route.params.crew_article_pk,
      });
      comment.value = "";
    };

    return {
      CommentCreate,
      comment,
    };
  },
};
</script>

<style scoped>
#contain {
  position:fixed;
  padding-bottom: 6px;
  width: 100%;
  background-color: white;
  height: 3.3rem;
  bottom: 65px;
  left: 0;
  border-top: 1px solid black;
  border-bottom: 1px solid black;
}

input {
  margin-top: 0.75rem;
  border:none;
  margin-left: 2rem;
}

.comment-form {
  /* background-color: white; */
  position:fixed;
  left: 5%;
  width: 87%;
  margin: 0 12px;
  bottom: 68px;
  height: 3rem;
}

button {
  position: fixed;
  bottom: 73px;
  right: 8%;
  width: 4rem;
  height: 2.4rem;
  border-radius: 10px;
  background-color: #D9D9D9;
  border-color: #D9D9D9;
}

</style>
