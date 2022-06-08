<template>
  <b-button variant="outline-info" @click="search">Start Movie</b-button>  
</template>

<script>
export default {
  methods: {
    search(event) {
      this.$emit('set-input-value', event.target.value)
    }
  }
}
</script>

<style>

</style>