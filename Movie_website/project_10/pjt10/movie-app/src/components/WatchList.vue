<template>
    <div>
        <watch-list-item
        v-for=" movie in movies"
        :key="movie.date"
        :movie = "movie">
        </watch-list-item>
    </div>
  
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'

export default {
    name: 'WatchList',
    components: { WatchListItem },
    computed: {
        movies() {
            return this.$store.state.movies
        }
    }
  

}
</script>

<style>

</style>