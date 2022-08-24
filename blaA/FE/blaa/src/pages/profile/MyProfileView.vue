<template>
  <br /><br />

  <!-- <div id="profile">
    <img class="imgProfile" :src="HOST + userInfo.image" />
  </div> -->
  <div class="image-upload" style="border: 3px solid; text-align: center; margin: auto" id="profile">
    <label for="update-profileImg">
      <img class="imgProfile" :src="HOST + userInfo.image" />
    </label>

    <input id="update-profileImg" class="update-profileImg" @change="updateProfileImg" type="file" style="display: none" />
  </div>
  <h4 class="mt-3 mb-2" style="text-align: center; font-weight: bold">
    {{ userInfo.nickname }}
  </h4>

  <div class="d-flex justify-content-center">
    <table>
      <tr>
        <td rowspan="4" align="center" @click="follower">
          <div style="margin-right: 0.5rem">
            <b style="font-size: 1.2rem">
              {{ follow.followers }}
              <br />
              <p>팔로워</p>
            </b>
          </div>
        </td>
        &nbsp; &nbsp;
        <td rowspan="4" align="center" @click="following">
          <div style="margin-left: 0.5rem">
            <b style="font-size: 1.2rem">
              {{ follow.followings }}
              <br />
              <p>팔로잉</p>
            </b>
          </div>
        </td>
      </tr>
    </table>
  </div>

  <!-- <button @click.prevent="gochatroom">채팅하러가기</button> -->
  <!-- <button @click="showinvitedcrewlist">나를초대한크루리스트</button> -->
  <div class="container">
    <hr style="margin-top: 0rem" />
    <div>
      <div @click.prevent="gochatroom">
        <h5 id="title_text" class="profile_list"><b>내 채팅창</b></h5>
      </div>
      <hr />
      <div @click="myStory">
        <h5 id="title_text" class="profile_list"><b>내 스토리</b></h5>
      </div>

      <hr />
      <div @click="myReview">
        <h5 id="title_text" class="profile_list"><b>내 리뷰</b></h5>
      </div>

      <hr />
      <div @click="myCrew">
        <h5 id="title_text" class="profile_list"><b>내 크루</b></h5>
      </div>

      <hr />
      <div @click="showinvitedcrewlist">
        <h5 id="title_text" class="profile_list"><b>초대받은 크루</b></h5>
      </div>

      <hr />
      <div @click="myInfo">
        <h5 id="title_text" class="profile_list"><b>회원정보</b></h5>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { ref, computed } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();

    const HOST = ref("https://i7b209.p.ssafy.io");

    const userInfo = computed(() => {
      return store.state.account.userInfo;
    });

    console.log(userInfo);
    console.log("nickname : ", userInfo.value.nickname);
    console.log("image : ", userInfo.value.image);

    const gochatroom = () => {
      router.push({ path: "/chatroom" });
    };
    const follow = ref({
      followers: null,
      followings: null,
    });

    axios
      .get(api.accounts.myInfo(userInfo.value.user_pk))
      .then((response) => {
        console.log("유저 정보 response : ", response);
        follow.value.followers = response.data.followers;
        follow.value.followings = response.data.followings;
      })
      .catch((err) => {
        console.log("유저정보 에러 : ", err);
      });

    const profileImg = ref(null);
    const imgURL = ref("");

    // 업로드 된 이미지를 미리 확인하는 함수
    const updateProfileImg = (e) => {
      const preview = document.querySelector(".imgProfile");
      if (e.target.files[0]) {
        profileImg.value = e.target.files[0];
        const reader = new FileReader();

        // 파일명을 가져와서 소문자로 변환
        let fileName = profileImg.value.name.substring(profileImg.value.name.lastIndexOf(".") + 1);
        fileName = fileName.toLowerCase();

        // 파일 형식과 3MB의 파일크기 확인
        if (
          ["jpeg", "png", "gif", "bmp", "jpg"].includes(fileName) &&
          profileImg.value.size <= 25165824
        ) {
          reader.onload = (e) => {
            preview.src = e.target.result;
            imgURL.value = e.target.result;
          };
          reader.readAsDataURL(profileImg.value);

          console.log("userInfo value : ", userInfo);
          const updateImg = {
            name: userInfo.value.name,
            nickname: userInfo.value.nickname,
            region: userInfo.value.region,
            category: userInfo.value.category,
            is_alba: userInfo.value.is_alba,
            tel: userInfo.value.tel,
            image: profileImg.value,
          };

          try {
            axios
              .put(api.profile.myInfo(userInfo.value.user_pk), updateImg, {
                headers: {
                  "Content-type": "multipart/form-data",
                },
              })
              .then(async (response) => {
                console.log("변경 후 data ", response.data);
                store.commit("account/USER_INFO", response.data);
                await store.dispatch(
                  "account/getMyCrewList",
                  userInfo.value.user_pk
                );
                // const res = sessionStorage.getItem("vuex");
                // console.log("sessionStorage : ", res);
                alert("사진 변경 완료");
              });
          } catch (err) {
            console.log(err);
          }

          // 파일 업데이트 요청 보내기
        } else if (profileImg.value.size <= 25165824) {
          preview.src = null;
        } else {
          alert("파일을 다시 선택해 주세요");
          profileImg.value = null;
          preview.src = null;
        }
        // 파일을 선택하지 않았을 떄
      } else {
        profileImg.value = null;
        preview.src = null;
      }
    };

    const follower = async () => {
      console.log("팔로워 조회");
      await store.dispatch("profile/getFollowerList", userInfo.value.user_pk);
      router.push({
        name: "followList",
        params: {
          user_pk: userInfo.value.user_pk,
          followType: "follower",
        },
      });
    };

    const following = async () => {
      console.log("팔로잉 조회");
      await store.dispatch("profile/getFollowingList", userInfo.value.user_pk);
      router.push({
        name: "followList",
        params: { user_pk: userInfo.value.user_pk, followType: "following" },
      });
    };

    const myStory = async () => {
      console.log("내 스토리 조회");
      await store.dispatch("profile/getMyStory", userInfo.value.user_pk);
      router.push({
        name: "mystory",
        params: { user_pk: userInfo.value.user_pk },
      });
      console.log("스토리 조회 페이지 이동");
    };

    const myReview = async () => {
      console.log("내 리뷰 조회");
      await store.dispatch("profile/getReviewList", userInfo.value.user_pk);
      router.push({
        name: "reviewList",
        params: { user_pk: userInfo.value.user_pk },
      });
    };

    const myCrew = async () => {
      console.log("내 크루 조회");
      await store.dispatch("profile/getCrewList", userInfo.value.user_pk);
      router.push({
        name: "crewList",
        params: { user_pk: userInfo.value.user_pk },
      });
    };

    const myInfo = () => {
      console.log("회원정보 조회");
      router.push({
        name: "myinfo",
        params: { user_pk: userInfo.value.user_pk },
      });
    };

    const showinvitedcrewlist = () => {
      router.push({ name: "invitedcrewlist" });
    };

    return {
      userInfo,
      follow,
      profileImg,
      imgURL,
      updateProfileImg,
      follower,
      following,
      HOST,
      myStory,
      myReview,
      myCrew,
      myInfo,
      showinvitedcrewlist,
      gochatroom,
    };
  },
};
</script>

<style>
.imgProfile {
  width: 9.6rem;
  height: 9.6rem;
  object-fit: cover;
}

.profile_list {
  margin-left: 1rem;
  font-weight: bold;
}
</style>
