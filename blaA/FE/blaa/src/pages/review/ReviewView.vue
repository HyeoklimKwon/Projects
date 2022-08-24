<template>
  <div class="row" id="top_box">
    <div class="col-2" id="top_box_text"></div>
    <h5 class="col-8" id="top_box_text">지점별 리뷰</h5>
    <div class="col-2" id="top_box_text"></div>
  </div>
  <PopUp v-if="isModalOpen">
    <div ref="modal">
      <head>
        <meta charset="utf-8" />
        <title>약관동의</title>
        <link rel="stylesheet" href="css/default.css" />
        <link rel="stylesheet" href="css/style.css" />
      </head>
      <body>
        <h2 class="h2">리뷰페이지 이용약관</h2>
        <div class="agree">
          <div tabindex="0">
            <h3>
              <b> 제 1 조 (목적) </b>
            </h3>
            <br />
            이 약관은 blaA(이하 "블라"라 합니다)가 제공하는 리뷰쉐어 서비스.와 관련하여 이용 고객과 "회사"간의 권리, 의무 및 책임사항, 서비스 이용조건 및 절차
            등 기본적인 사항을 규정함을 목적으로 합니다.<br />
            본 약관은 웹, 스마트폰(안드로이드폰, 아이폰 등) 앱 등을 이용하는 전자상거래에 대해서도 그 성질에 반하지 않는 한 준용됩니다. <br />
            <br />
            <br />
            <h3>
              <b>제 2 조 (회원의 의무)</b>
            </h3>
            <br />
            <b> ① 회원은 서비스를 이용할 때 다음 각 호의 행위를 하여서는 아니 됩니다. </b>
            1. 이용신청 또는 변경 시 허위 사실을 기재하거나, 다른 회원의 아이디(ID) 및 비밀번호를 도용, 부정하게 사용하는 행위<br />
            2. 회사의 서비스 정보를 이용하여 얻은 정보를 회사의 사전 승낙 없이 복제 또는 유통시키거나 상업적으로 이용하는 행위<br />
            3. 타인의 명예를 손상시키거나 불이익을 주는 행위 4. 회사의 저작권, 제3자의 저작권 등 기타 권리를 침해하는 행위<br />
            5. 공공질서 및 미풍양속에 위반되는 내용의 정보, 문장, 도형, 음성 등을 타인에게 유포하는 행위<br />
            6. 서비스와 관련된 설비의 오 동작이나 정보 등의 파괴 및 혼란을 유발시키는 컴퓨터 바이러스 감염 자료를 등록 또는 유포하는 행위<br />
            7. 서비스 운영을 고의로 방해하거나 서비스의 안정적 운영을 방해할 수 있는 정보 및 수신자의 명시적인 수신거부의사에 반하여 광고성 정보를 전송하는 행위
            또는 (불법)스팸을 전송하는 행위<br />
            8. 타인으로 가장하는 행위 및 타인과의 관계를 허위로 명시하는 행위<br />
            9. 다른 회원의 개인정보를 수집, 저장, 공개하는 행위<br />
            10. 자기 또는 타인에게 재산상의 이익을 주거나 타인에게 손해를 가할 목적으로 허위의 정보를 유통시키는 행위<br />
            11. 프로젝트 참여시 제공 받은 재화 또는 서비스를 재거래 하는 행위<br />
            12. 1개월 이내 회원 가입 및 서비스 이용 후 다시 해지하는 행위를 2회 이상 반복하는 등 회사 서비스를 부당하게 악용하는 행위<br />
            13. 기타 불법적이거나 부당한 행위<br />
            <b>
              ② 회원은 회사가 제공하는 서비스 이용 시 관계법령, 이 약관의 규정, 이용안내 및 서비스상에 공지한 주의사항, 회사가 통지하는 사항 등을 준수하여야
              하며, 기타 회사의 업무에 방해되는 행위를 하여서는 안됩니다. <br />
              ③ 회원은 회사에서 공식적으로 인정한 경우를 제외하고는 서비스를 이용하여 유료서비스를 판매하거나 기타 영리 활동을 할 수 없으며 또한, 해킹, 광고,
              음란사이트 홍보 또는 이를 통한 영리행위, 상용소프트웨어 불법배포 등을 할 수 없습니다. 이를 위반하여 발생한 모든 결과에 대하여 회사는 책임을 지지
              않으며, 회원은 이와 같은 행위로 인하여 회사에 발생한 손해를 배상하여야 합니다. 또한, 회사는 위와 같은 사실을 발견한 경우 그와 같은 사실을
              행정기관에 신고하거나 수사기관에 고발하는 등 법적조치를 취할 수 있습니다. <br />
              ④ 회원이 서비스 이용을 위하여 고유정보를 등록하는 경우 현재의 사실과 일치하는 완전한 정보를 제공하여야 합니다(이하 본 조에서 그와 같이 등록된
              정보를 “등록정보”라고 합니다). <br />
              ⑤ 회원은 등록정보에 변경사항이 발생할 경우 즉시 갱신하여야 합니다. 회원이 제공한 등록정보 및 갱신한 등록정보가 부정확할 경우, 기타 회원이 본 조
              <br />
              ①항에 명시된 행위를 한 경우에 회사는 이 약관 제6조 에 의해 서비스 이용계약을 해지하거나 회원의 서비스 이용을 제한 또는 중지할 수 있습니다. <br />
            </b>
          </div>
          <p @click="agree = !agree" style="font-size: 13px">
            <input :value="agree" type="checkbox" id="chk1" /><label @click="agree = !agree" for="chk1">이용약관에 동의합니다 </label>
          </p>
          <div v-if="agree" class="d-flex justify-content-center">
            <router-link style="color: black; margin-left: 5px; text-align: center" :to="{ name: 'createReview' }">
              <button class="w-btn w-btn-green" type="button">리뷰 등록하기</button>
            </router-link>
          </div>
        </div>
      </body>
    </div>
  </PopUp>

  <div id="review" class="d-flex justify-content-center">
    <div style="width: 90%">
      <div class="d-flex justify-content-between align-items-center">
        <div style="display: flex; align-items: center; padding-right: 0; font-weight: 600; font-size: 16px; padding-bottom: 10px">
          다양한 지점의 리뷰를 확인해보세요!
        </div>
        <div class="buttons">
          <!-- 클릭하거나 엔터를 치면 -->
          <span class="search-end material-symbols-outlined" v-if="isSearch" @click="searchEnd">cancel</span>
          <div class="search-box">
            <input class="search-txt" type="text" v-model="searchText" @keypress.enter="searchStore" />
            <span class="search-button material-symbols-outlined">search</span>
          </div>
          <div v-if="isSearch"></div>
        </div>
      </div>
      <hr />
      <div v-if="reviews.value">
        <ReviewList v-for="review in reviews.value" :key="review" :review="review" />
        <div class="end-list"></div>
      </div>
      <p v-else>아직 리뷰가 없어요 ㅠㅠ</p>
      <div class="plusbutton"><span class="material-symbols-outlined" style="font-size: 30px; font-weight: bold" @click="isModalOpen = true">add</span></div>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { computed, onBeforeMount, ref } from "vue";
import ReviewList from "@/components/review/ReviewList.vue";
import $ from "jquery";
import PopUp from "@/components/story/PopUp.vue";
import { onClickOutside } from "@vueuse/core";

export default {
  components: {
    ReviewList,
    PopUp,
  },
  setup() {
    const isModalOpen = ref(false);
    const store = useStore();
    const reviews = ref([]);
    const currentPage = ref(1);
    const total = ref(0);
    const isSearch = ref(false);
    const searchText = ref("");
    const agree = ref(false);
    const modal = ref(null);

    onClickOutside(modal, () => ((isModalOpen.value = false), (agree.value = false)));

    // 데이터를 가져오는 함수
    const getReviews = async (page = currentPage.value) => {
      const data = {
        isSearch: isSearch.value,
        searchText: searchText.value,
        page: page,
      };
      console.log(data);
      await store.dispatch("review/getReviews", data);
      reviews.value = computed(() => {
        return store.state.review.reviews;
      });
      total.value = computed(() => {
        return store.state.review.total_reviews;
      });
    };

    // DOM에 가져오기 전에 데이터 가져오기
    onBeforeMount(async () => {
      await getReviews();
    });

    const numberOfPages = computed(() => {
      return Math.ceil(total.value.value / 5);
    });

    // 화면이 길어서 스크롤 바가 안나올 떄
    $(window).ready(function () {
      if ($("#review").height() < $(window).height()) {
        currentPage.value += 1;
        getReviews(currentPage.value);
      }
    });

    // 무한 스크롤 구현
    window.onscroll = function (e) {
      if (numberOfPages.value > currentPage.value) {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
          setTimeout(function () {
            // 실행 시킬 함수 구현
            if (numberOfPages.value > currentPage.value) {
              currentPage.value += 1;
              getReviews(currentPage.value);
            }
          }, 1000);
        }
      }
    };

    // 필터링 함수
    // 새로 찾을 때 검색 정보 데이터를 다시 받아와야함
    const searchStore = () => {
      // 새로 찾을 때
      currentPage.value = 1;
      isSearch.value = true;
      getReviews();
    };

    const searchEnd = async () => {
      isSearch.value = false;
      searchText.value = "";
      currentPage.value = 1;
      await getReviews();
    };

    return {
      reviews,
      numberOfPages,
      currentPage,
      getReviews,
      searchStore,
      searchText,
      isSearch,
      searchEnd,
      isModalOpen,
      agree,
      modal,
    };
  },
};
</script>

<style scoped>
#review {
  margin-top: 24px;
}

.buttons {
  display: flex;
  align-items: center;
}

.search-box {
  height: 40px;
  background-color: #4d8d6d;
  padding: 0 10px;
  border-radius: 40px;
  margin-bottom: 5px;
}

.search-button {
  color: #ededed;
  float: right;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #4d8d6d;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-txt {
  float: right;
  padding: 0;
  background: none;
  border: none;
  outline: none;
  color: white;
  font-size: 15px;
  line-height: 40px;
  width: 0;
  transition: 0.5s;
}

.search-end {
  float: right;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  margin: auto 5px;
  cursor: pointer;
}

/* 마우스를 위에 올렸을 때 늘어남 */
.search-box:hover {
  width: 100%;
}

.search-box:hover > .search-txt {
  width: 77%;
}

.search-box:hover > .search-btn {
  background: #464e54;
}

.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modalk {
  background: white;
  padding: 50px 100px;
  border-radius: 5px;
  box-shadow: 0px 10px 5px 2px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 20px;
  margin-right: 20px;
  margin-left: 20px;
}

.w-btn-green {
  background-color: #77af9c;
  color: #d7fff1;
}

.plusbutton {
  position: fixed;
  z-index: 10;
  bottom: 80px;
  right: 20px;
  width: 50px;
  height: 50px;
  background-color: #eec95c;
  color: black;
  border-radius: 50%;
  padding: 10px;
}
</style>
