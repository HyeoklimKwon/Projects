<template>
    <div>
        {{ movie.title }}
        <button @click="deleteMovie">x</button>
    </div>
  
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'WatchListItem',
    props: {
        movie: Object,
    },
    methods: {
        ...mapActions(['craeteMovie', 'deleteMovie']),

    }

}
</script>

<style>

</style>