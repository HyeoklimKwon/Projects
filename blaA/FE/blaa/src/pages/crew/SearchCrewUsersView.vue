<template>
  <div v-if="userInfo">    
    <div class="view chat" style="background-color : #eec95c">    
      <header class="chat_list_wrap">   

        <div class="search">
          <input v-model="searchText" type="text" placeholder="Search user to invite" />
        </div>
      </header>
      <section class= "chat-box">
        <br />
        <div v-for="user in filteredUsers" :key="user.user_pk">
          <b-card>
            <b-card-text>
              <div class="d-flex justify-content-center">
                <img  id = "searchprofile" class="imgProfile" :src="HOST + user.image" alt="" />           
                  <b class="chodaeorchatname d-flex align-items-center">
                    {{ user.nickname }}
                  </b>          
              </div>
              <br>
              <div class="d-flex justify-content-end align-items-center chodaeorchatbutton" style="padding-right : 20px">
                <button class="w-btn w-btn-yellow" @click="inviteuser(crew_pk, user.user_pk)">초대하기</button>            
                <button class="w-btn w-btn-green" @click="gochat(user.user_pk, user.nickname)">채팅하기</button>
              </div>
            </b-card-text>
          </b-card>
        </div>
      </section>
      
   

      
    </div>
  </div>
  <div v-else>로그인이 필요합니다.</div>
</template>
<script>
import axios from "@/api/axios.js";
import api from "@/api/api.js";
import { useStore } from "vuex";
import { onMounted, reactive, ref, computed } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

export default {
  setup() {
    const HOST = ref("https://i7b209.p.ssafy.io");
    const store = useStore();
    const route = useRoute();
    const userInfo = store.state.account.userInfo;
    const crew_pk = route.params.crew_pk;
    const gochat = (from_userpk, from_usernickname) => {
      router.push({
        name: "chat",
        params: {
          from_userpk: from_userpk,
          from_usernickname : from_usernickname
        },
      });
    };
    const searchText = ref("");

    const filteredUsers = computed(() => {
      if (searchText.value) {
        return state.users.filter((user) => {
          return user.nickname.includes(searchText.value);
        });
      }
      return state.users.filter((user) => {
        return user.nickname.includes("!@#$%");
      });
    });

    const state = reactive({
      users: [],
    });

    onMounted(() => {
      if (userInfo) {
        axios.get(api.accounts.searchallusers()).then((response) => {
          state.users = response.data; 
        });
      }
    });

    const inviteuser = async (invitingcrew_pk, inviteduser_pk) => {
      try {
        const result = await axios.post(api.crew.inviteuser(invitingcrew_pk, inviteduser_pk), {});
        alert(result.data.message);
      } catch (error) {
        alert(error.response.data.message);
      }
    };

    return {
      state,
      searchText,
      gochat,
      filteredUsers,
      userInfo,
      crew_pk,
      inviteuser,
      HOST
    };
  },
};
</script>

<style>
.w-btn {
  position: relative;
  border: none;
  display: inline-block;
  padding: 15px 30px;
  border-radius: 15px;
  font-family: "paybooc-Light", sans-serif;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  font-weight: 600;
  transition: 0.25s;
}
.w-btn-green {
  background-color: #498d6d;
  color: #d7fff1;
  margin-left: 6px;
}

.w-btn-yellow {
  background-color: #eec95c;
  color: #6e6e6e;
  margin-right: 3px;
}
.notiimg {
  width: 70px;
  height: 70px;
  border-radius: 50px;
}
.chodaeorchatbutton {
  width: 100%;
  height: 40%;
  margin-bottom: 10px;
}
.chodaeorchatname {
  margin-left: 10px;
}

.search {
  width: 100%;
    border-radius: 4px;
    padding: 5px 0;
    border: 0;
    text-align: center;

}

#searchprofile {
  width: 50px;
  height: 50px;
  border-radius: 70%;
  overflow: hidden;
  margin-right : 13px
}


  
</style>
