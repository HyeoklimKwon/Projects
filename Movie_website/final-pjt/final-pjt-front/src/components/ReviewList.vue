<template>
  <div class="review-list">
    <h2>리뷰 작성</h2>
    <review-list-form></review-list-form>

    <h2>리뷰 목록</h2>
    <ul class="text-start">
      <review-list-item 
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>        
    </ul>
  </div>
</template>

<script>
  import ReviewListItem from '@/components/ReviewItem.vue'
  import ReviewListForm from '@/components/ReviewForm.vue'
  // import { mapGetters, mapActions } from 'vuex'


  export default {
    name: 'ReviewList',
    components: { ReviewListForm, ReviewListItem },
    props: { reviews: Array },
  }
</script>

<style>
</style>