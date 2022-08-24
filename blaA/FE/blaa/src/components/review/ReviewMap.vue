<template>
 <div class="my-modal">
    <div class="overlay">
      <div class="modal-card" style="opacity: 1">
        <div>
          <p>장소를 검색하세요 <span  @click="$emit('close-modal')" style="cursor:pointer"> 닫기</span></p>
          <input type="text" v-model="searchWord" @keypress.enter="firstSearchStore">
          <input type="checkbox" v-model="isStore" id="store" @click="switchIsStore"><label for="store">가게추가하기</label>
        </div>
        <div v-if="searchList.length">
          <ReviewMapList :isStore="isStore" v-for="searchChild in searchList" :key="searchChild.id" :searchChild="searchChild" @select-store="selectStore"/>
          <PaginationBar :currentPage="currentPage" :numberOfPages="numberOfPages" :idx="idx" @click="searchStore"/>
        </div>
        <p v-else>검색결과가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'
import api from '@/api/api'
import ReviewMapList from '@/components/review/ReviewMapList.vue'
import PaginationBar from '@/components/review/PaginationBar.vue'

export default {
  components: {
    ReviewMapList,
    PaginationBar
  },
  setup(props, {emit}) {
    const isStore = ref(false)
    const store = useStore()
    const searchList = ref([])
    const searchWord = ref('')
    const currentPage = ref(1)
    const totalCount = ref(0)
    const searchError = ref(false)

    // 추가 버튼을 클릭할 떄
    const switchIsStore = async() => {
      isStore.value = !isStore.value
      firstSearchStore()
    }

    const firstSearchStore = async() => {
      if (!searchWord.value) {
        searchError.value = true
      } else {
        if (!isStore.value) {
          try {
            const res = await axios.get(api.review.store(), {
              headers: {
                Authorization: `Bearer ${store.state.review.Token}` 
              },
              params: {
                search: searchWord.value,
                page: 1
              }
            })
            isStore.value = res.data.count ? false : true
            searchList.value = res.data.results
            totalCount.value = res.data.count
            // 처음 찾았을 떄 없으면
            if (isStore.value) {
              serachNewStore(1)
            }
          } catch (error) {
              console.error(error)
          }
        } else {
          serachNewStore(1)
        }
      }
    }

    const serachNewStore = async(page = currentPage.value) => {
      try {
          const res = await axios.get(`https://dapi.kakao.com/v2/local/search/keyword.json?query=${searchWord.value}`, {
            headers: {
              Authorization: `KakaoAK 8f46e3774c965e5aefdfc2bb2de1af41`
            },
            params: {
              page: currentPage.value,
              size: 5
            }
          })
          searchList.value = res.data.documents
          totalCount.value = res.data.meta.pageable_count
          currentPage.value = page
        } catch(error) {
          console.error(error)
        }
    }

    
    // 가게를 검색하는 함수
    const searchStore = async(page = currentPage.value) => {
      if (!isStore.value) {
        try {
          const res = await axios.get(api.review.store(), {
            headers: {
              Authorization: `Bearer ${store.state.review.Token}` 
            },
            params: {
              search: searchWord.value,
              page: currentPage.value
            }
          })
          isStore.value = res.data.count ? true : false
          searchList.value = res.data.results
          totalCount.value = res.data.count
        } catch (error) {
            console.error(error)
        }
      } else {
        serachNewStore(page)
      }
    }
      
    // 페이지 수 계산
    const numberOfPages = computed(() => {
      return Math.ceil(totalCount.value / 5)
    })

    // 5개씩 쪼개서 페이지네이션을 하기위한 인덱스
    const idx = computed(() => {
      return Math.floor((currentPage.value -1)/5)
    })

    // 상점 선택 결과 전송
    const selectStore = (data) => {
      data = {
        ...data,
        // 상점 생성 유무를 전송 false x / true 생성해야됨
        isStore: isStore.value
      }
      emit('select-store', data)
    }

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
      idx
    }
  }
}
</script>

<style scoped>
.my-modal, .overlay {
    width: 100%;
    height: 100%;
    /* 상단에 고정되어 있어야 하므로 */
    position: fixed;
    /* top: 0px;
    left: 0px; */
  }
  /* 모달이 떳을 떄 뒤에 배경화면을 안보이게 */
  .overlay {
    /* opacity: 0.5; */
    background-color:rgba(255,255,255,0.5);
  }

  .modal-card {
    position: relative;
    max-width: 80%;
    margin:auto;
    margin-top: 30px;
    padding: 20px;
    background-color: white;
    min-height: 300px;
    z-index:10;
  }
</style>