<template>
  <br />
  <h3 v-if="myCrew" style="font-weight: bold">내가 가입한 크루</h3>
  <h3 v-else style="font-weight: bold">
    <b style="color: #498d6d">{{ userNickname }}</b
    >님이 가입한 크루
  </h3>
  <hr />

  <div class="container">
    <div
      v-for="crew in crews"
      :key="crew.crew_pk"
      style="width: 100%"
      @click.prevent="crewDetail(crew.crew_pk)"
    >
      <div
        class="d-flex justify-content-around row"
        @click="crewDetail(crew.crew_pk)"
      >
        <img
          class="col-2"
          style="width: 5rem; height: 3.5rem; border-radius: 50%"
          :src="crew.crew_img"
        />

        <h5 class="col-5 mt-3 mb-0" style="font-weight: bold">
          <b>{{ crew.crew_name }}</b>
        </h5>
        <div
          style="padding: 0%; margin-top: 4%"
          class="col-2 material-symbols-outlined"
        >
          arrow_forward_ios
        </div>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref, computed } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    const crewList = store.state.profile.crewList.results;
    const user_pk = ref(-1);
    for (var i = 0; i < crewList.length; i++) {
      if (crewList[i].user_pk == route.params.user_pk) {
        user_pk.value = i;
        console.log("i : ", user_pk.value);
      }
    }

    const myCrew = computed(() => {
      if (store.state.account.userInfo.user_pk == route.params.user_pk) {
        return true;
      }
      return false;
    });

    const userNickname = ref(null);
    axios
      .get(api.profile.myInfo(route.params.user_pk))
      .then((response) => {
        userNickname.value = response.data.nickname;
      })
      .catch((err) => {
        console.log(err);
      });

    const crews = store.state.profile.crewList.results[user_pk.value].crews;

    const crewDetail = (crew_pk) => {
      router.push({
        name: "crewboardmember",
        params: {
          crew_pk: crew_pk,
        },
      });
    };

    return {
      crewList,
      myCrew,
      userNickname,
      crews,
      crewDetail,
    };
  },
};
</script>

<style></style>
