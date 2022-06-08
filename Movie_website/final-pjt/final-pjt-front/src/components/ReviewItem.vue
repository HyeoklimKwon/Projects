<template>
  <div>
    <li class="review-list-item my-3 d-flex justify-content-between">
      <div class="mx-5"> 
        <div v-if="!isEditing">리뷰: {{ payload.content }}  평점: {{ payload.grade }}</div>
        <span> 글쓴이: </span>
        <router-link :to="{ name: 'profile', params: { username: review.user.username } }" style="text-decoration: none">
          {{ review.user.username }}
        </router-link>
      </div>
      <div>
        <span v-if="isEditing">
          <input type="text" v-model="payload.content">
          <input type="text" v-model="payload.grade">
          <button @click="onUpdate" class="mx-3 btn btn-outline-secondary">Update</button> 
          <button @click="switchIsEditing" class="mx-3 btn btn-outline-secondary">Cancle</button>
        </span>

        <span v-if="currentUser.username === review.user.username && !isEditing">
          <button @click="switchIsEditing" class="mx-3 btn btn-outline-secondary">Edit</button> 
          <button @click="deleteReview(payload)" class="mx-3 btn btn-outline-secondary">Delete</button>
        </span>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        grade: this.review.grade
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.review-list-item {
  border: 1px
}
</style>