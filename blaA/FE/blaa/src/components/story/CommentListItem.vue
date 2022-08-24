<template>
  <li>
    <br />
    <div class="comment-info">
      <div>
        <img :src="host + comment.user_pk.image" width="50" height="50" style="border-radius: 50%" />
      </div>
      <div>
        <div class="d-flex justify-content-between">
          <span style="font-weight: 700">{{ comment.user_pk.nickname }}</span>
          <div>
            <span style="font-weight: 400; font-size: 15px">{{ comment.created_at }}</span>
            <div v-if="isUpdate" id="update">
              <div style="cursor: pointer" @click="[(isFix = true), (isUpdate = !isUpdate)]">수정</div>
              <div style="cursor: pointer" @click="[(popUpOpen = true), (isUpdate = !isUpdate)]">삭제</div>
            </div>
            <div style="display: inline-block; margin-left: 10px" v-if="user_pk == comment.user_pk.user_pk">
              <i class="fa fa-solid fa-bars hamburger" @click="[(isUpdate = !isUpdate)]"></i>
              <PopUp v-if="popUpOpen" @close-modal="popUpOpen = false">
                <div class="modal-content">
                  <p>정말 삭제하시겠습니까?</p>
                  <button class="btn btn-secondary" @click="popUpOpen = false">취소</button>
                  <button class="btn btn=danger" @click="commnetDelete">삭제</button>
                </div>
              </PopUp>
            </div>
          </div>
        </div>
        <div v-if="!isFix" style="font-weight: 300; margin-top: 5px; z-index=1; font-weight: 400;">{{ comment.story_comment }}</div>
        <div v-else>
          <textarea style="margin-top: 5px" class="updateCommnet" type="text" v-model="changeComment" @keyup.enter="commentFix"> </textarea>
        </div>
      </div>
    </div>
  </li>
</template>

<script>
import PopUp from "@/components/story/PopUp.vue";
import { useStore } from "vuex";
import { ref } from "vue";
import $ from "jquery";

export default {
  props: {
    comment: {
      type: Object,
      required: true,
    },
  },
  components: {
    PopUp,
  },
  setup(props) {
    const store = useStore();
    const popUpOpen = ref(false);
    const user_pk = store.state.account.userInfo.user_pk;
    const isFix = ref(false);
    const changeComment = ref("");
    const isUpdate = ref(false);
    const host = ref("https://i7b209.p.ssafy.io");
    changeComment.value += String(props.comment.story_comment);

    const commnetDelete = async () => {
      const comment_pk = props.comment.comment_pk;
      await store.dispatch("story/deleteComment", comment_pk);
    };

    const commentFix = async () => {
      const data = {
        comment_pk: props.comment.comment_pk,
        story_comment: changeComment.value,
      };
      await store.dispatch("story/fixComment", data);
      isFix.value = false;
    };

    return {
      user_pk,
      popUpOpen,
      commnetDelete,
      commentFix,
      isFix,
      changeComment,
      isUpdate,
      host,
    };
  },
};
</script>

<style scoped>
.comment-info {
  background-color: #f8f9fe;
  display: grid;
  grid-template-columns: 15% 85%;
  padding: 10px;
  border-radius: 16px;
}

.hamburger {
  transform: rotate(0.5turn);
}

#update {
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
  width: 70px;
  overflow: hidden;
  border: 1px black solid;
  border-radius: 12px;
  padding: 5px;
  z-index: 10;
  -webkit-animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
  animation: slide-in-top 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

@-webkit-keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}
@keyframes slide-in-top {
  0% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
    opacity: 1;
  }
}

#update > div {
  font-weight: 600;
  font-size: 18px;
  padding: 3px;
}

.updateCommnet {
  width: 100%;
  padding: 10px;
  border-radius: 12px;
  height: 100%;
}
</style>
