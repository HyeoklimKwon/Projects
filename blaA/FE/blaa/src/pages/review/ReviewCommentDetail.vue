<template>
  <div class="row" id="top_box">
    <div class="col-2" id="top_box_text" @click="moveToPrevious"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-8" id="top_box_text">{{ review.value.user.nickname }}님의 한줄평</h5>
    <div class="col-2" id="top_box_text"></div>
  </div>
  <div v-if="review.value">
    <div class="d-flex justify-content-center main">
      <PopUp v-if="popUpOpen" @close-modal="popUpOpen = false">
        <div class="modal-content">
          <p>정말 삭제하시겠습니까?</p>
          <button class="btn btn-secondary" @click="popUpOpen = false">취소</button>
          <button class="btn btn=danger" @click="deleteReview">삭제</button>
        </div>
      </PopUp>
      <div style="width: 90%">
        <!-- <div class="d-flex justify-content-between align-items-center">
          <span class="material-symbols-outlined" style="color: black; font-size: 36px; cursor: pointer" @click="moveToPrevious">arrow_back</span>
          <h2 style="margin: 0; font-weight: 700">{{ store_name }}</h2>
          <div style="width: 36px"></div>
        </div>
        <div style="background: black; height: 1px; width: 100%; margin: 10px 0"></div>
        <br />
        <p class="nickname">{{ review.value.user.nickname }} 님은 이렇게 평가했어요.</p>
        <br /> -->
        <CommentDetail class="userReview" :review="review.value" :isDetail="true" @update="update" />
        <hr />

        <p id="semi_title_text" style="margin: 0 0 10px 10px">{{ review.value.user.nickname }}님의 총 별점</p>
        <div class="userReviewDetail">
          <div class="star-ratings">
            <div class="star-ratings-fill space-x-2 text-lg" :style="{ width: score + '%' }">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
            <div class="star-ratings-base space-x-2 text-lg"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
          </div>
          <span style="font-weight: 600; font-size: 24px">{{ review.value.star }}.0점</span>
        </div>
        <hr />

        <p id="semi_title_text" style="margin: 0 0 10px 10px">{{ review.value.user.nickname }}님이 긍정적으로 평가하셨어요!</p>
        <div class="userReviewDetail">
          <div class="buttonReview">
            <div v-for="type of check_button" :key="type.id">
              <div class="buttonDetail">{{ type }}</div>
            </div>
          </div>
        </div>

        <div class="udbutton" v-if="review.value.user.nickname == user_name">
          <hr />
          <button class="delete button" @click="popUpOpen = true">삭제</button>
          <!-- <button class="update button" @click="moveToForm">수정</button> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import CommentDetail from "@/components/review/CommentDetail.vue";
import $ from "jquery";
import PopUp from "@/components/story/PopUp.vue";

export default {
  components: {
    CommentDetail,
    PopUp,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();
    const review_pk = route.params.review_pk;
    const store_name = route.params.store_name;
    const score = ref(0);
    const review = ref({});
    const user_name = store.state.account.userInfo.nickname;
    const check_button = ref([]);
    const popUpOpen = ref(false);

    const start = async () => {
      await store.dispatch("review/getDetailReview", review_pk);
      review.value = computed(() => {
        return store.state.review.detailReview;
      });
      const button = ["친절한 사장님", "깨끗한 매장", "좋은 분위기", "교통 접근성", "칼퇴근 가능", "유니폼 제공"];
      button.forEach((ele) => {
        if (review.value.value.button[ele] == 1) {
          check_button.value.push(ele);
        }
      });
      score.value = review.value.value.star * 20 + 1.5;
    };

    start();

    const update = () => {
      review.value = computed(() => {
        return store.state.review.detailReview;
      });
    };

    const moveToPrevious = () => {
      if (window.history.state.back.includes("create") || !window.history.state.back) {
        console.log("상세");
        router.push({
          name: "detailReview",
          params: {
            store_pk: route.params.store_pk,
            store_name: route.params.store_name,
          },
        });
      } else {
        console.log("이전");
        router.go(-1);
      }
    };

    const deleteReview = async () => {
      await store.dispatch("review/deleteReview", review_pk);
      router.push({
        name: "detailReview",
        params: {
          store_name: route.params.store_name,
          store_pk: route.params.store_pk,
        },
      });
    };

    return {
      review,
      moveToPrevious,
      score,
      store_name,
      update,
      deleteReview,
      user_name,
      check_button,
      popUpOpen,
    };
  },
};
</script>

<style scoped>
.main {
  padding-top: 24px;
  padding-bottom: 60px;
}
.nickname {
  font-weight: 800;
  font-size: 24px;
}
/* 유저 리뷰 css */
.userReview {
  background-color: #f8f9fe;
  border-radius: 20px;
  padding: 20px;
  z-index: 1;
}

.userOnelineReview {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 30px;
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
  -webkit-text-stroke-color: #498d6d;
}

.star-ratings span {
  font-size: 30px;
  margin-left: 3px;
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
  -webkit-text-fill-color: #498d6d;
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

  background: #f8f9fe;
  border-radius: 16px;
}

/* 버튼 css */
.buttonReview {
  /* margin-top: 40px; */
  display: grid;
  grid-template-columns: repeat(2, auto);
}

.buttonDetail {
  justify-content: center;
  text-align: center;
  background-color: white;
  color: #498d6d;
  border-radius: 16px;
  padding: 6px 10px;
  margin: 8px 12px;
  font-weight: 600;
}

.udbutton {
  width:90%;
  position: fixed;
  bottom: 70px;
  display: flex;
  justify-content: space-around;
}

.button {
  border: 0;
  width: 100%;
  padding: 10px 0;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 600;
}

.update {
  background-color: #eec95c;
}

.delete {
  background: #c25243;
  color: white;
}
</style>
