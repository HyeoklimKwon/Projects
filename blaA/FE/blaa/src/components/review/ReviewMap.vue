<template>
  <div class="my-modal">
    <div class="overlay">
      <div class="modal-card" style="opacity: 1">
        <div>
          <span style="font-weight: 700; font-size: 20px">장소를 검색하세요</span>
          <span @click="$emit('close-modal')" style="cursor: pointer; float: right; font-size: 16px">닫기</span>
        </div>
        <span style="font-size: 12px">결과가 없는 가게는 주소로 추가할 수 있어요.</span>
        <hr />
        <div class="storeSearch">
          <input class="storeInput" type="text" v-model="searchWord" @keypress.enter="firstSearchStore" />
          <input type="checkbox" v-model="isStore" id="store" @click="switchIsStore" style="display: none" /><label
            id="addStore"
            for="store"
            :class="{ isStore: isStore, isNotStore: !isStore }"
            >추가</label
          >
        </div>
        <div v-if="searchList.length" style="margin-top: 10px" class="modal-content">
          <ReviewMapList :isStore="isStore" v-for="searchChild in searchList" :key="searchChild.id" :searchChild="searchChild" @select-store="selectStore" />
          <PaginationBar :currentPage="currentPage" :numberOfPages="numberOfPages" :idx="idx" @click="searchStore" />
        </div>
        <p style="margin-top: 10px" v-else>검색결과가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from "vue";
import { useStore } from "vuex";
import axios from "axios";
import myaxios from "@/api/axios";
import api from "@/api/api";
import ReviewMapList from "@/components/review/ReviewMapList.vue";
import PaginationBar from "@/components/review/PaginationBar.vue";

export default {
  components: {
    ReviewMapList,
    PaginationBar,
  },
  setup(props, { emit }) {
    const isStore = ref(false);
    const store = useStore();
    const searchList = ref([]);
    const searchWord = ref("");
    const currentPage = ref(1);
    const totalCount = ref(0);
    const searchError = ref(false);

    // 추가 버튼을 클릭할 떄
    const switchIsStore = async () => {
      isStore.value = !isStore.value;
      firstSearchStore();
    };

    const firstSearchStore = async () => {
      if (!searchWord.value) {
        searchError.value = true;
      } else {
        if (!isStore.value) {
          try {
            const res = await myaxios.get(api.review.store(), {
              params: {
                search: searchWord.value,
                page: 1,
              },
            });
            isStore.value = res.data.count ? false : true;
            searchList.value = res.data.results;
            totalCount.value = res.data.count;
            // 처음 찾았을 떄 없으면
            if (isStore.value) {
              serachNewStore(1);
            }
          } catch (error) {
            console.error(error);
          }
        } else {
          serachNewStore(1);
        }
      }
    };

    const serachNewStore = async (page = currentPage.value) => {
      try {
        const res = await axios.get(`https://dapi.kakao.com/v2/local/search/keyword.json?query=${searchWord.value}`, {
          headers: {
            Authorization: `KakaoAK ${process.env.VUE_APP_KAKAO_REST_API}`,
          },
          params: {
            page: currentPage.value,
            size: 5,
          },
        });
        console.log(res.data);
        searchList.value = res.data.documents;
        totalCount.value = res.data.meta.pageable_count;
        currentPage.value = page;
      } catch (error) {
        console.error(error);
      }
    };

    // 가게를 검색하는 함수
    const searchStore = async (page = currentPage.value) => {
      currentPage.value = page;
      if (!isStore.value) {
        try {
          const res = await axios.get(api.review.store(), {
            headers: {
              Authorization: `Bearer ${store.state.review.Token}`,
            },
            params: {
              search: searchWord.value,
              page: currentPage.value,
            },
          });
          isStore.value = res.data.count ? true : false;
          searchList.value = res.data.results;
          totalCount.value = res.data.count;
        } catch (error) {
          console.error(error);
        }
      } else {
        serachNewStore(page);
      }
    };

    // 페이지 수 계산
    const numberOfPages = computed(() => {
      return Math.ceil(totalCount.value / 5);
    });

    // 5개씩 쪼개서 페이지네이션을 하기위한 인덱스
    const idx = computed(() => {
      return Math.floor((currentPage.value - 1) / 5);
    });

    // 상점 선택 결과 전송
    const selectStore = (data) => {
      data = {
        ...data,
        // 상점 생성 유무를 전송 false x / true 생성해야됨
        isStore: isStore.value,
      };
      emit("select-store", data);
    };

    return {
      isStore,
      searchWord,
      searchList,
      searchStore,
      currentPage,
      numberOfPages,
      selectStore,
      firstSearchStore,
      switchIsStore,
      idx,
    };
  },
};
</script>

<style scoped>
.my-modal,
.overlay {
  width: 100%;
  height: 100%;
  /* 상단에 고정되어 있어야 하므로 */
  position: fixed;
  /* top: 0px;
    left: 0px; */

  /* 구분선이 계속 떠서, 이거 추가함! */
  z-index: 100;
}
/* 모달이 떳을 떄 뒤에 배경화면을 안보이게 */
.overlay {
  /* opacity: 0.5; */
  background-color: rgba(255, 255, 255, 0.5);
}

#store {
  height: 20px;
}

.modal-card {
  overflow-y: initial !important;
  position: relative;
  max-width: 80%;
  margin: auto;
  padding: 20px;
  margin-bottom: 60px;
  background-color: #f8f9fe;
  border-radius: 20px;
  min-height: 635px;
  z-index: -1;
}

.modal-content {
  height: 600px;
  overflow-y: auto;
}

.storeSearch {
  display: grid;
  grid-template-columns: 70% 30%;
}

.storeInput {
  padding: 6px 10px;
  border-radius: 12px;
}

#addStore {
  border-radius: 16px;
  padding: 6px 10px;
  margin-left: 10px;
  font-weight: 700;
  max-width: 90px;
  text-align: center;
  justify-content: center;
}

.isStore {
  background-color: #498d6d;
  color: white;
}

.isNotStore {
  background-color: #c9c9c9;
}
</style>
