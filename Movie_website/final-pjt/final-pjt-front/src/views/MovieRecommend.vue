<template>
  <div>
    <br>
    <h1 class="text-black fw-bolder">영화 추천</h1>
    <br>
    <div class="container">
      <div class="row">
        <div class="col-2" v-for="movie in recommend.results" :key="movie.id">
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

export default {
  name: 'MovieRecommend',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['recommend'])
  },
  methods: {
    ...mapActions(['fetchRecommend']),
  },
  created() {
    this.fetchRecommend(this.moviePk)
  },
}
</script>

<style>

</style>