<template>  
  <div class="d-flex justify-content-between align-items-center" style="background-color: #498d6d; padding: 30px 10px 10px 10px;">
    <div @click="moveToPrevious"><img src="@/assets/icons/arrow-left.png" alt=""></div>
    <h5 class="chodaecardtitle" style="margin: 0; color:white"><b>알림함</b></h5>
    <div style="width:25px; height:25px"></div>
    </div>     
      <div v-for="(notification, i) in state.notifications" :key="i">           
          <b-card >       
            <b-card-text  @click="clicknotification(notification), isModalOpen = false, deleteclicknotification(notification.pk)"> 
              <div class="noticontent d-flex justify-content-center align-items-center">                              
                <div>
                  &nbsp; 
                </div>
                <div>
                  &nbsp; 
                </div>
                <div>
                  &nbsp; 
                </div>
                <div >
                  {{ notification.content }}
                </div>                                
              </div>               
            </b-card-text>           
          </b-card>
        
      </div>

  
</template>

<script>
import { onMounted, reactive } from 'vue'
import { useStore } from 'vuex'
import axios from "@/api/axios.js";
import api from "@/api/api.js";
import router from '@/router';
export default { 
  
  setup () { 
    const store = useStore()    
    const userInfo = store.state.account.userInfo;
    const state = reactive({      
            notifications: [],
            isUnread : "",    
        })      
    onMounted(async () => {
          if(userInfo){                
                    await axios.get(api.notification.getnotifications()).then((response) => {
                      state.notifications = response.data.results
                      for (let index = 0; index < state.notifications.length; index++) {
                        const element = state.notifications[index];
                        console.log(element);
                        axios.put(api.notification.makeviewtrue(element.pk),{
                            view : true
                        })                     
                      }
                    }                 
                      
              )  
                       
          }
      })
    const clicknotification = ((notification) => {
      if (notification.type == "crew_invite") {
        router.push({name : 'invitedcrewlist'})        
      } else if (notification.type == "follow") {
        router.push({ name : 'userProfile', 
          params : {
            user_pk : notification.redirect_pk
          }
        })
      } else if (notification.type == "story") {
        router.push({name : 'detailStory', 
          params: {
            story_pk: notification.redirect_pk,
        }
        })        
      } else if (notification.type == "crew"){
        console.log("accpet_crew");
        router.push({name : 'mycrewlist'
          
        })
      }

    })

    const typetransformation = (notification) => {
      if (notification.type == "crew_invite") {
        if (notification.content.length > 13) {
          return notification.content.splice(1,5)          
        }
        
      }
    }

    const deleteclicknotification = (notification_pk) => {      
      axios.delete(api.notification.deletenotification(notification_pk))
    }       

    const moveToPrevious = () => {
      router.go(-1)
    }
    
    return {
      state,
      clicknotification,
      deleteclicknotification, 
      typetransformation,
      moveToPrevious         
    }
    
  }

}
</script>

<style>
.noticontent{
  margin-top: 5px;
  margin-bottom: 5px
}
.notiimg{
  width: 70px;
  height : 70px;
  border-radius: 50px;

}
</style>