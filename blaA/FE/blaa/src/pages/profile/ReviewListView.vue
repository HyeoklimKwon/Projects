<template>
  <br />
  <h3 v-if="myReview" style="font-weight: bold">내가 쓴 리뷰</h3>
  <h3 v-else style="font-weight: bold">
    <b style="color: #498d6d">{{ userNickname }}</b
    >님의 리뷰
  </h3>
  <hr />

  <div class="container">
    <div v-for="review in reviews" :key="review.review_pk" style="width: 100%">
      <div
        class="d-flex justify-content-around row"
        @click="
          reviewDetail(review.store_pk, review.store_name, review.review_pk)
        "
      >
        <img
          class="col-2"
          style="width: 5rem; height: 3.5rem; border-radius: 50%"
          :src="review.store_image"
        />

        <h5 class="col-5 mt-3 mb-0" style="font-weight: bold">
          <b>{{ review.store_name }}</b>
        </h5>
        <div
          style="padding: 0%; margin-top: 4%"
          class="col-2 material-symbols-outlined"
        >
          arrow_forward_ios
        </div>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref, computed } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const HOST = ref("https://i7b209.p.ssafy.io");
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    const reviewList = store.state.profile.reviewList.results;
    console.log("reviewList : ", reviewList);
    console.log("reviewList length: ", reviewList.length);
    const user_pk = ref(-1);
    for (var i = 0; i < reviewList.length; i++) {
      if (reviewList[i].user_pk == route.params.user_pk) {
        user_pk.value = i;
        console.log("i ; ", user_pk.value);
      }
    }

    const myReview = computed(() => {
      if (store.state.account.userInfo.user_pk == route.params.user_pk) {
        return true;
      }
      return false;
    });

    const userNickname = ref(null);
    axios
      .get(api.profile.myInfo(route.params.user_pk))
      .then((response) => {
        userNickname.value = response.data.nickname;
      })
      .catch((err) => {
        console.log(err);
      });

    const reviews =
      store.state.profile.reviewList.results[user_pk.value].reviews;
    console.log("user_pk : ", user_pk.value);
    console.log("reviewList[user_pk]", reviews);

    const reviewDetail = (store_pk, store_name, review_pk) => {
      router.push({
        name: "detailComment",
        params: {
          store_pk: store_pk,
          store_name: store_name,
          review_pk: review_pk,
        },
      });
    };

    return {
      reviewList,
      myReview,
      userNickname,
      user_pk,
      reviews,
      reviewDetail,
      HOST,
    };
  },
};
</script>

<style>
.material-symbols-outlined {
  font-variation-settings: "FILL" 0, "wght" 400, "GRAD" 0, "opsz" 48;
}
</style>
