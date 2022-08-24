<template>
  <div class="nav">
    <div class="page-change">
      <router-link :to="{ name: 'story' }" :class="{ activate: isStory, deactivate: isFollow }" style="font-weight: 700">오출완</router-link>
      <router-link :to="{ name: 'followStory' }" :class="{ activate: isFollow, deactivate: isStory }" style="font-weight: 700">팔로우</router-link>
    </div>
    <div style="display: flex">
      <div class="notification">
        <div v-if="state.isUnread">
          <div class="position-relative" @click="gotonotification">
            <img src="@/assets/icons/bell.png" />
            <span class="position-absolute top-0 start-100 translate-middle p-1 bg-light border-light rounded-circle">
              <span class="visually-hidden">New alerts</span>
            </span>
          </div>
          <!-- <span @click="gotonotification" class="material-symbols-outlined"> notification_important </span> -->
        </div>
        <div v-else>
          <div v-if="state.notifications.length != 0">
            <!-- <span @click="gotonotification" class="material-symbols-outlined"> notifications_active </span> -->
            <div @click="gotonotification">
              <img src="@/assets/icons/bell.png" />
            </div>
          </div>
          <div v-else>
            <!-- <span @click="gotonotification" class="material-symbols-outlined"> notifications </span> -->
            <div @click="gotonotification">
              <img src="@/assets/icons/bell.png" />
            </div>
          </div>
        </div>
      </div>
      <div class="alpha-feature">
        <div class="plus-btn" @click="change" v-if="isStory">
          <!-- <span class="material-symbols-outlined" style="font-size: 32px" @click="isSearch = !isSearch">search</span> -->
          <img src="@/assets/icons/search.png" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, ref } from "vue";
import { useStore } from "vuex";
import axios from "@/api/axios.js";
import api from "@/api/api.js";
import router from "@/router";
import { onClickOutside } from "@vueuse/core";
export default {
  components: {},
  props: {
    isStory: Boolean,
    isFollow: Boolean,
    isFilter: Boolean,
  },
  setup(props, { emit }) {
    const change = () => {
      emit("change");
    };

    let isModalOpen = ref(false);
    const modal = ref(null);
    const store = useStore();

    const userInfo = store.state.account.userInfo;
    const state = reactive({
      notifications: [],
      isUnread: "",
    });
    onClickOutside(modal, () => (isModalOpen.value = false));

    onMounted(() => {
      if (userInfo) {
        axios.get(api.notification.getnotifications()).then((response) => {
          state.notifications = response.data.results;
          for (let index = 0; index < state.notifications.length; index++) {
            const element = state.notifications[index];
            if (element.view == false) {
              state.isUnread = true;
              break;
            }
          }
        });
      }
    });

    const clicknotification = (notification) => {
      if (notification.type == "crew_invite") {
        router.push({ name: "invitedcrewlist" });
      } else if (notification.type == "follow") {
        router.push({
          name: "userProfile",
          params: {
            user_pk: notification.redirect_pk,
          },
        });
      } else if (notification.type == "story") {
        router.push({
          name: "detailStory",
          params: {
            story_pk: notification.redirect_pk,
          },
        });
      } else if (notification.type == "crew") {
        console.log("accpet_crew");
        router.push({
          name: "crewboard",
          params: {
            crew_pk: notification.redirect_pk,
          },
        });
      }
    };

    const deleteclicknotification = (notification_pk) => {
      axios.delete(api.notification.deletenotification(notification_pk));
    };

    const acceptinvitation = (crew_pk) => {
      console.log("들어간크루pk", crew_pk);
      try {
        axios.post(api.crew.acceptcrew(crew_pk), {});
        alert("가입이 완료되었습니다! 크루원님의 활발한 활동을 응원합니다");
      } catch (error) {
        alert("가입에 실패하셨습니다.");
      }
      refreshAll();
    };

    const refreshAll = () => {
      // 새로고침
      router.push({
        path: "/crew/list/alllist",
      });
    };

    const refuseinvitation = async (crew_pk) => {
      try {
        await axios
          .post(api.crew.refusecrew(crew_pk), {})
          .then(axios.get(api.notification.getinvitedcrewlist()).then((response) => (state.crews = response.data)));
      } catch (error) {
        alert("가입거절에 성공하셨습니다.");
      }
    };

    const gotonotification = () => {
      router.push({ name: "notifications" });
    };

    return {
      change,

      isModalOpen,
      modal,
      onClickOutside,
      state,
      clicknotification,
      deleteclicknotification,
      acceptinvitation,
      refuseinvitation,
      gotonotification,
    };
  },
};
</script>

<style scoped>
.nav {
  display: flex;
  justify-content: space-between;
}

.page-change > a {
  text-decoration: none;
  margin-right: 0.5rem;
  font-size: 1.5rem;
}
.alpha-feature {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.5rem;
  height: 32px;
}

.plus-btn {
  display: inline-block;
  margin-right: 5px;
  height: 32px;
}

.fa-plus {
  color: black;
}

.activate {
  color: white;
}

.deactivate {
  color: #2e634a;
}
</style>
