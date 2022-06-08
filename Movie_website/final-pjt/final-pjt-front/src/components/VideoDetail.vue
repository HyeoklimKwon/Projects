<template>
  <div>
    <iframe
      width="640"
      height="360"
      :src="`https://www.youtube.com/embed/${selectedVideo.id.videoId}`"
      frameborder="0"></iframe>    
  </div>
</template>

<script>
export default {
  props: {
    selectedVideo: {
      type: Object,
      required: true,
    }
  },
}
</script>

<style>

</style>