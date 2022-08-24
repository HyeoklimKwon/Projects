<template>
<body>
    <div v-if="userInfo">
      <div class="chat_list_wrap">
          <div class="header">
              {{ userInfo.nickname }}'s bla
          </div>
          <div class="search">
              <input v-model="searchText" type="text" placeholder="닉네임 검색" />
          </div>
          <div class="list">
              <ul>
                  <li @click="gochat(message.from_userpk)" v-for="message in filteredMessages" :key = "message.key">
                      <table cellpadding="0" cellspacing="0">
                          <tr>
                              <td class="profile_td">
                              <!--ProfileImg-->
                                  <img src="" />
                                  <div>{{ message.from_userpk }}</div>
                              </td>
                              <td class="chat_td">
                              <!--Email & Preview-->
                                  <div class="username">
                                      {{ message.username}}
                                  </div>
                                  <div class="chat_preview">
                                      {{ message.content }}
                                  </div>
                              </td>                            
                          </tr>
                      </table>
                  </li>          
              </ul>
          </div>
      </div>
    </div>
    <div v-else>
      <div>로그인이 필요함</div>
    </div>
</body>     
</template>

<script>
import router from '@/router';
import db from '@/db'
import { reactive, onMounted, ref, computed } from 'vue';
import { useStore } from "vuex";
import api from "@/api/api.js"
import axios from 'axios'

export default {
  setup () {
    const gochat = (from_userpk) => {
      router.push({ name: 'chat',
      params: {
        from_userpk: from_userpk
      }}
      )
    }

    const store = useStore();

    const userInfo = store.state.account.userInfo;

    const searchText = ref('');
    const filteredMessages = computed(() => {
      if (searchText.value) {
        return state.messages.filter( message => {
          return message.username.includes(searchText.value);
        });
      }
      return state.messages;
    });

    const state = reactive({      
      messages: [],      
      
    })

    onMounted(() =>  {      
      if (userInfo) {
        const messageRef = db.database().ref("messages");     
        
        messageRef.on('value', snapshot =>  {
          const data = snapshot.val();
          let messages = [];
               
          Object.keys(data).forEach(key =>       
          {if (data[key].to_userpk == userInfo.user_pk) {            
              messages.push({
                id: key,
                username: data[key].username,
                content: data[key].content,
                from_userpk : data[key].from_userpk,
                to_userpk : data[key].to_userpk,
                to_usernickname : "sorry",
                to_userprofileurl : "you failed"                
              })                         
            }
          }
          )          
          let arrayUniqueByKey = [...new Map(messages.map(item =>
          [item['from_userpk'], item])).values()];
          let token = sessionStorage.getItem("token");

          for (let index = 0; index < arrayUniqueByKey.length; index++)  {                         
            axios.get(api.accounts.myInfo(arrayUniqueByKey[index]['from_userpk']),
            {
              headers : {"Authorization": `Bearer ${token}`}
            }).then(response => {                          
              arrayUniqueByKey[index]['to_usernickname'] = response.data.nickname,
              arrayUniqueByKey[index]['to_userprofileurl'] = response.data.image                                            
            })                 
                                   
          }
          state.messages = arrayUniqueByKey;         
        
          // state.messages = arrayUniqueByKey;  
          // console.log(state.messages[2]['to_usernickname']);      
                           
        })             
      }
        
    }
    )
    return {
      gochat,
      userInfo,
      state,
      filteredMessages,
      searchText

    }
  }

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
body {
  font-size: 11px;
}
.chat_list_wrap {
  list-style: none;
}
.chat_list_wrap .header {
  font-size: 14px;
  padding: 15px 0;
  background: #1daa13;
  color: white;
  text-align: center;
  font-family: "Josefin Sans", sans-serif;
}
.chat_list_wrap .search {
  background: #eee;
  padding: 5px;
}
.chat_list_wrap .search input[type="text"] {
  width: 100%;
  border-radius: 4px;
  padding: 5px 0;
  border: 0;
  text-align: center;
}
.chat_list_wrap .list {
  padding: 0 16px;
}
.chat_list_wrap .list ul {
  width: 100%;
  list-style: none;
  margin-top: 3px;
}
.chat_list_wrap .list ul li {
  padding-top: 10px;
  padding-bottom: 10px;
  border-bottom: 1px solid #e5e5e5;
}
.chat_list_wrap .list ul li table {
  width: 100%;
}
.chat_list_wrap .list ul li table td.profile_td {
  width: 50px;
  padding-right: 11px;
}
.chat_list_wrap .list ul li table td.profile_td img {
  width: 50px;
  height: auto;
}
.chat_list_wrap .list ul li table td.chat_td .username {
  font-size: 12px;
  font-weight: bold;
}
.chat_list_wrap .list ul li table td.time_td {
  width: 90px;
  text-align: center;
}
.chat_list_wrap .list ul li table td.time_td .time {
  padding-bottom: 4px;
}
.chat_list_wrap .list ul li table td.time_td .check p {
  width: 5px;
  height: 5px;
  margin: 0 auto;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  border-radius: 50%;
  background: #e51c23;
}

</style>