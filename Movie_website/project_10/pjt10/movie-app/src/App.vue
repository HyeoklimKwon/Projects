<template>
  <div id="app">
    <b-nav tabs class="d-flex justify-content-end">  
      <b-nav-item>
        <router-link to = '/'>Home</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link to = '/random'>Random</router-link>
      </b-nav-item>     
      <b-nav-item>
        <router-link to = '/watch-list'>MyMovieList</router-link>
      </b-nav-item>
    </b-nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
