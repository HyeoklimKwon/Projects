<template>
  <div class="background4">
    <h1 style="margin-top: 305px ;font-family: 'Nanum Pen Script', cursive; font-size: 35px">Welcome to T.M.T</h1>
    <p3 style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">In this Website, you can watch free movies in 10 minutes</p3>
    <div style="margin-top: 150px">
        <router-link :to="{ name: 'movies' }">
          <b-button variant="success" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px"> Select Movie </b-button>
        </router-link>      
        
        <p>   </p>
        <router-link :to="{ name: 'logout' }">
            <b-button variant="danger" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">Next time Maybe</b-button>
        </router-link>
        
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
.background4{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/Mainbackground.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}
</style>