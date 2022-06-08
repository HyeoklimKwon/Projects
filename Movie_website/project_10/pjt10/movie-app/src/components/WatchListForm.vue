<template>
  <div>      
      <input type="text" 
      v-model.trim="movieTitle"
      @keyup.enter="createMovie">
      <button
      @click="createMovie">Add</button>
  </div>
</template>

<script>
export default {
    name: 'WatchListForm',
    data() {
        return {
            movieTitle: ''
        }
    },
    methods: {
        createMovie() {
            const newMovie = {
                title: this.movieTitle,
                isCompleted: false,
                date: new Date().getTime()
            }
            this.$store.dispatch('createMovie', newMovie)
            this.movieTitle = ''
        }
    }
}
</script>

<style>

</style>