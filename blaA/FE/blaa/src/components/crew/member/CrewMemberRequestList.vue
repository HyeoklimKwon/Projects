<template>
  <div>크루 가입 신청 명단</div>
  <table>
    <thead>
      <th>유저번호</th>
      <th>닉네임</th>
      <th>업종</th>
    </thead>
    <tbody>
      <tr v-for="(member, i) in list" :key="i" v-bind="member">
        <td>{{ member.user }}</td>
        <td>{{ member.nickname }}</td>
        <td>{{ member.category }}</td>
        <button @click="acceptRequest(member.user)">승인</button>
        <button @click="denyRequest(member.user)">거절</button>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const list = ref([]);

    const getRequestList = async () => {
      await store.dispatch("crew/getRequestList", {
        crew_pk: route.query.crew_pk,
        type: "sign",
      });
      list.value = store.state.crew.requestlist;
    };

    const acceptRequest = async (user) => {
      await store.dispatch("crew/acceptRequest", {
        crew_pk: route.query.crew_pk,
        user_pk: user,
      });
      router.go({
        name: "crewmemberrequestlist",
        query: { crew_pk: route.query.crew_pk },
      });
    };

    const denyRequest = async (user) => {
      await store.dispatch("crew/denyRequest", {
        crew_pk: route.query.crew_pk,
        user_pk: user,
      });
    };

    getRequestList();

    return {
      list,
      acceptRequest,
      denyRequest,
    };
  },
};
</script>

<style></style>
