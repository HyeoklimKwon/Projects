<template>
  <div class="background5">
    <h1 style="margin-right : 80px; margin-top: 100px ;font-family: 'Nanum Pen Script', cursive; font-size: 50px">새 글 쓰기 </h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');</style>
