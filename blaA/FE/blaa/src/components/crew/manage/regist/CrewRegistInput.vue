<template>
  <div class="container" v-show="check">
    <div>
      <br /><br /><br /><br />
      <div class="title">어떤 용도의 크루가 필요한가요?</div>
    </div>
    <div class="row" style="padding-top: 20px">
      <div class="category1" @click="moveToBusiness">
        <div style="padding: 20px">
          <img src="@/assets/crew_default1.png" width="80" />
        </div>
        <div class="row" style="padding: 10px">
          <span id="title_text" style="padding-top: 5px">업무용</span>
          <span>업무용 크루에서</span>
          <span>공적인 대화만 나눠요!</span>
        </div>
      </div>

      <div><hr style="margin-top: 20px" /></div>

      <div class="category2" @click="moveToFriends">
        <div style="padding: 20px">
          <img src="@/assets/crew_default2.png" width="80" />
        </div>
        <div class="row" style="padding: 10px">
          <span id="title_text" style="padding-top: 5px">친목용</span>
          <span>친목용 크루에서</span>
          <span>친구들과 모임을 즐겨요!</span>
        </div>
      </div>
    </div>
  </div>

  <div v-show="!check && is_business">
    <div class="row" id="top_box_g">
      <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
      <h5 class="col-6" id="top_box_text">업무용 크루</h5>
      <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px">
        <button class="submit-btn" type="submit" form="crewForm">등록</button>
      </div>
    </div>
    <div class="container" style="margin-top: 20px">
      <form id="crewForm" @submit.prevent="submitForm" enctype="multipart/form-data">
        <div style="text-align: center">
          <label class="input_file_button" for="crew_img">
            <img class="profileImg" id="preview-image" src="@/assets/crew_default1.png" />
            <p style="padding-top: 5px; color: #498d6d">크루 이미지</p>
          </label>
          <input type="file" id="crew_img" name="crew_img" @change="previewFile" style="display: none" />
        </div>
        <label for="crew_name">크루명</label><br />
        <input type="text" id="crew_name" name="crew_name" v-model="crew_name" /><br />

        <label for="crew_explain">크루 설명</label><br />
        <textarea id="crew_explain" name="crew_explain" v-model="crew_explain" cols="35" rows="5"></textarea><br />
        <!-- <div class="row">
          <div class="col-8">
            <label for="crew_region">크루 지역</label><br />
            <input type="text" id="crew_region" name="crew_region" v-model="crew_region" disabled />
          </div>
          <div class="col-4" style="display: flex; align-items: end">
            <div class="submit_button3" @click="isModalOpen = true">검색</div>
          </div>
        </div> -->
        <label for="crew_region">크루 지역</label><br />
        <input type="text" id="crew_region" name="crew_region" v-model="crew_region" />
      </form>
    </div>
  </div>

  <div v-show="!check && !is_business">
    <div class="row" id="top_box_y">
      <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
      <h5 class="col-6" id="top_box_text">친목용 크루</h5>
      <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px">
        <button class="submit-btn" type="submit" form="crewForm">등록</button>
      </div>
    </div>
    <div class="container" style="margin-top: 20px">
      <form id="crewForm" @submit.prevent="submitForm" enctype="multipart/form-data">
        <div style="text-align: center">
          <label class="input_file_button" for="crew_img">
            <img class="profileImg" id="preview-image" src="@/assets/crew_default2.png" />
          </label>
          <input type="file" id="crew_img" name="crew_img" @change="previewFile" style="display: none" />
          <p style="color: #ffcd38">크루 이미지 설정</p>
        </div>
        <label for="crew_name">크루명</label><br />
        <input type="text" id="crew_name" name="crew_name" v-model="crew_name" /><br />

        <label for="crew_explain">크루 설명</label><br />
        <textarea id="crew_explain" name="crew_explain" v-model="crew_explain" cols="35" rows="5"></textarea><br />
        <!-- 
      <label for="crew_region">크루 활동 지역</label><br />
      <input type="text" id="crew_region" name="crew_region" v-model="crew_region" /> -->
      </form>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref, computed } from "vue";
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
      check.value = true;
    };

    const readImage = (input) => {
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        console.log(reader);

        reader.onload = (e) => {
          const previewImage = document.getElementById("preview-image");
          console.log(previewImage);
          previewImage.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
      }
    };

    const submitForm = () => {
      let error = true;
      let msg = "";
      console.log("크루명: " + crew_name.value);
      !crew_name.value && ((msg = "크루명을 입력하세요."), (error = false));
      error && !crew_explain.value && ((msg = "크루 설명을 입력하세요."), (error = false));
      if (!error) alert(msg);
      else crewRegist();
    };
    const previewFile = (e) => {
      if (e.target.files[0]) {
        crew_img.value = e.target.files[0];
        readImage(e.target);
      } else {
        alert("파일을 다시 선택해 주세요");
        crew_img.value = null;
      }
    };
    const crewRegist = async () => {
      const crewData = new FormData();
      crewData.append("crew_name", crew_name.value);
      crewData.append("crew_explain", crew_explain.value);
      crewData.append("crew_region", crew_region.value);
      crewData.append("crew_img", crew_img.value);
      crewData.append("is_business", is_business.value);
      try {
        console.log(crewData);
        await store.dispatch("crew/registcrew", crewData);
        await store.dispatch("account/getMyCrewList", store.state.account.userInfo.user_pk);

        // store.commit("account/ADD_NEW_CREW", crewData);
      } catch (error) {
        console.log(error);
      }
    };
    const moveList = () => {
      router.push({ name: "crewlist" });
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

<style scoped>
.title {
  margin-left: 15px;

  font-weight: 800;
  font-size: 20px;
}

#top_box_y {
  height: 55px;
  margin: auto;

  color: white;
  background-color: #ffcd38;
  border-bottom: 0.5px solid #bdbdbd;
}

#top_box_g {
  height: 55px;
  margin: auto;

  color: white;
  background-color: #498d6d;
  border-bottom: 0.5px solid #bdbdbd;
}

.category1 {
  display: flex;
  /* width: 150px; */
  width: 90%;
  height: 200px;
  margin: auto;
  /* justify-content: center; */
  align-items: center;
  /* text-align: center; */
  /*
  background-color: #498d6d;
  color: #ffcd38; */
  /* border-radius: 100px; */

  padding: 10px;
  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
  border-radius: 20px;

  position: relative;
  /* animation: fadeInUp 1s; */
}
.category2 {
  display: flex;
  width: 90%;
  height: 200px;
  margin: auto;
  /* justify-content: center; */
  align-items: center;
  /* text-align: center; */
  /*
  background-color: #ffcd38;
  color: #498d6d; */
  /* border-radius: 100px; */
  padding: 10px;
  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
  border-radius: 20px;

  position: relative;
  /* animation: fadeInUp 1s; */
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  to {
    opacity: 1;
    transform: translateZ(0);
  }
}

#crew_name,
#crew_region {
  box-sizing: border-box;
  /* Auto layout */

  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 12px 16px;
  gap: 8px;

  width: 100%;
  height: 48px;

  /* Neutral/Light/Darkest */

  border: 1px solid #c5c6cc;
  border-radius: 12px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}
#crew_explain {
  /* Field */

  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 12px 16px;
  gap: 8px;

  width: 100%;
  height: 97px;

  /* Neutral/Light/Darkest */

  border: 1px solid #c5c6cc;
  border-radius: 12px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.input_file_button {
  border-radius: 75px;
  color: white;
  cursor: pointer;

  width: 102px;
  height: 102px;

  align-items: center;
}

.submit_button1 {
  display: inline-block;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 10px 24px;
  margin: auto;
  /* gap: 10px; */

  width: 100px;
  background: #498d6d;
  color: #ffcd38;
  border-radius: 100px;
  border: 0px;
}

.submit_button2 {
  display: inline-block;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 10px 24px;
  margin: auto;
  /* gap: 10px; */

  width: 100px;
  background: #ffcd38;
  color: #498d6d;
  border-radius: 100px;
  border: 0px;
}

.submit_button3 {
  display: inline-block;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 10px 24px;
  margin: auto;
  /* gap: 10px; */

  width: 80px;
  background: #498d6d;
  color: #ffcd38;
  border-radius: 100px;
  border: 0px;
}

.profileImg {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
