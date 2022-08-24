<template>
  <span style="cursor:pointer" @click="moveToPrevious">X</span> <h3>{{store_name}}</h3>
      <CommentDetail class="userReview" :review="review.value" :isDetail="true"/>
    <br>
    <div>
      <p>{{review.value.user.nickname}} 님은이렇게 평가했어요.</p>
    </div>
    <br>
    <div class="userReviewDetail">
      <div>
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
        <span>{{review.value.star}} 점</span>
      </div>
      <div v-for="(value, name) of review.value.button" :key="name.id">
        <div v-if="value == 1" class="buttonReview" >{{name}}</div>
      </div>
    </div>
</template>

<script>
import { onBeforeMount, ref, computed } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import CommentDetail from '@/components/review/CommentDetail.vue'

export default {
  components: {
    CommentDetail
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const store_pk = route.params.store_pk
    const review_pk = route.params.review_pk
    const store_name = route.params.store_name
    const score = ref(0)
    const review = ref([])
    const user_pk = store.state.account.userInfo.user_pk

    onBeforeMount(async() => {
      await store.dispatch('review/getDetailReview', review_pk)
      review.value = computed(() => {return store.state.review.detailReview})
      score.value = (review.value.value.star * 20) + 1.5
    })

    const update = () => {
      review.value = computed(() => {return store.state.review.detailReview})
    }


    const moveToPrevious =() => {
      console.log('이동')
      router.push({
        name: 'detailReview',
        params: {
          store_pk: store_pk,
          store_name: store_name
        }
      })
    }

    return {
      review,
      moveToPrevious,
      score,
      store_name,
      user_pk,
      update
    } 
  }
}
</script>

<style scoped>
/* 유저 리뷰 css */
.userReview {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px;
  gap: 16px;

  background: #F8F9FE;
  border-radius: 16px;
}

.userOnelineReview {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.user_info {
  flex-direction: row;
  justify-content: space-between;
}
/* 별점 css */
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  display: inline-block;
  unicode-bidi: bidi-override;
  width: max-content;
  margin-right: 20px;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: greenyellow;
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
  -webkit-text-fill-color: greenyellow;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}

/* 하트 css */
.activate {
  background-color: red;
}

.deactivate {
  background-color: #aaa9a9;
}

.userReviewDetail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 16px;

  background: #F8F9FE;
  border-radius: 16px;
}
/* 버튼 css */
.buttonReview {
  
}
</style>