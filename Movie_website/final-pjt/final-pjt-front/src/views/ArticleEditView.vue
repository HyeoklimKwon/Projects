<template>
  <div class="background5">
    <h1 style="margin-right : 80px; margin-top: 100px ;font-family: 'Nanum Pen Script', cursive; font-size: 50px">수정하기</h1>
    <article-form v-if="isArticle" :article="article" action="update">

    </article-form>
  </div>

</template>

<script>

import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
.background5{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/detailbackground.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}
</style>

