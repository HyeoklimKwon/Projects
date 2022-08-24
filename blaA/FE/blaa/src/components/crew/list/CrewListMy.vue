<template>
  <!-- <template v-if="myCrewCnt == null">
      <p>가입된 크루가 없습니다.</p>
    </template> -->

  <div class="wrap-vertical">
    <div style="display: flex">
      <div v-for="(crew, i) in myCrews" :key="i">
        <div class="crew_border" @click="moveToDetail(crew.crew_pk)">
          <div class="crew_info" style="display: flex; align-items: center; justify-content: center">
            <div>
              <img class="crew_img" :src="crew.crew_img" />
              <p id="small_title_text" style="white-space: normal">{{ crew.crew_name }}</p>
            </div>
            <!-- <div>
                <p class="text_crew_name" >{{crew.crew_name}}</p>
              </div> -->
          </div>

          <div class="row" id="small_text" style="margin-top: 5px">
            <div class="col" style="text-align: center">
              <img class="member_icon" src="@/assets/icons/person.png" style="margin-bottom: 2px" />
              {{ crew.crew_member_count }}
              &nbsp;&nbsp;| &nbsp; {{ crew.is_business ? "업무용" : "친목용" }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const myCrews = ref([]);
    const myCrewCnt = ref(null);
    const user_pk = store.state.account.userInfo.user_pk;
    const crewMember = ref([]);
    let business = ref(true);
    let isMember = ref(false);
    const host = "https://i7b209.p.ssafy.io/";

    myCrews.value = store.state.account.userInfo.crew.results[0].crews;
    console.log(myCrews.value);

    const moveToDetail = async (crew_pk) => {
      await store.dispatch("crew/getCrewMembers", crew_pk);

      Object.assign(crewMember.value, store.state.crew.members);
      if (crewMember.value.length > 0) {
        for (var i = 0; i < crewMember.value.length; i++) {
          if (crewMember.value[i].user_pk == user_pk) {
            isMember.value = true;
            break;
          }
        }
      }
      console.log(isMember.value);
      if (isMember.value) {
        router.push({ name: "crewboardmember", params: { crew_pk: crew_pk } });
      } else if (!isMember.value) {
        router.push({ name: "crewboardnonmember", params: { crew_pk: crew_pk } });
      }
    };

    return {
      myCrews,
      myCrewCnt,
      moveToDetail,
    };
  },
};
</script>

<style scoped>
.crew_border {
  padding: 10px;
  margin: 10px;
  background: #ffffff;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
  border-radius: 20px;
}

.crew_img {
  width: 100px;
  height: 100px;
  margin-bottom: 10px;
  object-fit: cover;
  border-radius: 50%;
}
.crew_info {
  display: inline-block;
  width: 150px;
  height: 150px;
  text-align: center;
  word-break: break-all;

  /* border: 1px solid black; */
}
.text_crew_name {
  width: 150px;
  height: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.wrap-vertical {
  width: 100%;
  overflow: scroll;
  /* color: #112031;
  background: #F0D9FF;
  border: 1px solid #000; */
  /* 가로 스크롤 */
  white-space: nowrap;
  overflow-x: scroll;
}

.wrap-vertical::-webkit-scrollbar {
  display: none;
}

#text_line {
  line-height: 0px;
}
</style>
