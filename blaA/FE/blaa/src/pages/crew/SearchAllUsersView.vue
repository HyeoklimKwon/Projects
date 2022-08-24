<template>  
  <div v-if="userInfo">    
    <div class="view chat">    
      <header class="chat_list_wrap">   

        <div class="search">
          <input v-model="searchText" type="text" placeholder="Search user to chat" />
        </div>
      </header>
      <section class= "chat-box">
        <br />
        <div v-for="user in filteredUsers" :key="user.user_pk">
          <b-card>
            <b-card-text class="d-flex justify-content-between align-items-center">
              <div @click="moveToProfile(user.user_pk)" >                
                <img style="margin-left: 20px" id = "searchprofile" class="imgProfile" :src="HOST + user.image" alt="" />           
                  <b>
                    {{ user.nickname }}               
                  </b>                                                                     
              </div>
              <button class="w-btn w-btn-green" @click="gochat(user.user_pk, user.nickname)">채팅하기</button>              
              <br>
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
          from_usernickname : from_usernickname,
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

    const moveToProfile = (user_pk) => {
      router.push({
        name: "userProfile",
        params: {
          user_pk: user_pk,
        },
      });
    };

    return {
      state,
      searchText,
      gochat,
      filteredUsers,
      userInfo,
      crew_pk,
      inviteuser,
      moveToProfile,
      HOST
    };
  },
};
</script>

<style>
ul.mylist,
ol.mylist {
  padding: 5px 0px 5px 5px;
  margin-bottom: 5px;
  border-bottom: 1px solid #efefef;
  font-size: 12px;
}
ul.mylist li:before,
ol.mylist li:before {
  content: ">";
  display: inline-block;
  vertical-align: middle;
  padding: 0px 5px 6px 0px;
}
ul.mylist li:last-child,
ol.mylist li:last-child {
  border-bottom: 0px;
}
</style>