<template>
  <div class="row" id="top_box">
    <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="goBack"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-6" id="top_box_text">오출완</h5>
    <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px"></div>
  </div>
  <!-- 뒤로, 하트 이모지 추가 -->
  <div v-if="!isError">
    <PopUp v-if="popUpOpen" @close-modal="popUpOpen = false">
      <div class="modal-content">
        <p>정말 삭제하시겠습니까?</p>
        <button class="btn btn-secondary" @click="popUpOpen = false">취소</button>
        <button class="btn btn=danger" @click="storyDelete">삭제</button>
      </div>
    </PopUp>
    <div id="story">
      <div class="story-content">
        <div id="story-info">
          <img :src="host + story.user_pk.image" height="60" width="60" style="margin: 0 auto; cursor: pointer; border-radius: 30px" @click="moveToProfile" />
          <div class="d-flex justify-content-between" style="padding: 15px 0 0 10px">
            <span style="margin-left: 10px; font-size: 18px">{{ story.user_pk.nickname }} </span>
            <span>{{ story.created_at }}</span>
          </div>
        </div>
      </div>
      <p style="margin: 20px">{{ story.story_title }}</p>
      <div class="story-content">
        <div id="image">
          <img :src="host + story.story_picture" alt="이미지 영역입니다." style="width: 100%" />
        </div>
      </div>
      <div class="d-flex justify-content-center align-items-center" style="margin-top: 20px">
        <div class="d-flex justify-content-between align-items-center" style="width: 90%">
          <!-- 좋아요 기능 구현 -->
          <div class="like">
            <div>
              <i
                class="fa fa-solid fa-heart"
                :class="{ activate: isLike, deactivate: !isLike }"
                @click="likeStory"
                style="cursor: pointer; maring-left: 5px"
              ></i>
            </div>
            <span style="margin-left: 5px">{{ story.like_user_count }}</span>
          </div>
          <div style="margin-left: 10px" v-if="story.user_pk.user_pk == user_pk"><i class="fa fa-solid fa-trash" @click="popUpOpen = true"></i></div>
        </div>
      </div>
      <hr />
      <CommentList />
      <CommentForm />
    </div>
  </div>
  <div v-else>
    <h2>오류가 발생하였습니다. 다시 시도해주세요</h2>
  </div>
</template>

<script>
// import axios from 'axios'
import { computed, onBeforeMount, ref } from "vue";
import CommentList from "@/components/story/CommentList.vue";
import CommentForm from "@/components/story/CommentForm.vue";
import PopUp from "@/components/story/PopUp.vue";
// import api from '@/api/api'
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";
import { dataChange } from "@/hooks/dateChange";

export default {
  components: {
    CommentList,
    CommentForm,
    PopUp,
  },
  setup() {
    const host = "https://i7b209.p.ssafy.io";
    const store = useStore();
    const story = ref({});
    const isError = ref(false);
    const router = useRouter();
    const route = useRoute();
    const popUpOpen = ref(false);
    const user_pk = store.state.account.userInfo.user_pk;

    const isLike = computed(() => {
      if (story.value.like_user) {
        return story.value.like_user.includes(user_pk);
      } else {
        return false;
      }
    });

    const { howNow } = dataChange();

    // 데이터를 불러오는 함수
    onBeforeMount(async () => {
      isError.value = false;
      await store
        .dispatch("story/getCurrentStory", route.params.story_pk)
        .then(() => {
          story.value = store.state.story.currentStory;
        })
        .catch((error) => {
          console.error(error);
          isError.value = true;
        });
    });

    const storyDelete = async () => {
      await store.dispatch("story/deleteCurrentStory", route.params.story_pk);
      router.push({
        name: "story",
      });
    };

    // 폼에서 생성했을 시 뷰로 빠져나올 수 있게
    const goBack = () => {
      if (window.history.state.back.includes("create")) {
        router.push({
          name: "story",
        });
      } else {
        router.go(-1);
      }
    };

    const likeStory = async () => {
      await store.dispatch("story/likeStory", route.params.story_pk);
    };

    const moveToProfile = () => {
      router.push({
        name: "userProfile",
        params: {
          user_pk: story.value.user_pk.user_pk,
        },
      });
    };

    return {
      host,
      story,
      popUpOpen,
      isError,
      storyDelete,
      isLike,
      likeStory,
      goBack,
      howNow,
      moveToProfile,
      user_pk,
    };
  },
};
</script>

<style scoped>
#topView {
  background-color: #4D8D6D;
  color: white;
  padding-bottom: 10px;
}
.my-modal {
  overflow: hidden;
}

#story {
  width: 100%;
}

.story-content {
  display: grid;
  place-items: center;
  margin-top: 20px;
}

#image {
  width: 90%;
  display: flex;
  justify-content: center;
}

#story-info {
  width: 90%;
  display: grid;
  grid-template-columns: 15% auto;
  margin-top: 10px;
}

.activate {
  color: #f36e5d;
  -webkit-animation: jello-horizontal 0.6s both;
  animation: jello-horizontal 0.6s both;
}

@-webkit-keyframes jello-horizontal {
  0% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
  30% {
    -webkit-transform: scale3d(1.25, 0.75, 1);
    transform: scale3d(1.25, 0.75, 1);
  }
  40% {
    -webkit-transform: scale3d(0.75, 1.25, 1);
    transform: scale3d(0.75, 1.25, 1);
  }
  50% {
    -webkit-transform: scale3d(1.15, 0.85, 1);
    transform: scale3d(1.15, 0.85, 1);
  }
  65% {
    -webkit-transform: scale3d(0.95, 1.05, 1);
    transform: scale3d(0.95, 1.05, 1);
  }
  75% {
    -webkit-transform: scale3d(1.05, 0.95, 1);
    transform: scale3d(1.05, 0.95, 1);
  }
  100% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}
@keyframes jello-horizontal {
  0% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
  30% {
    -webkit-transform: scale3d(1.25, 0.75, 1);
    transform: scale3d(1.25, 0.75, 1);
  }
  40% {
    -webkit-transform: scale3d(0.75, 1.25, 1);
    transform: scale3d(0.75, 1.25, 1);
  }
  50% {
    -webkit-transform: scale3d(1.15, 0.85, 1);
    transform: scale3d(1.15, 0.85, 1);
  }
  65% {
    -webkit-transform: scale3d(0.95, 1.05, 1);
    transform: scale3d(0.95, 1.05, 1);
  }
  75% {
    -webkit-transform: scale3d(1.05, 0.95, 1);
    transform: scale3d(1.05, 0.95, 1);
  }
  100% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

.deactivate {
  color: darkgray;
}

.like {
  padding: 5px 10px 5px 10px;
  background-color: #ffe2e5;
  border-radius: 20px;
  display: flex;
  font-size: 18px;
  text-align: center;
}
</style>
