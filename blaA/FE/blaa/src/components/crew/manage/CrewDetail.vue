<template>
  <div>
    <div>{{ crewInfo.crew_name }}의 CREW DETAIL</div>
    <div>
      <img class="crew_img" :src="crewInfo.crew_img" />
      <li>크루 생성일 : {{ crewInfo.created_at }}</li>
      <li>크루 소개 : {{ crewInfo.crew_explain }}</li>
      <li>크루 인원수 : {{ crewInfo.crew_member_count }}</li>
      <li>크루 지역 : {{ crewInfo.crew_region }}</li>
      <li>크루장: {{ crewInfo.crew_leader }}</li>
      <li @click="leaveCrew" style="color: red">크루 탈퇴</li>
      <hr />
      <p>크루장만 접근 가능</p>
      <li @click="modiCrew" style="color: blue">크루 정보 수정</li>
      <li @click="delCrew" style="color: red">크루 삭제</li>
      <hr />
    </div>
  </div>
</template>

<script>
import { reactive } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();

    const crewInfo = reactive({
      crew_pk: "",
      crew_name: "",
      crew_explain: "",
      crew_region: "",
      crew_img: "",
      crew_member_count: "",
      created_at: "",
    });

    const getCrew = async () => {
      console.log(route.params.crew_pk);
      await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
      Object.assign(crewInfo, store.state.crew.crewInfo);
    };

    const delCrew = () => {
      if (confirm("크루를 삭제하시겠습니까?")) {
        router.replace({
          name: "crewdelete",
          params: { crew_pk: crewInfo.crew_pk },
        });
      }
    };

    const leaveCrew = () => {
      if (confirm("크루를 탈퇴하시겠습니까?")) {
        router.replace({
          name: "crewleave",
          params: { crew_pk: crewInfo.crew_pk },
        });
      }
    };

    const modiCrew = () => {
      router.push({ name: "crewmodify", params: { crew_pk: crewInfo.crew_pk } });
    };

    getCrew();

    return {
      getCrew,
      crewInfo,
      delCrew,
      modiCrew,
      leaveCrew,
    };
  },
};
</script>

<style scoped>
.crew_img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
