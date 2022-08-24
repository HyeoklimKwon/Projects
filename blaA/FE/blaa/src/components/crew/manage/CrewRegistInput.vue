<template>
  <div>
    <button v-show="check" @click="moveToBusiness">영업용</button>
    <button v-show="check" @click="moveToFriends">친목용</button>
  </div>
  <!-- <router-view></router-view> -->
  <div v-show="!check">
    <p>Crew 등록</p>
    <form @submit.prevent ="submitForm" enctype="multipart/form-data">
      <label for="crew_name">크루명</label><br />
      <input type="text" id="crew_name" name="crew_name" v-model="crew_name" /><br />
      <label for="crew_explain">크루 설명</label><br />
      <textarea id="crew_explain" name="crew_explain" v-model="crew_explain" cols="35" rows="5"></textarea><br />
      <label for="crew_region">크루 지역</label><br />
      <input type="text" id="crew_region" name="crew_region" v-model="crew_region" />
      <label for="crew_img">크루 이미지</label><br />
      <input type="file" id="crew_img" name="crew_img" @change="previewFile" />
      <button type="submit">등록</button>

      <button @click="moveList">목록</button>
    </form>
  </div>
  <div v-show="!check">
    <button @click="back">뒤로가기</button>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from 'vue';
export default {
  setup() {
    const router = useRouter();
    const store = useStore();
    let check = ref(true);
    let isbusiness = ref(true);
    const crew_name = ref("");
    const crew_explain = ref("");
    const crew_region = ref("");
    const crew_img = ref(null);
    const is_business = ref(false);

    const moveToBusiness = () => {
      check.value = false;
      is_business.value = true;
    };
    const moveToFriends = () => {
      check.value = false;
      is_business.value = false;
    };

    const back = () => {
      check.value=true;
    }

    const submitForm = () => {
      let error = true;
      let msg = "";
      console.log("크루명: " + crew_name.value);
      !crew_name.value && ((msg = "크루명을 입력하세요."), (error = false));
      error && !crew_explain.value && ((msg = "크루 설명을 입력하세요."), (error = false));
      error && !crew_region.value && ((msg = "크루 지역을 입력하세요."), (error = false));

      if (!error) alert(msg);
      else crewRegist();
    };

    const previewFile = (e) => {
      if (e.target.files[0]) {
        crew_img.value = e.target.files[0];
      } else {
        alert('파일을 다시 선택해 주세요')
        crew_img.value = null;
      }
    }

    const crewRegist = async () => {
      console.log(crew_name.value);
      const crewData = new FormData();
      crewData.append("crew_name", crew_name.value);
      crewData.append("crew_explain", crew_explain.value);
      crewData.append("crew_region", crew_region.value);
      crewData.append("crew_img", crew_img.value);
      crewData.append("is_business", is_business.value);

      for (var value of crewData.values()) {
        console.log(value);
      }

      try {
        const token = store.state.crew.Token;
        console.log(token);
        await store.dispatch("crew/registcrew", crewData);
        // if (!store.state.crew.success) alert("등록에 실패하였습니다.");
        // else {
        //   alert("등록에 성공하였습니다.");
        //   moveList();
        // }
        console.log(store.state.crew.success);
      } catch (error) {
        console.log(error);
      }

        
        // console.log(crewData.keys());
        //await store.dispatch("crew/registcrew", crewData);
        //let msg = "등록이 완료되었습니다.";
        //alert(msg);
        //moveList();

      
    };

    const moveList = () => {
      router.push({ name: "allcrewlist" });
    };


    return {
      moveToBusiness,
      moveToFriends,
      check,
      isbusiness,
      back,
      submitForm,
      crew_name,
      crew_explain,
      crew_region,
      crew_img,
      is_business,
      previewFile,
      moveList,
    };
  },
};
</script>

<style></style>
