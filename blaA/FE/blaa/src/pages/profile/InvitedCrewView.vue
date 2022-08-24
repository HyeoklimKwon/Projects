<template>
  <br /><br />
  <div>
    <h5 class="d-flex justify-content-center align-items-center chodaecardtitle"><b>나를 초대한 크루리스트들</b></h5>
  </div>
  <hr />

  <div v-for="crew in state.crews" :key="crew.id">
    <b-card class="chodaecard">
      <div class="d-flex justify-content-center">
        <b-card-text>
          <div v-if="crew.crew_name.length > 6">
            <div>
              <b> {{ crew.crew_name[0] + crew.crew_name[1] + crew.crew_name[2] + crew.crew_name[3] }}...크루에서 초대를 보내셨습니다.</b>
            </div>
          </div>
          <div v-else>
            <div>
              <b>{{ crew.crew_name }}크루에서 초대를 보내셨습니다. </b>
            </div>
          </div>

          <div><b>수락하시겠습니까?</b></div>
        </b-card-text>
        <br />
      </div>
      <div class="d-flex justify-content-center">
        <button class="w-btn-outline w-btn-green-outline" @click="acceptinvitation(crew.crew)">수락하기</button>
        <button class="w-btn-outline w-btn-red-outline" @click="refuseinvitation(crew.crew)">거절하기</button>
      </div>
    </b-card>
    <br />
  </div>
</template>

<script>
import axios from "@/api/axios.js";
import api from "@/api/api.js";
import { useStore } from "vuex";
import router from "@/router";
import { onMounted, reactive } from "vue";

export default {
  setup() {
    const refreshAll = () => {
      // 새로고침
      router.push({
        path: "/crew/list/alllist",
      });
    };
    const store = useStore();
    const userInfo = store.state.account.userInfo;
    const state = reactive({
      crews: [],
    });
    onMounted(() => {
      if (userInfo) {
        axios.get(api.notification.getinvitedcrewlist()).then((response) => (state.crews = response.data));
      }
    });

    const acceptinvitation = (crew_pk) => {
      console.log("들어간크루pk", crew_pk);
      try {
        axios.post(api.crew.acceptcrew(crew_pk), {});
        alert("가입이 완료되었습니다! 크루원님의 활발한 활동을 응원합니다");
      } catch (error) {
        alert("가입에 실패하셨습니다.");
      }
      refreshAll();
    };

    const refuseinvitation = async (crew_pk) => {
      // for (let index = 0; index < state.crews.length; index++) {
      //     if(state.crews[index].crew == crew_pk){
      //         state.crews.splice(index)
      //         break
      //     }
      //     break
      // }
      try {
        await axios
          .post(api.crew.refusecrew(crew_pk), {})
          .then(axios.get(api.notification.getinvitedcrewlist()).then((response) => (state.crews = response.data)));
      } catch (error) {
        console.log(error);
        alert("가입거절에 성공하셨습니다.");
      }
    };

    return {
      state,
      acceptinvitation,
      refreshAll,
      refuseinvitation,
    };
  },
};
</script>

<style>
.w-btn-outline {
  position: relative;
  padding: 15px 30px;
  border-radius: 15px;
  font-family: "paybooc-Light", sans-serif;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  font-weight: 600;
  transition: 0.25s;
  width: 160px;
  height: 60px;
}
.w-btn-green-outline {
  border: 3px solid #77af9c;
  color: #128b37;
  margin-right: 10px;
}
.w-btn-green-outline:hover {
  background-color: #77af9c;
  color: #d7fff1;
}
.w-btn-red-outline {
  border: 3px solid #ff5f2e;
  color: #8b1313;
  margin-left: 5px;
}
.w-btn-red-outline:hover {
  background-color: #ff5f2e;
  color: #e1eef6;
}

.chodaecard {
  border: 1px black solid;
  overflow-y: scroll;
}
</style>
