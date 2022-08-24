<template>
<div>
  <!-- 클릭하거나 엔터를 치면 -->
  <input type="text" v-model="searchText" @keypress.enter="search">
  <span @click="search"><i class="fa fa-solid fa-magnifying-glass"></i></span>
</div>
</template>

<script>
import { ref } from 'vue'

export default {
  emits: ['search-store'],
  setup(props, {emit}) {
    const searchText = ref('')    

    const search = () => {
      emit('search-store', searchText.value)
    }

    return {
      searchText,
      search
    }
  }
}
</script>

<style>

</style>