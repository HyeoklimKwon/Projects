<template>
  <form @submit.prevent="onSubmit" class="review-list-form">
    <div class="mx-3 px-3">
      <textarea class="form-control" id="review" v-model="content" rows="3"></textarea>
    </div>
   
    <div>
      <star-rating id=grade :star-size="30" v-model="grade" :border-width="5" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" class="d-flex justify-content-center align-items-center py-3"></star-rating>
      <button class="btn btn-outline-danger mx-3">작성하기</button>
    </div>

     
   


  </form>
  
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewListForm',
  components: {
    StarRating
  },
  data() {
    return {
      content: '',
      grade: 0,
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, content: this.content, grade: this.grade})
      this.content = '' 
    },
  }
}
</script>

<style>
</style>