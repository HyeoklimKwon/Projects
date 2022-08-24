<template>
  <input type="text" v-model="comment" placeholder="댓글을 입력해주세요">
  <button @click="CommentCreate">등록</button>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  setup() {
    const comment = ref('')
    const store = useStore()
    const route = useRoute()

    const CommentCreate = () => {
      const content = {
        story_comment: comment.value,
        story_pk: route.params.story_pk
      }
      store.dispatch('story/createComment', content)
      comment.value = ''
    }

    return {
      CommentCreate,
      comment
    }
  }
}
</script>

<style>

</style>