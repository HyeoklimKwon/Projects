<template>
  <div>
    <router-link :to="{name: 'review'}">뒤로</router-link><h2>{{store_name}}</h2>
    <!-- 별점  -->
    <div class="star">
      <p>전체 리뷰 평균 ({{person}} 명)</p>
      <span>{{star}} 점</span>
      <div class="star-ratings">
        <div 
          class="star-ratings-fill space-x-2 text-lg"
          :style="{ width: score + '%' }"
        >
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
        <div class="star-ratings-base space-x-2 text-lg">
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
      </div>
      <span>으로 평가했어요!</span>
    </div>
    <br>
    <!-- 버튼식 리뷰 -->
    <div v-for="(value, name) of types.value" :key="name.id">
      <p style="margin: 0;">{{name}}</p>
      <div style="display: flex;">
        <div style="
          background: #6BC098;
          padding: 0;
          position: absolute;
          z-index: 1;
          display: flex;
          overflow: hidden;
          border-radius: 20px;
          height:15px;"

          :style="{width: (value * 64/100) + '%'}"
          >
          
        </div>
        <div style="
          background: #D6D6D6;
          border-radius: 20px;
          height:15px;
          width: 64%
          z-index: 0;
          padding: 0;
          margin-right: 20px;"
          >
        </div>
        <span>{{value}}%</span>
      </div> 
      <br>
      </div>

    <br>
    <!-- 한줄평 -->
    <h3>한줄평</h3>
    <div v-if="review">
      <CommentDetail class="userReview" v-for="userReview in review.value" :key="userReview.review_pk" :review="userReview" :isDetail="false" @update="update"/>
    </div>
    <p v-else>아직 리뷰가 없어요</p>
  </div>
  
  

</template>

<script>
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { computed, onMounted, ref } from 'vue'
import CommentDetail from '@/components/review/CommentDetail.vue'
// import $ from 'jquery'

export default {
  components: {
    CommentDetail
  },
  setup() {
    const route = useRoute()
    const store = useStore()
    const review = ref([])
    const types = ref([])
    const star = ref(0)
    const store_name = route.params.store_name
    const score = ref(0)
    const like = ref(false)
    const user_pk = store.state.account.userInfo.user_pk
    const person = ref(0)

    // 처음 시작될 때 실행
    onMounted(async() => {
      await store.dispatch('review/getReview', route.params.store_pk)
      review.value = computed(() => {return store.state.review.review})
      // 별점, 버튼, 날짜 변환
      star.value = computed(() => {return store.state.review.reviewStar})
      types.value = computed(() => {return store.state.review.reviewBtn})
      score.value = (star.value.value * 20) + 1.5
      person.value = computed(() => {return review.value.value.length})
    })


    return {
      like,
      star,
      types,
      review,
      store_name,
      score,
      user_pk,
      person
    }
  }
}
</script>

<style scoped>
/* 유저 리뷰 css */
.userReview {
  background-color: lightgray;
  border-radius: 20px;
  padding: 5px;
  z-index: 1;
}
/* 별점 css */
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  display: inline-block;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}

/* 하트 css */
.heart { 
  z-index: 10;
  height: 25px;
  width: 25px;
}
.activate {
  background-color: red;
}

.deactivate {
  background-color: #aaa9a9;
}
</style>