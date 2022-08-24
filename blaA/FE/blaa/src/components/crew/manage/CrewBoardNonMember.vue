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
        <h4>약 {{ diffTime }}일</h4>
        <p>활동기간</p>
      </div>
      <div class="col-2" style="display: flex; justify-content: center">
        <div class="v-line"></div>
      </div>
      <div class="col-5" @click="moveToMember" style="padding-right: 40px">
        <h5>{{ crewInfo.crew_member_count }}명</h5>
        <p>참여인원</p>
      </div>
    </div>
    <div
      :class="{
        joinBtn_business: crewInfo.is_business,
        joinBtn_friends: !crewInfo.is_business,
      }"
      @click="crewJoin(crewInfo.crew_pk)"
    >
      가입하기
    </div>
  </div>
  <br />
  <div style="position: relative; margin-top: 200px">
    <hr />
    <div class="row" style="text-align: center; margin-left: 30px; margin-right: 30px">
      <div class="col-5" @click="Info">정보</div>
      <div class="col-2" style="display: flex; justify-content: center">
        <div class="v-line2"></div>
      </div>
      <div class="col-5" @click="Feed">피드</div>
    </div>
    <hr />

    <div v-show="isInfo">
      <div class="detail">
        <p id="semi_title_text">우리 크루를 소개합니다!</p>
        <p>
          안녕하세요, {{ crewInfo.crew_name }} 입니다.<br />
          <span>
            {{ crewInfo.crew_explain }}
          </span>
        </p>
      </div>
      <hr />
      <div class="detail">
        <div class="row">
          <p id="semi_title_text">크루장</p>
          <p>{{ crewInfo.crew_leader }}</p>
        </div>
      </div>
    </div>

    <div v-show="isFeed">
      <article-list :isMember="isMember" style="margin: 0"></article-list>
      <!-- <router-view :isMember="isMember" style="margin: 30px"></router-view> -->
    </div>

    <!-- <button @click="moveToArticle">Article</button>
    <button @click="moveToCalendar">Calendar</button>
    <button @click="moveToDetail">크루 정보</button>
    <button @click="moveToMember">사용자</button>
    <router-view></router-view> -->
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { onMounted, reactive, ref } from "vue";
import ArticleList from "@/components/crew/article/ArticleList.vue";
export default {
  components: {
    ArticleList,
  },
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const crewInfo = reactive({});
    const crewMember = ref([]);
    const user_pk = store.state.account.userInfo.user_pk;
    let isInfo = ref(true);
    let isFeed = ref(false);
    let isMember = ref(false);
    var diffTime = ref(null);

    // const getCrewInfo = async () => {
    //   await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
    //   Object.assign(crewInfo, store.state.crew.crewInfo);
    // };
    onMounted(async () => {
      await store.dispatch("crew/getCrewInfo", route.params.crew_pk);
      await store.dispatch("crew/getCrewMembers", route.params.crew_pk);
      // await store.dispatch("")

      Object.assign(crewInfo, store.state.crew.crewInfo);
      Object.assign(crewMember.value, store.state.crew.members);
      if (crewMember.value.length > 0) {
        for (var i = 0; i < crewMember.value.length; i++) {
          if (crewMember.value[i].user_pk == user_pk) {
            isMember.value = true;
            break;
          }
        }
      }

      /* 활동 기간 구하기 */
      const start = new Date();
      const end = new Date(crewInfo.created_at);
      diffTime.value = Math.round((start.getTime() - end.getTime()) / (1000 * 60 * 60 * 24));
    });

    const crewJoin = async (crew_pk) => {
      await store.dispatch("crew/crewJoin", crew_pk);
    };

    const Info = () => {
      isFeed.value = false;
      isInfo.value = true;
    };

    const Feed = () => {
      isInfo.value = false;
      isFeed.value = true;
    };

    const moveToDetail = () => {
      router.push({ name: "crewdetail", params: { crew_pk: crewInfo.crew_pk } });
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
      moveToDetail,
      crewJoin,
      Info,
      Feed,
      isInfo,
      isFeed,
      isMember,
      diffTime,
    };
  },
};
</script>

<style scoped>
.back_ground_business {
  height: 179px;
  z-index: -1;

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

  background-color: #ffffff;
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
  margin: 8px;
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

#semi_title_text {
  font-weight: 600;
  font-size: 18px;
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
