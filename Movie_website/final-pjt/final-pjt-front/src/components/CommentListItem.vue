<template>
  <li class="comment-list-item" >
    <div class="container" style="display: flex; justify-content: space-between;">
      <div>
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">
          {{ comment.user.username }}
        </router-link>:       
        <span v-if="!isEditing" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px;">{{ payload.content }}</span>
        <span v-if="isEditing">
          <input style ="margin-right: 850px" type="text" v-model="payload.content">
          <b-button variant="outline-primary" @click="onUpdate" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px; ">Update</b-button> |
          <b-button variant="outline-danger" @click="switchIsEditing" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px; ">Cancel</b-button>
        </span>
      </div>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <b-button variant="outline-success" @click="switchIsEditing" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px; ">Edit</b-button> |
        <b-button variant="outline-danger" @click="deleteComment(payload)" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Delete</b-button>
      </span>
    </div>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },      
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}

.container {
  margin: 0px 0px 0px 0px;
}
</style>