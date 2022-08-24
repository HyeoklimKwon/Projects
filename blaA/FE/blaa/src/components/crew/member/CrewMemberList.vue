<template>
  <div>
    <div>크루 멤버 입니다.</div>
    <table>
      <thead>
        <th>번호</th>
        <th>닉네임</th>
      </thead>
      <tbody>
        <tr v-for="(member, i) in All.members" :key="i" v-bind="member">
          <td>{{ member.user_pk }}</td>
          <td>{{ member.nickname }}</td>
        </tr>
      </tbody>
    </table>
    <button v-show="leader" @click="moveToRequestList">신청 목록</button>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { reactive, ref } from "vue";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const All = reactive({
      members: [],
    });
    let leader = ref(null);

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

    getMembers();
    isLeader();

    console.log(All);
    return {
      All,
      moveToRequestList,
      isLeader,
      leader,
    };
  },
};
</script>

<style></style>
