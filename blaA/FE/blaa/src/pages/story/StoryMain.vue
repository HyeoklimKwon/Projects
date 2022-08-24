<template>
  <button @click="isModalOpen = true">임시알림버튼</button>
  <div class="black-bg" v-if="isModalOpen">
    <div class="white-bg" ref="modal">
      <h4>알림창임</h4>
      <div v-for="(notification, i) in state.notifications" :key="i">        
          <b-card >       
            <b-card-text>
              <!-- <div>
                {{notification}}
              </div> -->
              <div @click="clicknotification(notification)">
                {{ notification.content }}
              </div>
              <div v-if= notification.view>읽음</div>
              <div v-else>안 읽음</div>
            </b-card-text>
          </b-card>
      </div>
      <button @click="isModalOpen = false" class="close-btn">close</button>
    </div>

  </div>


  <router-view></router-view>

</template>

<script>
import { onMounted, reactive , ref } from 'vue'
import { useStore } from 'vuex'
import axios from "axios";
import api from "@/api/api.js";
import router from '@/router';
import { onClickOutside } from '@vueuse/core'
export default { 
  
  setup () {
    const isModalOpen = ref(false)
    const modal = ref(null)   
    const store = useStore()
    
    const userInfo = store.state.account.userInfo;
    const state = reactive({      
            notifications: [],    
        })
    onClickOutside(modal, () => (isModalOpen.value = false))    

    onMounted(() => {
          if(userInfo){                
              const token = store.state.story.Token
                    axios.get(api.notification.getnotifications(),{
                    headers : {
                      "Authorization": `Bearer ${token}`
                    }}).then((response) =>                        
                    state.notifications = response.data.results                    
              )  
                       
          }
      })

    const clicknotification = ((notification) => {
      if (notification.type == "crew_invite") {
        router.push({name : 'invitedcrewlist'})
        
      } else if (notification.type == "follow") {
        console.log("this is follow");
      } else if (notification.type == "story") {
        console.log("this is story");
      } else if (notification.type == "accept_crew"){
        console.log("accepted crew invite");
      }

    })

    
    
    return {
      isModalOpen,
      modal,
      onClickOutside,
      state,
      clicknotification
      
    }
    
  }

}
</script>

<style>
body {
  margin: 0
}
div {
  box-sizing: border-box;
}
.black-bg {
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding:20px;

}
.white-bg {
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
}


</style>