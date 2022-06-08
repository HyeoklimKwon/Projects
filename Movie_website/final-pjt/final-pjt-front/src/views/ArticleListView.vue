<template>
  <div class="backgr">
    <h1 style=" margin-top: 100px">자유게시판</h1>
    <table class="table">
      <thead>
      <tr>
          <th>번호</th>
          <th>제목</th>
          <th>작성자</th>
          <th>댓글수</th>
          <th>추천수</th>
      </tr>
      </thead>
      <tbody >
      <tr v-for="article in articles" :key="article.pk">
        <td>{{ article.pk }}</td>
        <td><router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }} 
        </router-link></td>
        <td>
          <router-link 
          :to="{ name: 'profile', params: {username: article.user.username} }">
          {{ article.user.username }} 
        </router-link>
        
        </td>
        <td>
          <i class="fa-solid fa-comment"></i>
          {{ article.comment_count }}
        </td>
        <td>
          <i class="fa-solid fa-thumbs-up"></i>
          {{ article.like_count }}
        </td>
      </tr>     
        
      </tbody>
    </table>    
    
    <router-link :to="{ name: 'articleNew' }">
            <b-button variant="danger"><i class="fa-solid fa-pencil"></i></b-button>
        </router-link>

    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles']),
      
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
.background5{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/communitybackground.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}</style>