<template>
  <div
    :class="{
      back_ground_business: crewInfo.is_business,
      back_ground_friends: !crewInfo.is_business,
    }"
  ></div>
  <div class="info_desk">
    <div style="text-align: center; padding: 20px">
      <!-- <div v-if=""></div> -->
      <img class="imgProfile" :src="crewInfo.crew_img" />
      <!-- <img src="@/assets/crew_default1.png" /> -->
    </div>
    <div style="text-align: center">
      <h2 style="margin: 0">{{ crewInfo.crew_name }}</h2>
      <p>{{ crewInfo.crew_region }}</p>
    </div>
    <div class="row" style="margin: auto; text-align: center">
      <div class="col-5" style="padding-left: 40px">
        <!-- <p>{{ crewInfo.created_at }}</p> -->
        <h4>30일</h4>
        <p>내 활동기간</p>
      </div>
      <div class="col-2" style="display: flex; justify-content: center">
        <div class="v-line"></div>
      </div>
      <div class="col-5" @click="moveToMember" style="padding-right: 40px">
        <h5>{{ crewInfo.crew_member_count }}명</h5>
        <p>참여인원</p>
      </div>
    </div>
  </div>
  <br />

  <div style="position: relative; margin-top: 150px">
    <hr />
    <div class="row" style="margin-left: 20px; margin-right: 20px">
      <p id="semi_title_text" style="color: #498d6d">고정 게시물</p>
    </div>

    <div>
      <article-pin></article-pin>
    </div>
    <hr />

    <div class="row" style="margin-left: 20px; margin-right: 20px">
      <p id="semi_title_text" style="color: #498d6d">바로가기</p>
    </div>
    <div class="col" style="margin-left: 20px; margin-right: 20px">
      <div class="buttons" @click="moveToArticle">
        <p class="button_text">게시판</p>
      </div>
      <div class="buttons" @click="moveToCalendar">
        <p class="button_text">스케줄</p>
      </div>
      <div class="buttons" @click="moveToDetail">
        <p class="button_text">크루 정보</p>
      </div>
    </div>

    <!-- <div v-show="isFeed">
      <router-view :isMember="isMember" style="margin: 30px"></router-view>
    </div> -->
  </div>
</template>

<script>
import ArticlePin from "../article/Items/ArticlePin.vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { onMounted, reactive, ref } from "vue";
export default {
  components: {
    ArticlePin,
  },
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const crewInfo = reactive({});

    const user_pk = store.state.account.userInfo.user_pk;
    let isInfo = ref(true);
    let isFeed = ref(false);

    // const getCrewInfo = async () => {
    //   await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
    //   Object.assign(crewInfo, store.state.crew.crewInfo);
    // };

    onMounted(async () => {
      await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
      Object.assign(crewInfo, store.state.crew.crewInfo);
    });

    const crewJoin = async (crew_pk) => {
      await store.dispatch("crew/crewJoin", crew_pk);
    };

    const moveToArticle = () => {
      router.push({ name: "articlelist" });
    };

    const moveToCalendar = () => {
      router.push({ name: "schedule", parmas: { crew_pk: route.params.crew_pk } });
    };

    const moveToDetail = () => {
      router.push({ name: "crewdetail", params: { crew_pk: crewInfo.crew_pk } });
    };

    const moveToMember = () => {
      router.push({ name: "crewmemberlist", params: { crew_pk: crewInfo.crew_pk } });
    };

    // getCrewInfo();

    // const crewMember = (crew_pk) => {
    //   router.push(
    //     { name: "crewmember" },
    //     {
    //       params: {
    //         crew_pk: crew_pk,
    //       },
    //     }
    //   );
    // };

    return {
      crewInfo,
      // getCrewInfo,
      moveToArticle,
      moveToCalendar,
      moveToDetail,
      moveToMember,
      crewJoin,
    };
  },
};
</script>

<style scoped>
* {
  font-family: "Pretendard-Regular";
}

.back_ground_business {
  height: 179px;
  z-index: -1;
  margin: 0;

  background-color: #498d6d;
}

.back_ground_friends {
  height: 179px;
  z-index: -1;

  background-color: #ffcd38;
}

.info_desk {
  position: absolute;
  left: 0;
  right: 0;
  top: 50px;
  margin: auto;
  width: 320px;

  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
  border-radius: 30px;

  /* animation: fadeInUp 1s; */
}

.joinBtn_business {
  display: flex;
  width: 207px;
  height: 30px;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: auto;
  margin-bottom: 20px;

  background: #498d6d;
  color: #ffffff;
  border-radius: 20px;
}

.joinBtn_friends {
  display: flex;
  width: 207px;
  height: 30px;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: auto;
  margin-bottom: 20px;

  background: #ffcd38;
  color: #ffffff;
  border-radius: 20px;
}

.v-line {
  border-left: 0.5px solid #d9d9d9;
  height: 50px;
}

.v-line2 {
  border-left: 0.5px solid #d9d9d9;
  height: 20px;
}

hr {
  margin: 20px;
}

.detail {
  margin: 30px;
}

.imgProfile {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.pin_article {
  height: 150px;
  text-align: center;
  margin-left: 20px;
  margin-right: 20px;

  background-color: #498d6d;
  border-radius: 20px;
}

.buttons {
  height: 60px;
  margin-bottom: 10px;

  background: #f5f5f5;
  border-radius: 20px;
  border: 1px #498d6d;
}

.button_text {
  line-height: 60px;
  margin-left: 30px;
}

#semi_title_text {
  font-weight: 600;
  font-size: 18px;
}

#small_title_text {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 0;
}

/* @keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translate3d(0, 20%, 0);
  }
  to {
    opacity: 1;
    transform: translateZ(0);
  }
} */
</style>
