<template>
  <div id="movielist">
    <carousel :autoplay="true" :nav="true" :dots="true" class="marginTop50">
      <img src="../assets/header1.jpg">
      <img src="../assets/header2.jpg">
      <img src="../assets/header3.jpg">
    </carousel>
    <br>
    <h1 class="text-black fw-bolder">영화 검색</h1>
    <br>
    <div class="container-fluid">
      <form class="d-flex">
        <input class="form-control mx-5" type="search" placeholder="영화 제목을 입력해주세요." aria-label="Search" v-model="SearchValue">
        <router-link 
              :to="{ name: 'search', params: {value: SearchValue} }">
          <button class="btn btn-outline-success mx-2" type="submit" id="inputbutton">Search</button>
        </router-link>
      </form>
    </div>
    <br>
    <br>
    <h1 class="text-black fw-bolder">전체 영화 목록</h1>
    <br>

    <div class="container">
      <div class="row">
        <div class="col-2" v-for="movie in movies" :key="movie.pk">
          <div class="card h-100">
            <router-link 
              :to="{ name: 'movie', params: {moviePk: movie.id} }">
              <img :src="`https://image.tmdb.org/t/p/w185/${movie.poster_path}`" class="card-img-top">
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import carousel from 'vue-owl-carousel'

  export default {
    name: 'movieList',
    components: { carousel },
    data(){
      return{
        SearchValue: '',
      }
    },
    
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies']),
      
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style>
#inputbutton {
  height: 2.5rem;
}
#movielist{
  background-color: rgb(167, 141, 141);
}
</style>
