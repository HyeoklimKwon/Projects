<template>
  <div>
    <div>{{ crewInfo.crew_name }}의 CREW DETAIL</div>
    <div>
      <img :src="crewInfo.crew_img" />
      <li>크루 생성일 : {{ crewInfo.created_at }}</li>
      <li>크루 소개 : {{ crewInfo.crew_explain }}</li>
      <li>크루 인원수 : {{ crewInfo.crew_member_count }}</li>
      <li>크루 지역 : {{ crewInfo.crew_region }}</li>
      <li>크루장</li>
      <div @click="modcrew">
        <li style="color: blue">크루 정보 수정</li>
      </div>
      <div @click="delcrew">
        <li style="color: red">크루 삭제</li>
      </div>
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

    const delcrew = () => {
      if (confirm("크루를 삭제하시겠습니까?")) {
        router.replace({
          name: "crewdelete",
          params: { crew_pk: crewInfo.crew_pk },
        });
      }
    };
    const modcrew = () => {
      router.push({ name: "crewmodify", params: { crew_pk: crewInfo.crew_pk } });
    };

    getCrew();

    return {
      getCrew,
      crewInfo,
      delcrew,
      modcrew,
    };
  },
};
</script>

<style></style>
