<template>
  <h1>여기는 리뷰 페이지입니다!</h1>
  <router-link class="btn btn-primary" :to="{name: 'createReview'}">리뷰 생성</router-link>
  <ReviewSearchBar @search-store="searchStore"/>
  <div v-if="reviews"> 
    <ReviewList v-for="review in reviews" :key="review.store_pk" :review="review"/>
    <PaginationBar :currentPage="currentPage" :numberOfPages="numberOfPages" :idx="idx" @click="getReviews"/>
  </div>
  <p v-else>아직 리뷰가 없어요 ㅠㅠ</p>
  
  
</template>

<script>
import { useStore } from 'vuex'
import { computed, onBeforeMount, ref } from 'vue'
import ReviewList from '@/components/review/ReviewList.vue'
import PaginationBar from '@/components/review/PaginationBar.vue'
import ReviewSearchBar from '@/components/review/ReviewSearchBar.vue'

export default {
  components: {
    ReviewList,
    PaginationBar,
    ReviewSearchBar
  },
  setup() {
    const store = useStore()
    const reviews = ref([])
    const currentPage = ref(1)
    const total = ref(0)
    const searchStoreName = ref('')

    // 데이터를 가져오는 함수
    const getReviews = async(page = currentPage.value) => {
      const data = {
        searchText: searchStoreName.value,
        page: page
      }
      await store.dispatch('review/getReviews', data)
      reviews.value = store.state.review.reviews
      currentPage.value = page
      total.value = store.state.review.total_reviews
    }

    // DOM에 가져오기 전에 데이터 가져오기
    onBeforeMount(async() => {
      await getReviews()
    })

    const numberOfPages = computed(() => {
      return Math.ceil(total.value / 5)
    })

    const idx = computed(() => {
      return parseInt((currentPage.value -1) /5)
    })

    // 필터링 함수
    const searchStore = (searchText) => {
      console.log(searchText)
      searchStoreName.value = searchText
      // 새로 찾을 때 
      currentPage.value = 1
      getReviews()
    }

    return {
      reviews,
      numberOfPages,
      currentPage,
      getReviews,
      idx,
      searchStore
    }
  }
}
</script>

<style></style>
