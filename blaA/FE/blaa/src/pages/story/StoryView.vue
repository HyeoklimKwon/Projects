<template>
<div>
  <h1>여기는 오출완 페이지입니다!</h1>
  <router-link class="btn btn-primary m-1" style="maring-left:5px" :to="{name: 'createStory'}">+</router-link>
  <button type="button" class="btn btn-primary m-1" data-bs-toggle="modal" data-bs-target="#exampleModal">
    검색
  </button>
  <button class="btn m-1" @click="onCategory" :class="{ activate: isCategory, deactivate: !isCategory}">관심업종</button>
  <button class="btn m-1" @click="onRegion" :class="{ activate: isRegion, deactivate: !isRegion}">근무지</button>
  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body">
          <HashTagForm @search-hash-tag="searchHastTag"/>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
          <button type="button" class="btn btn-primary" @click="searchStoryHashTag">검색</button>
        </div>
      </div>
    </div>
  </div>
  <StoryImageCardList :images="images"/>
</div>
</template>

<script>
import StoryImageCardList from '@/components/story/StoryImageCardList.vue'
import HashTagForm from '@/components/story/HashTagForm.vue'
import { useStore } from 'vuex'
import { onBeforeMount, ref } from 'vue'
// import axios from 'axios'

export default {
  components: {
    StoryImageCardList,
    HashTagForm
  },
  setup() {
    const store = useStore()
    const images = ref(null)
    const isCategory = ref(false)
    const isRegion = ref(false)
    const hashTag = ref([])

    const getPure = async() => {
      await store.dispatch('story/getImages')
      images.value = store.state.story.images 
    }

    // 시작할 떄
    onBeforeMount(() => {
      getPure()
    })

    // 해시태그 검색
    const searchHastTag = (hashTag) => {
      hashTag.value = hashTag
    }

    const searchStoryHashTag = () => {

    }


    const onCategory = async() => {
      isCategory.value = !isCategory.value
      isRegion.value = false
      // 관심업종이 커져있으면 해당 업종 검색
      if (isCategory.value) {
        await store.dispatch('story/getCategory')
        images.value = store.state.story.images
      } else {
        getPure()
      }
    }

    const onRegion = async() => {
      isRegion.value = !isRegion.value
      isCategory.value = false
      // 관심업종이 커져있으면 해당 업종 검색
      if (isRegion.value) {
        await store.dispatch('story/getRegion')
        images.value = store.state.story.images
      } else {
        getPure()
      }
    }

    return {
      images,
      searchHastTag,
      onCategory,
      onRegion,
      isRegion,
      isCategory,
      searchStoryHashTag
    }
  }
}
</script>

<style scoped>
.activate {
  background-color: greenyellow;
}

.deactivate {
  background-color: gray;
}
</style>
