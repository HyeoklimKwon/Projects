<template>
  <div id="contain">
    <div class="comment-form">
      <div style="background-color: white">
        <input type="text" v-model="comment" placeholder="댓글을 입력해주세요" :style="{ width: windowWidth.value + 'px' }" />
        <div class="button" @click="CommentCreate">등록</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import $ from "jquery";

export default {
  setup() {
    const comment = ref("");
    const store = useStore();
    const route = useRoute();
    const windowWidth = ref(0);
    const formWidth = ref(0);

    const CommentCreate = () => {
      const content = {
        story_comment: comment.value,
        story_pk: route.params.story_pk,
      };
      store.dispatch("story/createComment", content);
      comment.value = "";
    };

    windowWidth.value = computed(() => {
      return $(window).width() - 215;
    });

    formWidth.value = computed(() => {
      return windowWidth.value.value + 64;
    });

    $(window).resize(function () {
      windowWidth.value = computed(() => {
        return $(window).width() - 215;
      });
      formWidth.value = computed(() => {
        return windowWidth.value.value + 64;
      });
    });

    return {
      CommentCreate,
      comment,
      windowWidth,
      formWidth,
    };
  },
};
</script>

<style scoped>
#contain {
  position: fixed;
  padding-bottom: 6px;
  width: 100%;
  background-color: white;
  height: 3.3rem;
  bottom: 65px;
  left: 0;
  border-top: 0.5px solid black;
}

input {
  margin-top: 0.75rem;
  border: none;
  /* margin-left: 2rem; */
}

.comment-form {
  /* background-color: white; */
  position: fixed;
  left: 5%;
  width: 87%;
  margin: 0 12px;
  bottom: 68px;
  height: 3rem;
}

.button {
  line-height: 2.4rem;
  text-align: center;
  position: fixed;
  bottom: 70px;
  right: 3%;
  width: 4rem;
  height: 2.4rem;
  border-radius: 10px;
  background-color: #498d6d;
  color: white;
  font-family: "Pretendard-Regular";
  font-weight: 600;
}
</style>
