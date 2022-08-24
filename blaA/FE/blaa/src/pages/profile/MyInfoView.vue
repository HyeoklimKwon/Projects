<template>
  <!-- <div id="myInfo"> -->
  <!-- <div id="myInfo-header">
    <img src="@/img/back.png" @click="back" />
    <h2 id="myInfo-text">회원정보</h2>
  </div> -->

  <div class="row" id="top_box">
    <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-6" id="top_box_text">회원 정보</h5>
    <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px">
      <!-- <button class="submit-btn" @click="sumbitReview">등록</button> -->
    </div>
  </div>

  <div>
    <!-- <br /> -->
    <div class="myInfo-list" style="margin-top: 20px">
      <b class="myinfo">이메일</b>
      <p>{{ myInfo.email }}</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">이름</b>
      <p>{{ myInfo.name }}</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">닉네임</b>
      <p>{{ myInfo.nickname }}</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">전화번호</b>
      <p>{{ myInfo.tel }}</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">알바여부</b>
      <p v-if="myInfo.is_alba">예</p>
      <p v-else>아니오</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">카테고리</b>
      <p>{{ myInfo.category }}</p>
    </div>
    <hr />

    <div class="myInfo-list">
      <b class="myinfo">지역</b>
      <p>{{ myInfo.region }}</p>
    </div>
    <hr />

    <br />
  </div>

  <div class="d-block text-center">
    <button class="btnUpdate" @click="updateMyInfo">회원정보 수정</button>
    &nbsp;
    <button class="btnUpdate" @click="updatePassword">비밀번호 변경</button>
  </div>
  <br />
  <div class="d-block text-center">
    <button @click.prevent="logout">로그아웃</button> &nbsp;
    <button @click.prevent="deleteAccount">회원 탈퇴</button>
  </div>
  <!-- </div> -->
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { kakaoLogout, deleteKakaoAccount } from "@/hooks/kakaologin.js";
import { useCookies } from "vue3-cookies";

export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const { cookies } = useCookies();

    const back = () => {
      router.go(-1);
    };

    const logout = async () => {
      router.replace("/");

      if (store.state.account.kakaoLogin) {
        console.log("kakao getaccesstoken : ", window.Kakao.Auth.getAccessToken());
        await kakaoLogout();
        cookies.remove("access-token");
        cookies.remove("refresh-token");
      }

      store.commit("account/USER_INFO", null);
      store.commit("account/SET_LOGIN_TOKEN", null);
      store.commit("account/LOGIN", false);
      store.commit("account/KAKAO_LOGIN", false);

      sessionStorage.clear();
    };

    const myInfo = store.state.account.userInfo;
    console.log("myInfo : ", myInfo);
    console.log("is_alba: ", myInfo.is_alba);

    const updateMyInfo = async () => {
      console.log("회원정보 수정");
      router.push({
        name: "updateInfo",
        params: { user_pk: route.params.user_pk },
      });
    };

    const updatePassword = () => {
      router.push({
        name: "updatePassword",
        params: {
          user_pk: route.params.user_pk,
        },
      });
    };

    const deleteAccount = () => {
      if (store.state.account.kakaoLogin) {
        deleteKakaoAccount();
        cookies.remove("access-token");
        cookies.remove("refresh-token");
      }
      router.push({
        name: "deleteAccount",
        params: { user_pk: route.params.user_pk },
      });
    };

    return {
      back,
      myInfo,
      logout,
      updateMyInfo,
      updatePassword,
      deleteAccount,
    };
  },
};
</script>

<style scoped>
#myInfo {
  padding-top: 20px;
}

#myInfo-header {
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  width: 25px;
  height: 25px;
  left: 25px;
  top: 25px;
  margin-left: 20px;
}

#myInfo-text {
  width: 100%;
  height: 30px;
  left: 45px;
  top: 27px;

  font-family: "Lato";
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 30px;

  align-items: center;
  text-align: center;
}

.myInfo-list {
  height: 50px;
  padding-left: 20px;
  padding-right: 20px;
  line-height: 50px;
}

b {
  /* font-family: "Inter"; */
  font-style: normal;
  font-weight: 800;
  font-size: 18px;
}

p {
  float: right;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
}

button {
  /* position: absolute; */
  width: 120px;
  height: 40px;
  bottom: 5px;
  right: 5px;
  border-radius: 100px;
  background-color: #eec95c;
  /* border: 2px solid #eec95c; */
  background-color: #ffffff;
  font-weight: bold;
  color: #000000;

  font-size: 12px;
}
</style>
