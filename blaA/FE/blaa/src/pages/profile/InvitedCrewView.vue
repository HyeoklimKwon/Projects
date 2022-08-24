<template>
  <div>나를 초대한 크루리스트들</div>
  <div>{{ state.crews[0]}}</div>
  <div v-for="crew in state.crews" :key="crew.id">
        <b-card>
            <b-card-text>
                <div> {{ crew.crew_name }}크루에서 초대를 보내셨습니다. 수락하시겠습니까? </div>
            </b-card-text> 
    <button @click="acceptinvitation(crew.crew)">수락하기</button>
    <button>거절하기</button>
  </b-card>
  </div>
</template>

<script>
import axios from "axios";
import api from "@/api/api.js";
import { useStore } from "vuex";
import router from '@/router';
import { onMounted, reactive  } from "vue";

export default {    
    setup() {
        const refreshAll= (() => {
            // 새로고침
            router.push({
                path: '/crew/list/alllist'
            })
        })
        const store = useStore();
        const userInfo = store.state.account.userInfo;
        const state = reactive({      
            crews: [],    
        })
        onMounted(() => {
            if(userInfo){      
                let token = store.state.chat.token        
                axios.get(api.notification.getinvitedcrewlist(),
                 {
                  headers : {"Authorization": `Bearer ${token}`}
                }).then((response) =>                        
                    state.crews = response.data          
                )                
            }

        })

        const acceptinvitation =  ((crew_pk) => {
            let token = store.state.chat.token
            console.log("들어간크루pk", crew_pk);
            try {
                axios.post(api.crew.acceptcrew(crew_pk),{},{
                      headers : {"Authorization": `Bearer ${token}`}
                    })                  
                    alert("가입이 완료되었습니다! 크루원님의 활발한 활동을 응원합니다")                  
                
            } catch(error) {
                alert("가입에 실패하셨습니다.")
                
            }
        refreshAll()
        })
        
        return {
            state,
            acceptinvitation,
            refreshAll

        }   
    }
}

</script>

<style>

</style>