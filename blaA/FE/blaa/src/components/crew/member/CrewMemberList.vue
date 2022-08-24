<template>
  <div>
    <div class="row" id="top_box">
      <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
      <h5 class="col-6" id="top_box_text">크루 멤버</h5>
      <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px"></div>
    </div>
    <table>
      <thead>
        <th>번호</th>
        <th>닉네임</th>
      </thead>
      <tbody>
        <tr v-for="(member, i) in All.members" :key="i" v-bind="member">
          <td>{{ member.user_pk }}</td>
          <td>{{ member.nickname }}</td>
          <button @click="gochat(member.user_pk)">채팅하기</button>
        </tr>
      </tbody>
    </table>
    <button v-show="leader" @click="moveToRequestList">신청 목록</button>
    <button @click.prevent="gosearch">크루원 초대하기</button>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { onMounted, reactive, ref } from "vue";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const All = reactive({
      members: [],
    });
    let leader = ref(null);

    onMounted(async () => {
      await store.dispatch("crew/getCrewMembers", route.params.crew_pk);
      All.members = store.state.crew.members;
    });

    const getMembers = async () => {
      await store.dispatch("crew/getCrewMembers", route.params.crew_pk);
      All.members = store.state.crew.members.results;
    };

    const moveToRequestList = () => {
      router.push({
        name: "crewmemberrequestlist",
        query: { crew_pk: route.params.crew_pk },
      });
    };

    const isLeader = () => {
      const leader_pk = store.state.crew.crewInfo.crew_leader_pk;
      const user_pk = store.state.account.userInfo.user_pk;
      if (leader_pk == user_pk) leader = true;
    };

    const gosearch = () => {
      router.push({
        name: "searchcrewusers",
        params: { crew_pk: route.params.crew_pk },
      });
    };

    const gochat = (from_userpk) => {
      router.push({
        name: "chat",
        params: {
          from_userpk: from_userpk,
        },
      });
    };

    // getMembers();
    isLeader();

    console.log(All);
    return {
      All,
      moveToRequestList,
      isLeader,
      leader,
      gochat,
      gosearch,
    };
  },
};
</script>

<style></style>
