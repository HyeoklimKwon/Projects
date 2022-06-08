<template>
  <div >  
  <b-card>  
    <b-card-body class="background5">
      <b-card-title><h1 style="font-family: 'Nanum Pen Script', cursive; font-size: 100px">{{ article.title }}</h1></b-card-title>
      <hr>
      <br>      
      <b-card-text>
        <p style="font-family: 'Nanum Pen Script', cursive; font-size: 50px">
      {{ article.content }}
         </p>
      </b-card-text>
    </b-card-body>

    <b-list-group flush>
      
      <b-list-group-item>
        <!-- Article Like UI -->
    
      </b-list-group-item>
      <b-list-group-item>댓글</b-list-group-item>
    </b-list-group>   
    <b-card-footer>
      <!-- Comment UI -->
    <comment-list :comments="article.comments" ></comment-list>
    </b-card-footer>
    <!-- Article Edit/Delete UI -->
    <div style="font-family: 'Nanum Pen Script', cursive; font-size: 25px; margin-bottom: 10px">
      Likeit:
      
      <button
        @click="likeArticle(articlePk)"
      ><i class="fa-solid fa-thumbs-up"></i></button>
      {{ likeCount }}
    </div>
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <b-button variant="success" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Edit</b-button>
      </router-link>
      |
      <b-button variant="danger" @click="deleteArticle(articlePk)" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Delete</b-button>
    </div>

    
  </b-card>
 
    
  
  </div>


  
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
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


.h1{
  font-family: 'Nanum Pen Script', cursive;
}

</style>
