<template>
  <br /><br />
  <button type="button" @click="myChat">내 채팅목록</button>

  <div id="profile">
    <img id="imgProfile" :src="HOST + userInfo.image" />
  </div>

  <div>
    <h3 style="float: left">{{ userInfo.nickname }}</h3>
    &nbsp;
    <button type="button" @click="updateMyInfo">회원정보 수정</button>
  </div>

  <br />

  <div>
    <table>
      <tr>
        <td rowspan="2" align="center" @click="follower">
          <b>
            {{ follow.followers }}
            <br />
            팔로워
          </b>
        </td>
        &nbsp; &nbsp;
        <td rowspan="2" align="center" @click="following">
          <b>
            {{ follow.followings }}
            <br />
            팔로잉
          </b>
        </td>
      </tr>
    </table>
  </div>

  <hr />
  <div @click="myStory">
    <h5><b>내 스토리</b></h5>
  </div>

  <hr />
  <div @click="myReview">
    <h5><b>내 리뷰</b></h5>
  </div>

  <hr />
  <div @click="myGroup">
    <h5><b>내 그룹</b></h5>
  </div>

  <hr />
  <div @click="myInfo">
    <h5><b>회원정보</b></h5>
  </div>

  <hr />
  <div>
    <h5><b>회원탈퇴</b></h5>
  </div>
  <hr />
</template>

<script>
import { useStore } from "vuex";
import { ref } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";
import router from "@/router/index.js";

export default {
  setup() {
    const store = useStore();

    const HOST = ref("http://localhost:8000");

    const userInfo = store.state.account.userInfo;
    console.log(userInfo);
    console.log("nickname : ", userInfo.nickname);
    console.log("image : ", userInfo.image);

    const follow = ref({
      followers: null,
      followings: null,
    });

    axios
      .get(api.accounts.myInfo(userInfo.user_pk))
      .then((response) => {
        console.log("유저 정보 response : ", response);
        follow.value.followers = response.data.followers;
        follow.value.followings = response.data.followings;
      })
      .catch((err) => {
        console.log("유저정보 에러 : ", err);
      });

    const myChat = () => {
      console.log("내 채팅목록 페이지");
    };

    const updateMyInfo = () => {
      console.log("회원정보 수정");
      router.push({
        name: "updateInfo",
        params: { user_pk: userInfo.user_pk },
      });
    };

    const follower = () => {
      console.log("팔로워 조회");
      router.push({
        name: "followList",
        params: { user_pk: userInfo.user_pk, followType: "follower" },
      });
    };

    const following = () => {
      console.log("팔로잉 조회");
      router.push({
        name: "followList",
        params: { user_pk: userInfo.user_pk, followType: "following" },
      });
    };

    const myStory = () => {
      console.log("내 스토리 조회");
      router.push({ name: "mystory", params: { user_pk: userInfo.user_pk } });
      store.dispatch("profile/getMyStory", userInfo.user_pk);
      console.log("스토리 조회 페이지 이동");
    };

    const myReview = () => {
      console.log("내 리뷰 조회");
      router.push({ name: "myreview", params: { user_pk: userInfo.user_pk } });
    };

    const myGroup = () => {
      console.log("내 크루 조회");
      console.log(userInfo.user_pk);
      router.push({ name: "mycrew", params: { user_pk: userInfo.user_pk } });
    };

    const myInfo = () => {
      console.log("회원정보 조회");
      router.push({ name: "myinfo", params: { user_pk: userInfo.user_pk } });
      axios
        .get(api.accounts.myInfo(userInfo.user_pk))
        .then((data) => {
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      myChat,
      userInfo,
      follow,
      updateMyInfo,
      follower,
      following,
      HOST,
      myStory,
      myReview,
      myGroup,
      myInfo,
    };
  },
};
</script>

<style>
#profile {
  width: 150px;
  height: 150px;
  border-radius: 70%;
  overflow: hidden;
}

#imgProfile {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
