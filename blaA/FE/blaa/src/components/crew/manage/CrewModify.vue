<template>
  <div>
    <div>크루 수정하기</div>
    {{ crew_name.value }}
    <form @submit.prevent="modifyForm" enctype="multipart/form-data">
      <label for="crew_name">크루명</label><br />
      <input type="text" id="crew_name" name="crew_name" v-model="crew_name" /><br />
      <label for="crew_explain">크루 설명</label><br />
      <textarea id="crew_explain" name="crew_explain" v-model="crew_explain" cols="35" rows="5"></textarea><br />
      <label for="crew_region">크루 지역</label><br />
      <input type="text" id="crew_region" name="crew_region" v-model="crew_region" />
      <label for="crew_img">크루 이미지</label><br />
      <input type="file" id="crew_img" name="crew_img" @change="previewFile" />
      <button type="submit">수정</button>
      <button @click="moveDetail">돌아가기</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
export default {
  setup() {
    const router = useRouter();
    const store = useStore();
    const route = useRoute();
    const crew_name = ref(store.state.crew.crewInfo.crew_name);
    const crew_explain = ref(store.state.crew.crewInfo.crew_explain);
    const crew_region = ref(store.state.crew.crewInfo.crew_region);
    const crew_img = ref(store.state.crew.crewInfo.crew_img);

    const modifyForm = () => {
      let error = true;
      let msg = "";
      console.log("크루명: " + crew_name.value);
      !crew_name.value && ((msg = "크루명을 입력하세요."), (error = false));
      error && !crew_explain.value && ((msg = "크루 설명을 입력하세요."), (error = false));
      error && !crew_region.value && ((msg = "크루 지역을 입력하세요."), (error = false));

      if (!error) alert(msg);
      else crewModify();
    };

    const previewFile = (e) => {
      if (e.target.files[0]) {
        crew_img.value = e.target.files[0];
      } else {
        alert("파일을 다시 선택해 주세요");
        crew_img.value = null;
      }
    };

    const crewModify = async () => {
      console.log(crew_name);
      const crewData = new FormData();
      crewData.append("crew_name", crew_name.value);
      crewData.append("crew_explain", crew_explain.value);
      crewData.append("crew_region", crew_region.value);
      crewData.append("crew_img", crew_img.value);

      try {
        await store.dispatch("crew/modifyCrew", {
          crew_pk: route.params.crew_pk,
          crew: crewData,
        });
      } catch (error) {
        console.log(error);
      }
    };

    const moveDetail = () => {
      router.push({ name: "crewdetail", params: { crew_pk: route.params.crew_pk } });
    };

    return {
      modifyForm,
      crew_name,
      crew_explain,
      crew_region,
      crew_img,
      previewFile,
      moveDetail,
    };
  },
  // setup() {
  //   const store = useStore();
  //   const route = useRoute();
  //   const router = useRouter();
  //   const crewData = reactive({
  //     crew_name: "",
  //     crew_explain: "",
  //     crew_region: "",
  //     // crew_img:"",
  //   });
  //   // const crewData = new FormData();
  //   // crewData.append("crew_name", crew_name);

  //   Object.assign(crewData, store.state.crew.crewInfo);

  //   const checkValue = () => {
  //     let error = true;
  //     let msg = "";
  //     console.log("크루명: " + crewData.crew_name);
  //     console.log("이미지: ", crewData.crew_img);
  //     !crewData.crew_name && ((msg = "크루명을 입력하세요."), (error = false));
  //     error && !crewData.crew_explain && ((msg = "크루 설명을 입력하세요."), (error = false));
  //     error && !crewData.crew_region && ((msg = "크루 지역을 입력하세요."), (error = false));

  //     if (!error) alert(msg);
  //     else modifyCrew();
  //   };

  //   const modifyCrew = async () => {
  //     console.log(route.params.crew_pk, "번째 크루 수정");
  //     await store.dispatch("crew/modifyCrew", {
  //       crew_pk: route.params.crew_pk,
  //       crew: crewData,
  //     });
  //     alert("수정이 완료되었습니다.");
  //     moveDetail();
  //   };

  //   const moveDetail = () => {
  //     router.push({ name: "crewdetail", params: { crew_pk: route.params.crew_pk } });
  //   };

  //   return {
  //     crewData,
  //     checkValue,
  //     modifyCrew,
  //     moveDetail,
  //   };
  // },
};
</script>

<style></style>
