<template>
  <div>  
    <link rel="stylesheet" href="style.css"> 
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=Alata&display=swap" rel="stylesheet">
    <div class="page-container  background">
        <div class="login-form-container shadow ">
            <div class="login-form-right-side">
                <div class="top-logo-wrap">                    
                </div>
                <div >
                  <h1>Ten</h1>
                  <h1>Minutes</h1>
                  <h1>Theater</h1>
                  <hr>
                  <p2>Life is short, </p2>
                  <br>
                  <p2>you need Ten Minutes Theater</p2>

                </div>
            </div>
            <div class="login-form-left-side">
                <div class="login-top-wrap">
                    <span>Don't have an account?</span>
                    <router-link :to="{ name: 'signup' }">
                     <button class="create-account-btn shadow-light">Sign Up</button>                      
                    </router-link>
                </div>

              <form @submit.prevent="login(credentials)">
                <div class="login-input-container">
                    <div class="login-input-wrap input-id">
                        <i class="far fa-envelope"></i>
                        <label for="username"></label>
                        <input v-model="credentials.username" placeholder="User ID" type="text" id="username" required >
                    </div>
                    <div class="login-input-wrap input-password">
                        <i class="fas fa-key"></i>
                        <label for="password"></label>
                        <input v-model="credentials.password" placeholder="Password"  type="password"  id="password" required>
                    </div>
                </div>
                <account-error-list v-if="authError"></account-error-list>
                <div class="login-btn-wrap">
                    <button class="login-btn">Login</button>                    
                </div>
              </form>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style>
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Alata', sans-serif;
}

.page-container{
    width: 100vw;
    height: 100vh;
    background: #eff0f2;
    display: flex;
    justify-content: center;
    align-items: center;

}
.shadow{
    -webkit-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    -moz-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
}/*
.shadow-light{
    -webkit-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    -moz-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);

}*/
.login-form-container{
 
    background:#f5f5f5 ;
    width:860px;
    height: 540px;
    display: flex;
    flex-direction: row;
    box-shadow: 10px black;
    border-radius: 10px;

}
.login-form-right-side{
    width: 50%; 
    border-radius: 10px 0px 0px 10px;
    padding:75px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    background-image: 
  radial-gradient(ellipse farthest-corner at 0 140%, #5d9dff 0%, #2178ff 70%, #3585ff 70%);
}
.login-form-right-side h1{
    color: white;
    width:100%;
    text-align: right;
    opacity: 0.9;

}
.login-form-right-side p{
    padding-top: 50px;
    font-size:12px;
    text-align: right;
    opacity: 0.8;
}
.login-form-left-side{
    width: 50%;
    border-radius: 0px 10px 10px 0px;
    display: flex;

    flex-direction: column;
    align-items: center;
    padding:40px;
    background: rgb(255,255,255);
background: linear-gradient(287deg, rgba(255,255,255,1) 0%, rgba(243,244,244,1) 0%, rgba(255,255,255,1) 100%);
}
.login-form-left-side .login-top-wrap{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width:100%;
}
.login-form-left-side .login-top-wrap span{
    color: gray;
    font-size: 11px;
    padding-right:20px;

}
.login-form-left-side .login-top-wrap .create-account-btn {
    background: white;
    border:  0;
    width:85px;
    height: 35px;
    font-size: 11px;
    color: #2178ff;
    border-radius: 3px;

}
.login-input-container{
    padding-top:120px;
    width:300px;
}
.login-input-container .login-input-wrap{
    width:300px;
    height: 45px;
    margin-top: 20px;
    border-radius: 2px;
    border-bottom: solid 2px #2178ff;
   
}
.login-input-container .login-input-wrap i{
    color: #2178ff;
    line-height: 45px;
}

.login-input-container .login-input-wrap input{
    background: none;
   
    border: none;
    line-height: 45px;
    padding-left:10px;
    width:267px;
}
.login-input-container .login-input-wrap input:focus{
    outline: none;
}
.login-btn-wrap{
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;;
}
.login-btn-wrap .login-btn{
    width:95px;
    height:35px;
    color:white;
    border: 0;
    border-radius: 4px;

    background: rgb(105,163,255);
background: linear-gradient(162deg, rgba(105,163,255,1) 0%, rgba(43,125,254,1) 50%, rgba(43,125,254,1) 100%);
}
.login-btn-wrap a{
    margin-top:10px;
    text-decoration: none;
    font-size: 11px;
    color: gray;

}

.background{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/backgroundmovie.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}

.background2{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/backgroundmovie.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  opacity: 0.4;
  
}
</style>
