<template>
  <div class="background3">
    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        alert('잘못된 접근')
        this.$router.back()
      }
    },
  }
</script>

<style>
.background3{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/goodbye.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}
</style>
