<template>
  <div>
    <h1>My Movie List</h1>
    <watch-list-form></watch-list-form>   
    <watch-list></watch-list> 
  </div>
</template>

<script>
import WatchList from '@/components/WatchList.vue'
import WatchListForm from '@/components/WatchListForm.vue'


export default {
  name: 'WatchListView',
  components: {
    WatchList, WatchListForm    
  },
}
</script>

<style>

</style>