<template>   
  <!-- <div class="view login" v-if="state.username === '' || state.username === null">
    <form class="login-form" @submit.prevent="Login">
      <div class="form-inner">
        <h1>Login to FireChat</h1>
        <label for="username">Username</label>
        <input 
          type="text" 
          v-model="inputUsername" 
          placeholder="Please enter your username..." />
        <input 
          type="submit" 
          value="Login" />
      </div>
    </form>
  </div>   -->
 
  
  <div class="view chat"  v-if="userInfo">
    <header class="d-flex justify-content-center align-items-center" style="padding-bottom : 0px">
      <h1 style="margin : 0">{{ from_usernickname}}</h1>         
    </header>    
    <section class = "chat-box">
      <div 
        v-for="message in state.messages" 
        :key="message.key" 
        :class="(message.username == state.username ? 'message current-user' : 'message')">
        <div class="message-inner">
          <div>
            <img v-if="message.username != state.username" id = "chatprofile" class="imgProfile" :src="HOST + state.userprofile" alt="">             
            <div class="content">{{ message.content }}</div>
          </div>          
        </div>
      </div>
    </section>
    <footer>
      <form @submit.prevent="SendMessage">
        <input 
          type="text" 
          v-model="inputMessage" 
          placeholder="Write a message..." />
        <input 
          type="submit" 
          value="전송" />     
      </form>
    </footer>    
  </div>

  <div v-else>
    <h1>로그인이 필요합니다.</h1>    
  </div>
</template>

<!-- 
 1. {from_userpk, from_userpk_url, to_userpk_url, to_userpk, content } 형태로 message를 저장 /accounts/${userpk} => userpk에 해당되는 정보 받기
 2. 채팅 목록 생성 방법 feedback : 
    : 현재 유저 pk와 to_userpk와 같은 messages
      모든 메세지 중 to,from_user 안에 currenuserpk 들어간걸 다 뽑아서 
      to_userpk.content를 전체 for문을 처음부터 끝까지 돌면서 갱신 => 이러면 content는 가장 최신 content가 되고 
      from_user별로 content와 from_userurl로 목록을 만들어준다. 
 3. 채팅 불러오기 
    : 그렇게 만든 목록을 클리하면 클릭한 user_pk 또는 currentuser_pk가 from_userpk, to_userpk에 있는 모든 messages를 갖고 오고 
    채팅창에 currentuser별로 채팅 css를 다르게 구성하여 보여준다. 
-->
<script>
import { reactive, onMounted, ref, onUpdated } from 'vue';
import db from '@/db'
import router from '@/router';
import { useStore } from "vuex";
import { useRoute } from 'vue-router'
import api from "@/api/api.js"
import axios from "@/api/axios.js";


export default {
  setup () {
    const store = useStore(); 
    const route = useRoute()
    const userInfo = store.state.account.userInfo; 
    const from_userpk = route.params.from_userpk 
    const from_usernickname = route.params.from_usernickname
  
            

    console.log("from_userpk는",from_userpk)
     
    const inputMessage = ref("");
    var scrollingElement = (document.scrollingElement || document.body);

    const scrollToBottom = () => {
      scrollingElement = (document.scrollingElement || document.body)
      scrollingElement.scrollTop = scrollingElement.scrollHeight;
    }

    const state = reactive({
      username: "",
      messages: [],
      userprofile : "",
    })
 
    const HOST = ref("https://i7b209.p.ssafy.io");
    const Logout = () => {
      state.username = "익명";
    }

    const SendMessage = async () => {
      console.log("Sendmessage");      
      const messageRef = db.database().ref("messages");
      if(inputMessage.value === "" || inputMessage.value === null){
        console.log("nothing");
        return;
      }

      const message = {
        username: state.username,
        content: inputMessage.value,
        from_userpk: userInfo.user_pk,
        to_userpk: parseInt(from_userpk),
        profileurl : userInfo.image        
      }

      await messageRef.push(message); 
      inputMessage.value = "";   
      scrollToBottom()
              
    }    

    onUpdated(() => {
      scrollToBottom()
    })

    onMounted(() => {
      console.log(userInfo.image);
      if (userInfo) {
        state.username = store.state.account.userInfo.nickname
        axios.get(api.accounts.myInfo(from_userpk)).then((response) => {
            console.log(response.data.image);
            state.userprofile =  response.data.image
          })           
        const messageRef = db.database().ref("messages");     
        messageRef.on('value', snapshot => {
          const data = snapshot.val();
          let messages = []; 
          Object.keys(data).forEach(key => {
            if ((data[key].to_userpk == userInfo.user_pk && data[key].from_userpk == parseInt(from_userpk)) || 
                  (data[key].to_userpk == parseInt(from_userpk) && data[key].from_userpk == userInfo.user_pk)) {
              messages.push({
                id: key,
                username: data[key].username,
                content: data[key].content,
                to_userpk: data[key].to_userpk,
                from_userpk: data[key].from_userpk,
                to_userprofile: data[key].to_userprofile
              })            
            }
          }) 
          state.messages = messages;                 
        })
       
      }
    })

    const goback = () => {
      router.push({ path : '../'})
     
    }
    return {           
      state,
      inputMessage,
      SendMessage,
      goback,
      Logout,
      scrollToBottom,
      userInfo,
      from_userpk,     
      from_usernickname,
      HOST
      
    }
  }
};
</script>

<style scoped>
  * {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  }

  .view {
    display: flex;
    justify-content: center;
    min-height: 100vh;
    background-color: #498D6D;
  }
  .view.login {
    align-items: center;
  }
  .view.login .login-form {
    display: block;
    width: 100%;
    padding: 15px;
  }
  .view.login .login-form .form-inner {
    display: block;
    background-color: #FFF;
    padding: 50px 15px;
    border-radius: 16px;
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
  }
  .view.login .login-form .form-inner h1 {
    color: #AAA;
    font-size: 28px;
    margin-bottom: 30px;
  }
  .view.login .login-form .form-inner label {
    display: block;
    margin-bottom: 5px;
    color: #AAA;
    font-size: 16px;
    transition: 0.4s;
  }
  .view.login .login-form .form-inner input[type=text] {
    appearance: none;
    border: none;
    outline: none;
    background: none;
    display: block;
    width: 100%;
    padding: 10px 15px;
    border-radius: 8px;
    margin-bottom: 15px;
    color: #333;
    font-size: 18px;
    box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);
    background-color: #F3F3F3;
    transition: 0.4s;
  }
  .view.login .login-form .form-inner input[type=text]::placeholder {
    color: #888;
    transition: 0.4s;
  }
  .view.login .login-form .form-inner input[type=submit] {
    appearance: none;
    border: none;
    outline: none;
    background: none;
    display: block;
    width: 100%;
    padding: 10px 15px;
    background-color: #21b326;
    border-radius: 8px;
    color: #FFF;
    font-size: 18px;
    font-weight: 700;
  }
  .view.login .login-form .form-inner:focus-within label {
    color: #1fde38;
  }
  .view.login .login-form .form-inner:focus-within input[type=text] {
    background-color: #FFF;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
  }
  .view.login .login-form .form-inner:focus-within input[type=text]::placeholder {
    color: #666;
  }
  .view.chat {
    flex-direction: column;
  }
  .view.chat header {
    position: relative;
    display: block;
    width: 100%;
    padding: 80px 30px 10px;
  }
  .view.chat header .logout {
    position: absolute;
    top: 15px;
    right: 15px;
    appearance: none;
    border: none;
    outline: none;
    background: none;
    color: #FFF;
    font-size: 18px;
    margin-bottom: 10px;
    text-align: right;
  }
  .view.chat header h1 {
    color: #FFF;
  }
  .view.chat .chat-box {
    border-radius: 24px 24px 0px 0px;
    background-color: #FFF;
    box-shadow: 0px 0px 12px rgba(100, 100, 100, 0.2);
    flex: 1 1 100%;
    padding: 12px;    
  }
  .view.chat .chat-box .message {
    display: flex;
    margin-bottom: 13px;
  }
  .view.chat .chat-box .message .message-inner .username {
    color: #888;
    font-size: 16px;
    margin-bottom: 5px;
    padding-left: 15px;
    padding-right: 15px;
  }
  .view.chat .chat-box .message .message-inner .content {
    display: inline-block;
    padding: 10px 20px;
    background-color: #F3F3F3;
    border-radius: 999px;
    color: #333;
    font-size: 14px;
    line-height: 1.2em;
    text-align: left;
  }
  .view.chat .chat-box .message.current-user {
    margin-top: 10px;
    margin-bottom: 10px;
    justify-content: flex-end;
    text-align: right;
  }
  .view.chat .chat-box .message.current-user .message-inner {
    max-width: 75%;
  }
  .view.chat .chat-box .message.current-user .message-inner .content {
    color: #FFF;
    font-weight: 600;
    background-color: #498D6D;
  }
  .view.chat footer {
    position: sticky;
    bottom: 0px;
    background-color: #FFF;
    padding: 0px;
    box-shadow: 0px 0px 12px rgba(100, 100, 100, 0.2);
  }
  .view.chat footer form {
    display: flex;
  }
  .view.chat footer form input[type=text] {
    flex: 1 1 100%;
    appearance: none;
    border: none;
    outline: none;
    background: none;
    display: block;
    width: 100%;
    padding: 10px 15px;    
    color: #333;
    font-size: 18px;
    box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);
   
    transition: 0.4s;
  }
  .view.chat footer form input[type=text]::placeholder {
    color: #888;
    transition: 0.4s;
  }
  .view.chat footer form input[type=submit] {
    appearance: none;
    border: none;
    outline: none;
    background: none;
    display: block;
    padding: 10px 15px;
    border-radius: 20px 20px 20px 20px;
    background-color: #498D6D;
    color: #FFF;
    font-size: 15px;
    font-weight: 700;
    margin-top : 10px;
    margin-bottom: 10px;
    margin-left: 5px;
    margin-right: 3px;
  }
  
.imgProfile {
  width: 30%;
  height: 30%;
  object-fit: cover;
}

#chatprofile {
  width: 35px;
  height: 35px;
  border-radius: 70%;
  overflow: hidden;
  margin-right : 13px
}
</style>