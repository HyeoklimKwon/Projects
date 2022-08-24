<template>
  <div v-if="userInfo">
    <div class="search">
      <input v-model="searchText" type="text" placeholder="닉네임 검색" />
    </div>
    <div v-for="user in filteredUsers" :key="user.user_pk">
      <!-- <img :src= "user.image" alt="#"> -->
      <div>{{ user.nickname }}</div>   
      <button @click="gochat(user.user_pk)">채팅하기</button>
    </div>  
  </div>
  <div v-else>로그인이 필요합니다.</div>
</template>

<script>
import axios from "axios";
import api from "@/api/api.js";
import { useStore } from "vuex";
import { onBeforeMount, reactive, ref, computed } from "vue";
import router from "@/router";

export default {
  setup() {
    const store = useStore();
    const userInfo = store.state.account.userInfo;
    const gochat = (from_userpk) => {
      router.push({
        name: "chat",
        params: {
          from_userpk: from_userpk,
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
    onBeforeMount(() => {
      if (userInfo) {
        let token = store.state.chat.token;
        axios
          .get(api.accounts.searchallusers(), {
            headers: { Authorization: `Bearer ${token}` },
          })
          .then((response) => (state.users = response.data.results));
        console.log(state.users);
      }
    });

    return {
      state,
      searchText,
      gochat,
      filteredUsers,
      userInfo,
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