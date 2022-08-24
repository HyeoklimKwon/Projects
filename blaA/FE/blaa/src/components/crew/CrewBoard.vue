<template>
  <div>
    <h2>{{ crewInfo.crew_name }} 의 게시판입니다.</h2>
    <br />
    <p>{{ crewInfo.crew_member_count }} 명 참여중</p>
    <br />
    <button @click="moveToArticle">Article</button>
    <button @click="moveToCalendar">Calendar</button>
    <button @click="moveToDetail">크루 정보</button>
    <button @click="moveToMember">사용자</button>
    <button @click="crewJoin(crewInfo.crew_pk)">가입하기</button>
    <router-view></router-view>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { reactive } from "vue";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const crewInfo = reactive({
      crew_pk: "",
      crew_name: "",
      crew_explain: "",
      crew_region: "",
      // crew_img: "",
      crew_member_count: "",
      created_at: "",
    });

    const getCrewInfo = async () => {
      await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
      Object.assign(crewInfo, store.state.crew.crewInfo);
    };

    const crewJoin = async (crew_pk) => {
      await store.dispatch("crew/crewJoin", crew_pk);
    };

    const moveToArticle = () => {
      router.push({ name: "articlelist" });
    };

    const moveToCalendar = () => {
      router.push({ name: "schedule" });
    };

    const moveToDetail = () => {
      router.push({ name: "crewdetail", params: { crew_pk: crewInfo.crew_pk } });
    };

    const moveToMember = () => {
      router.push({ name: "crewmember", params: { crew_pk: crewInfo.crew_pk } });
    };

    getCrewInfo();

    const crewMember = (crew_pk) => {
      router.push({ name: "crewmember"}, {
        params : {
          crew_pk : crew_pk
        }
      })
    }

    return {
      crewInfo,
      getCrewInfo,
      moveToArticle,
      moveToCalendar,
      moveToDetail,
      moveToMember,
      crewJoin,
    };
  },
};
</script>

<style></style>
