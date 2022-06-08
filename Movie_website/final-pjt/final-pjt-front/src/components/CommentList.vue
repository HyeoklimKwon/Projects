<template>
  <div class="comment-list"  >  
    <div>
      <ul>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.pk">
        </comment-list-item>        
      </ul>
    </div>  
  <comment-list-form></comment-list-form>  
  </div>
  
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
.comment-list {
  border: 1px solid blue;
}
</style>