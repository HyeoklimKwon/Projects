<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-5 d-flex justify-content-center align-items-center">
            <img :src="`https://image.tmdb.org/t/p/w185/${movie.poster_path}`" id="card-img">
        </div>
        <div class="col-5 d-flex justify-content-center align-items-center">
          <div>
            <h3 class="text-center fw-bolder">{{ movie.title }}</h3>
            <br>
            <p class="text-start">장르: <span v-for="genre in movie.genres" :key="genre.pk">
              {{ genre.name }}
            </span></p>
            <p class="text-start">인기: {{ movie.popularity }}</p>
            <p class="text-start">개봉일: {{ movie.release_date }}</p>
            <p class="text-start">예매율: {{ movie.vote_average }}</p>
            <p class="text-start">예매수: {{ movie.vote_count }}</p>        
            <p class="text-start">줄거리: {{ movie.overview }}</p>
          </div>
        </div>
        <div class="col-2 d-flex justify-content-center align-items-center">
          <router-link 
              :to="{ name: 'MovieRecommend', params: {moviePk: movie.id} }">
              <div id="icon"><font-awesome-icon icon="fa-solid fa-caret-right" size="6x"/></div>
            </router-link>
        </div>
      </div>
    </div>
    <br>
    <br>
    <br>
    <div>
      <review-list :reviews="movie.reviews"></review-list>
    </div>
    <router-link :to="{ name: 'theater' }">
      <b-button variant="success" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Go to Theater</b-button>
    </router-link>
    
    
  </div>
</template>

<script>

  import { mapActions, mapGetters } from 'vuex'
  import ReviewList from '@/components/ReviewList.vue'
  
  export default {
    name: 'MovieDetail',
    components: { ReviewList },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie'])
    },
    methods: {
      ...mapActions(['fetchMovie'])
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
#card-img {
  width: 100%;
  height: 80%;
}
#card {
  display: flex;
  flex-direction: row;
}
</style>
