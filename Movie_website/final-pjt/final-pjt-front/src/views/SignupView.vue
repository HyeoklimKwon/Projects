<template>
  <div class=" background">  
   

  <div class="container">
    <div class="row justify-content-center" style="margin-top: 150px">
      <div class="col-md-5">
        <div class="card">
        <h2 class="card-title text-center">Sign up</h2>
          <div class="card-body py-md-4">
            <form @submit.prevent="signup(credentials)" _lpchecked="1">
              <div class="form-group">
                <label for="username">Username: </label>
                <input  v-model="credentials.username"  type="text" class="form-control" id="username" placeholder="User ID" required/>
              </div>               
                       
            <div class="form-group">
              <label for="password1"></label>
              <input  v-model="credentials.password1" type="password" class="form-control" id="password" placeholder="Password" required />
            </div>
            <div class="form-group">
                <label for="password2">Password Confirmation:</label>
                <input v-model="credentials.password2" type="password" class="form-control" id="confirm-password" placeholder="confirm-password" required />
            </div>
            <account-error-list v-if="authError"></account-error-list>
            <div class="d-flex flex-row align-items-center justify-content-between">
                <router-link :to="{ name: 'login' }">Login</router-link>
                  <button class="btn btn-primary">Create Account</button>
                    </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=PT+Sans');

body{
  background: #fff;
  font-family: 'PT Sans', sans-serif;
}
h2{
  padding-top: 1.5rem;
}
a{
  color: #333;
}
a:hover{
  color: #da5767;
  text-decoration: none;
}
.card{
  border: 0.40rem solid #f8f9fa;
  top: 10%;
}
.form-control{
  background-color: #f8f9fa;
  padding: 20px;
  padding: 25px 15px;
  margin-bottom: 1.3rem;
}

.form-control:focus {

    color: #000000;
    background-color: #ffffff;
    border: 3px solid #da5767;
    outline: 0;
    box-shadow: none;

}

.btn{
  padding: 0.6rem 1.2rem;
  background: #da5767;
  border: 2px solid #da5767;
}
.btn-primary:hover {

    
    background-color: #df8c96;
    border-color: #df8c96;
  transition: .3s;

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

</style>
