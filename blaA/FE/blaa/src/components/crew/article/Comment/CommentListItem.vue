<template>
  <li>
    <div class="comment-info">
      <div class="d-flex justify-content-between align-items-center" style="height: 30px;">
        <span style="font-weight: 700">{{ comment.nickname }}</span> 
        <div class="d-flex align-items-center">
          <span style="margin-right: 5px; margin-top: 5px;">{{ howNow(comment.created_at) }}</span>
          <div v-if="user_pk == comment.user" style=" margin: auto 0; display:inline-block; height: 30px;">
            <span @click="isUpdtae=!isUpdate" style="font-size:30px;" class="material-symbols-outlined">menu</span>
              <div v-if="isUpdate" id="update" style="">
                <span style="display: inline-block; margin-right: 10px; cursor: pointer" @click="modiComment">수정</span>
                <span style="display: inline-block; cursor: pointer" @click="deleComment">삭제</span>
                  <!-- <PopUp v-if="popUpOpen" @close-modal="popUpOpen = false">
                    <div class="modal-content">
                      <p>정말 삭제하시겠습니까?</p>
                      <button class="btn btn-secondary" @click="popUpOpen = false">취소</button>
                      <button class="btn btn=danger" @click="commnetDelete">삭제</button>
                    </div>
                  </PopUp> -->
              </div>
            </div>
        </div>
      </div>
    </div>
    <div style="margin-top: 5px;">{{ comment.comment_content }}</div>
  </li>
</template>

<script>
// import PopUp from "@/components/story/PopUp.vue";
import { useStore } from "vuex";
import { ref } from "vue";
import {dataChange} from '@/hooks/dateChange'

export default {
  props: {
    comment: {
      type: Object,
      required: true,
    },
  },
  components: {
    // PopUp,
  },
  setup(props) {
    const store = useStore();
    const popUpOpen = ref(true);
    const user_pk = store.state.account.userInfo.user_pk;
    const isUpdate = ref(false)

    const {
      howNow
    } = dataChange()

    // const commnetDelete = async() => {
    //   const comment_pk = props.comment.comment_pk
    //   await store.dispatch('story/deleteComment', comment_pk)
    // }

    const deleComment = async () => {
      const comment_pk = props.comment.crew_comment_pk;
      await store.dispatch("crew/deleComment", comment_pk);
    };

    return {
      user_pk,
      popUpOpen,
      deleComment,
      howNow,
      isUpdate
    };
  },
};
</script>

<style scoped>
li {
  list-style: none;
}

#update {

}

.comment {
  background-color: #f8f9fe;
  border-radius: 16px;
  padding: 12px;
}

</style>
