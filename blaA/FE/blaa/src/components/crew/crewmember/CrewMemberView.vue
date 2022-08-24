<template>
  <div>크루맴버보여주기창입니다.</div>
  <div>해당크루의 pk는 {{ crew_pk }}</div>
  <div class="search">
            <input v-model="searchText" type="text" placeholder="닉네임 검색" />
 </div>  
    <div>                     
    <ul class="mylist">
        <li v-for="member in state.members" :key="member.user_pk">                  
            {{ member.nickname }}                                                
            
            <button @click="gochat(member.user_pk)">채팅하기</button>                                                 
            
        </li>                
    </ul>
    <button @click.prevent="gosearch">크루원 초대하기</button>
    </div>


</template>

<script>

import api from "@/api/api.js";
import { useStore } from "vuex";
import { useRoute } from 'vue-router'
import { onBeforeMount, reactive , ref, computed} from "vue";
import axios from 'axios';
import router from "@/router";
export default {
    setup () {
        const store = useStore()
        const route = useRoute()
        const crew_pk = route.params.crew_pk
        const userInfo = store.state.account.userInfo;
        const searchText = ref('');

        const filteredMembers = computed(() => {
        if (searchText.value) {
            return state.members.filter( member => {
            return member.nickname.includes(searchText.value);
            });
        }
        return state.members
        });

        const state = reactive({
            members : [],
        })

        onBeforeMount( async () => {
            if(userInfo) {
                let token = store.state.chat.token
                axios.get(api.crew.crewmemebers(crew_pk),
                {
                    headers : 
                        {"Authorization": `Bearer ${token}`}
                    
                }).then((response) => 
                state.members = response.data.results                
                )
                
            }
        })
        const gosearch = () => {
        router.push({ name: "searchcrewusers" ,
            params : {
                crew_pk : crew_pk
            }
        });
            };

        const gochat = (from_userpk) => {
        router.push({ name: 'chat',
        params: {
            from_userpk: from_userpk
        }}
        )
        } 
    
        return {
            crew_pk,
            state,
            userInfo,
            gochat,
            filteredMembers,
            searchText,
            gosearch
        }


    }


}
</script>

<style>

</style>