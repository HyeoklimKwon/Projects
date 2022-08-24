<template> 
    <div v-if="userInfo">
        <div>여기는 유저검색페이지입니다!</div>
        <div class="search">
            <input v-model="searchText" type="text" placeholder="닉네임 검색" />
        </div>  
        <div>                     
            <ul class="mylist">
                <li v-for="user in filteredUsers" :key="user.user_pk">                  
                        {{user.nickname}} 
                        <button @click="inviteuser(crew_pk, user.user_pk)">초대하기</button>                     
                        <button @click="gochat(user.user_pk)">채팅하기</button>                                              
                </li>                
            </ul>
        </div>
    </div>
    <div v-else>로그인이 필요합니다.</div>
</template>
<script>
import axios from "axios";
import api from "@/api/api.js";
import { useStore } from "vuex";
import { onMounted, reactive , ref, computed } from "vue";
import router from '@/router';
import { useRoute } from 'vue-router'


export default {
    setup () {
        const store = useStore();
        const route = useRoute();
        const userInfo = store.state.account.userInfo;
        const crew_pk = route.params.crew_pk
        const gochat = (from_userpk) => {
        router.push({ name: 'chat',
        params: {
            from_userpk: from_userpk
        }}
        )
        }
        const searchText = ref('');

        const filteredUsers = computed(() => {
        if (searchText.value) {
            return state.users.filter( user => {
            return user.nickname.includes(searchText.value);
            });
        }
        return state.users.filter(user => {
            return user.nickname.includes("!@#$%")
        });
        });        

        const state = reactive({      
            users: [],    
        })

        onMounted(() => {
            if(userInfo){                
                store.state.chat.token
                axios.get(api.accounts.searchallusers(),
                 {
                  headers : {"Authorization": `Bearer ${store.state.chat.token}`}
                }).then((response) =>                        
                state.users = response.data.results            
                )
                console.log(state.users);
            }

        })
        
        const inviteuser = async (invitingcrew_pk, inviteduser_pk) => {
            const token = sessionStorage.getItem('token')           
            try {
                const result = await axios.post(api.crew.inviteuser(invitingcrew_pk, inviteduser_pk),{},{
                    headers : {
                        "Authorization": `Bearer ${token}`
                    }
                })
                alert(result.data.message);
            } catch(error) {                
                alert(error.response.data.message)
            }
            }    


        return {
            state,
            searchText,
            gochat,
            filteredUsers,
            userInfo,
            crew_pk,
            inviteuser,
        }

        }
        
    }

</script>


<style>
ul.mylist, ol.mylist {
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