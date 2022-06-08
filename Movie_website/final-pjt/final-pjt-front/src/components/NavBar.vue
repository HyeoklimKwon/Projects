<template>
  <nav class="navbar navbar-light" >
      <router-link :to="{ name: 'movies' }">
        <img src="../assets/logo2.png" alt="" width="100" height="50">
      </router-link>
      <div>
        <span v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Login</router-link>
      </span>
      <span v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Signup</router-link>
      </span>
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'articles' }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Community</router-link>
      </span>
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">
          {{ currentUser.username }}'s page
        </router-link>
      </span>
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Logout</router-link>
      </span>
      </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
  nav {
    padding: 30px;
    background-color: #101111;
  }

  nav a {
    font-weight: bold;
    color: #f1f3f5;
    text-decoration: none;
    margin-left: 1rem;
  }

  nav a.router-link-exact-active {
    color: #42b983;
  }
</style>
