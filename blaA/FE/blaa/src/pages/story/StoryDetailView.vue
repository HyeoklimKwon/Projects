<template>
<!-- 뒤로, 하트 이모지 추가 -->
  <div v-if="!isError">
    <PopUp v-if="popUpOpen" @close-modal="popUpOpen=false">
        <div class="modal-content">
          <p>정말 삭제하시겠습니까?</p>
          <button class="btn btn-secondary" @click="popUpOpen=false">취소</button> 
          <button class="btn btn=danger" @click="storyDelete">삭제</button>
        </div>
    </PopUp>
    <div>
      <router-link class="btn btn-primary" :to="{name: 'story'}">뒤로</router-link>
      <button class="btn btn-danger ml-3" @click="popUpOpen=true">삭제</button>
    </div>
    <div class="d-flex justify-content-between">
      <h2>{{ story.story_title }}</h2>
      <!-- 좋아요 기능 구현 -->
      <div class="like">
        <span>{{story.like_user_count}}</span>
        <i class="fa fa-solid fa-heart" :class="{activate: isLike, deactivate: !isLike}" 
        @click="likeStory" style="cursor:pointer; maring-left: 5px;"></i>
      </div>
    </div>
    <div class="story-content">
      <img :src="host + story.story_picture" alt="이미지 영역입니다." style="width:100%">
      <span>작성자 : {{ story.user_pk }} </span>
      <span>작성일 :{{ story.created_at }}</span>
    </div>
    <CommentList/>
    <hr>
    <CommentForm/>
  </div>
  <div v-else>
    <h2>오류가 발생하였습니다. 다시 시도해주세요</h2>
  </div>
</template>

<script>
// import axios from 'axios'
import { computed, ref } from 'vue'
import CommentList from '@/components/story/CommentList.vue'
import CommentForm from '@/components/story/CommentForm.vue'
import PopUp from '@/components/story/PopUp.vue'
// import api from '@/api/api'
import { useRouter, useRoute } from 'vue-router'
import { useStore } from 'vuex'

export default {
  components: {
    CommentList,
    CommentForm,
    PopUp
  },
  setup() {
    const host = "http://localhost:8000"
    const store = useStore()
    const story = ref({})
    const isError = ref(false)
    const router = useRouter()
    const route = useRoute()
    const popUpOpen = ref(false)
    const user_pk = store.state.account.userInfo.user_pk
    const isLike = computed(() => {
      if (story.value.like_user) {
        return story.value.like_user.includes(user_pk)
      } else {
        return false
      }  
    })

    // 데이터를 불러오는 함수
    const start = async () => {
      isError.value = false
      await store.dispatch('story/getCurrentStory', route.params.story_pk).then(() => {
        story.value = store.state.story.currentStory
        console.log(story.value)
      }).catch((error) => {
        console.error(error)
        isError.value = true
      })  
    }
    
    start()

    const storyDelete = async () => {
      await store.dispatch('story/deleteCurrentStory', route.params.story_pk)
      router.push({
          name: 'story'
        })
    }

    const likeStory = async () => {
      await store.dispatch('story/likeStory', route.params.story_pk)
    }

    return {
      host,
      story,
      popUpOpen,
      isError,
      storyDelete,
      isLike,
      likeStory
    }
  }
}
</script>

<style scoped>
 .my-modal {
    overflow: hidden;
  }

.activate {
  color: pink;
}

.deactivate {
  color: gray;
}

.like {
  font-size: 24px;
  text-align: center;
}
</style>