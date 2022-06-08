<template>
<div>
  <div class="background4">    
    <div class="card">
    <div class="card-header">      
    </div>
    <div class="card-body">      
      <p class="full-name">{{ profile.username}}                
          <i v-if="isUser" @click="follow" class="fa-solid fa-heart-circle-plus"></i>        
      </p>
      <p class="username">가입일 : {{ profile.created_at.substring(0,10) }}</p>              
    </div>
    <div class="card-footer">
      <div class="col">
        <p><span class="count">{{ profile.followers }}</span> Followers</p>
      </div>
      <div class="col">
        <p><span class="count" id="following">{{ profile.followings }}</span> Following</p>
      </div>
    </div>
   </div>
    <br>
    <br>
    <br>
    <br>    
    <hr>
    <i class="fa-solid fa-pencil"></i> 
       <div v-for="article in articles" :key="article.pk"  >              
        <div v-if="article.user.username == profile.username" class="card">
          <div class="card-body">            
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }" style="font-family: 'Nanum Pen Script', cursive; font-size: 25px">           
             {{ article.title }}
            </router-link>
          </div>
        </div>        
      </div>
    
    <br>
    <hr>   
  </div>  
  
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'ProfileView',
  data: function () {
    return {
      isUser : null,
      created_at : null,
      
    }
    
  },
  computed: {
    ...mapGetters(['profile', 'currentUser','articles']),
    
  },
  methods: {
    ...mapActions(['fetchProfile']),
    setToken: function () {
      const config = {
        Authorization:  `Token ${localStorage.getItem('token')}`,
      }
      return config
    },
    follow: function() {
      console.log(this.setToken());
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/accounts/follow/${this.$route.params.username}/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res.data);
      })
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    const pagename = this.$route.params.username
    const username = this.currentUser.username
    if (pagename === username){
      this.isUser = false
    } else {
      this.isUser =true
    }    
    this.fetchProfile(payload)
  },

  countFollow: function (data) {
      // console.log(data.count);
      const followCount =document.querySelector('#following')
      followCount.innerText =data
    }
  
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
* {
  box-sizing: border-box;
}

body {
  font-family: "Raleway";
  background-color: #e6e6e6;
}

.card {
  width: 400px;
  margin: auto;
  background-color: #fff;
  box-shadow: 0 3px 30px rgba(0,0,0,.14);
  color: #444;
  text-align: center;
  font-size: 16px;
}

.card .card-header {
  position: relative;
  height: 48px;
}
.card .card-header .profile-img{
  width: 96px;
  height:96px;
  border-radius: 1000px;
  position: absolute;
  left : 50%;
  transform: translate(-50%, -50%);
  border: 6px solid #fff;
  box-shadow: 0 0 20px rgba(0,0,0,.2);
}

.card .card-body {
  padding: 10px 40px;

}
.card .card-body .full-name{
  font-size:20px;
  font-weight: 600;
  text-transform: uppercase;
  margin: 10px 0 0;

}
.card .card-body .username {
  font-size: 13px;
  color:#777;
  margin: 5px 0 0;
}
.card .card-body .city {
  font-weight: 500;
  margin :10px 0 0
}

.card .card-body .desc {
  line-height: 24px;
}

.card .card-footer {
  display:table;
  width: 100%;
  border-top: 1px solid #e6e6e6;

}
.card .card-footer .col{
  display: table-cell;
  padding: 5px 10px;
  font-size: 15px;
}
.card .card-footer .count {
  font-size: 18px;
  font-weight: 600;
}

.vr {
  border-right: 1px solid #e6e6e6;
}

@media screen and (max-width: 575px) {
  .card {
    width: 96%;
  }
  .card .card-body {
    padding: 10px 20px;
  }

  .card .card-footer .col {
    padding:0 10px;
  }
  .card .card-footer .count {
    display: block;
    margin-bottom: 5px;
  }


}

.background4{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/profilebackground.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}
</style>