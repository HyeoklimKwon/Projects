<template>
  <!-- 가게 주소 -->
  <ReviewMap v-if="isModalOpen" @close-modal="isModalOpen=false" @select-store="selectStore"/>
  <div>
    <router-link :to="{name: 'review'}">뒤로</router-link>
    <button @click="sumbitReview">제출완료</button>
  </div>
  <h1>리뷰 작성 폼</h1>
  <div>
    <p class="form-input">가게명 : {{storeName}} <button class="btn btn-primary" @click="isModalOpen=true">검색</button></p>
    <p class="form-input">가게주소 : {{storeAddress}}</p>
    <p v-if="storeError" class="error">가게를 검색해주세요</p>
  </div>
  <div v-if="isStore">
    <label for="store_picture">가게 사진 등록</label>
    <input class="store_picture" id="store_picture" type="file" @change="previewFile"/><br />
    <img class="img_test" src="" height="200" alt="이미지 미리보기..." />
  </div>
  <!-- 별점 -->
  <span>별점 : </span>
  <form id="myform" class="mb-3" @click="checkStar">
    <fieldset>
      <input type="radio" name="reviewStar" value="5" id="rate1"><label for="rate1">★</label>
      <input type="radio" name="reviewStar" value="4" id="rate2"><label for="rate2">★</label>
      <input type="radio" name="reviewStar" value="3" id="rate3"><label for="rate3">★</label>
      <input type="radio" name="reviewStar" value="2" id="rate4"><label for="rate4">★</label>
      <input type="radio" name="reviewStar" value="1" id="rate5"><label for="rate5">★</label>
    </fieldset>
  </form>
  <span> {{star}}점 </span>
  <p v-if="starError" class="error">별점을 입력해주세요</p>
  <hr>
  <!-- 버튼식 -->
  <form @click="checkBtn">
    <label for="kind" class="btn"><input type="checkbox" name="reviewBtn" vlaue="1" id="kind" class="checkList" >친절한 사장님</label>
    <label for="clean" class="btn"><input type="checkbox" name="reviewBtn" value="2" id="clean" class="checkList">깨끗한 매장</label>
    <label for="short" class="btn"><input type="checkbox" name="reviewBtn" value="3" id="short" class="checkList">교통 접근성</label>
    <label for="good" class="btn"><input type="checkbox" name="reviewBtn" value="4" id="good" class="checkList">좋은 분위기</label>
    <label for="workblance" class="btn"><input type="checkbox" name="reviewBtn" value="5" id="workblance" class="checkList">칼퇴근 가능</label>
    <label for="uniform" class="btn"><input type="checkbox" name="reviewBtn" value="6" id="uniform" class="checkList">유니폼 제공</label>
  </form>

  <!-- 한줄평 -->
  <div class="oneReview">
    <p>한줄평</p>
    <input type="text" class="form-input" v-model="oneReview">
    <p v-if="oneReviewError" class="error">한줄평을 입력해주세요</p>
  </div>
</template>

<script>
import ReviewMap from '@/components/review/ReviewMap.vue'
import { onMounted, ref, onBeforeMount, watch } from 'vue'
import $ from 'jquery'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  components: {
    ReviewMap,
  },
  setup() {
    const store = useStore()
    const router = useRouter()
    const storeName = ref('')
    const storeAddress = ref('')
    const storeError = ref(false)
    // 6개의 버튼으로 이루어짐
    const storeButton = ref([0,0,0,0,0,0])
    const oneReview = ref('')
    const oneReviewError = ref(false)
    const isModalOpen = ref(false)
    const star = ref(0)
    const starError = ref(false)
    const isStore = ref(true)
    const store_pk = ref(0)
    const store_picture = ref(null)
    const image_url = ref('')

    onBeforeMount(() => {
      storeButton.value = [0,0,0,0,0,0]
    })

    // 상점 선택하기
    const selectStore = (data) => {
      store_pk.value = data.store_pk
      isStore.value = data.isStore
      console.log(isStore.value)
      storeName.value = data.name
      storeAddress.value = data.region
      isModalOpen.value = false
    }

    // 사진 등록하기
    const previewFile = (e) => {
      const preview = document.querySelector('.img_test')
      if (e.target.files[0]) {
        store_picture.value = e.target.files[0]
        const reader = new FileReader();

        // 파일명을 가져와서 소문자로 변환
        let fileName = store_picture.value.name.substring(
          store_picture.value.name.lastIndexOf(".") + 1
        )
        fileName = fileName.toLowerCase()

        // 파일 형식과 3MB의 파일크기 확인
        if (
          ["jpeg", "png", "gif", "bmp"].includes(fileName) && store_picture.value.size <= 25165824
        ) {
          reader.onload = e => {
            preview.src = e.target.result
            image_url.value = e.target.result
          }
          reader.readAsDataURL(store_picture.value)
        } else if (store_picture.value.size <= 25165824) {
          preview.src = null
        } else {
          alert('파일을 다시 선택해 주세요')
          store_picture.value = null
          preview.src = null
        }
      // 파일을 선택하지 않았을 떄
      } else {
        store_picture.value = null
        preview.src = null
      }
    }

    // 별점 가져오기
    const checkStar = () => {
      star.value = $('input[name=reviewStar]:checked').val()
    }

    // 값을 가져와야됨.. 어케 가져오지?
    const checkBtn = () => {
      $('input:checkbox[name="reviewBtn"]').each(function(i) {
        if ($(this).is(':checked') == true) {
          $(this).parent().addClass("selected")
          // 값 변경
          if (storeButton.value[i] == 0) {
            storeButton.value[i] = i + 1
          }
        } else {
          $(this).parent().removeClass("selected")
          if (storeButton.value[i] == i+1) {
            storeButton.value[i] = 0
          }
        }
      })
    }

    const sumbitReview = async() => {
      if ( storeName.value && storeAddress.value && star.value && oneReview.value ){
        // Array => [1,4,6] 선택한 인자만 넘어감
        const buttonType = []
        for (let idx = 0; idx < 6; idx++) {
          if (storeButton.value[idx]) {
            buttonType.push(String(idx+1))
          }
        }
        // 이미지 전달
        const form = new FormData()

        form.append('image', store_picture.value)
        form.append('name', storeName.value)
        form.append('region', storeAddress.value)

        const data = {
          form: form,
          // 값을 생성하는지 아닌지 여부를 확인하기위해서
          isStore: isStore.value,
          store_pk: store_pk.value,
          name: storeName.value,
          region: storeAddress.value,
          star: Number(star.value),
          oneline_review: oneReview.value,
          type: buttonType
        }
        await store.dispatch('review/makeReviews', data).then(
          router.push({
            name: 'review'
          })
        )
      } else {
        // 에러 발생시 에러 문구 출력
        oneReviewError.value = oneReview.value == '' ? true : false
        storeError.value = storeName.value == '' ? true : false
        starError.value = star.value == 0 ? true : false 
      }
    }

    return {
      isModalOpen,
      selectStore,
      storeName,
      storeAddress,
      checkStar,
      star,
      checkBtn,
      oneReview,
      sumbitReview,
      starError,
      storeError,
      oneReviewError,
      previewFile,
      isStore
    }
  }
}
</script>

<style scoped>
#myform fieldset{
    display: inline-block;
    direction: rtl;
    border:0;
}
#myform fieldset legend{
    text-align: right;
}
#myform > input{
    cursor: pointer;
    width:10px;
    height: 10px;
}
#myform input[type=radio]{
    display: none;
}
input[type=checkbox]{
  display: none;
}
.error {
  color: red;
}
.selected {
  background-color:greenyellow;
}

/* 노란색이안먹어 */
#myform label:hover{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}
#myform label:hover ~ label{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}
#myform input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}
</style>