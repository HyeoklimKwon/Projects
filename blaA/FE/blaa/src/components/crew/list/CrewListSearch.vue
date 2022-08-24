<template>
  <div class="row" id="top_box">
    <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-6" id="top_box_text">크루 검색</h5>
    <div class="col-3" id="top_box_text"></div>
  </div>
  <!-- <label id="search">크루 검색</label> -->
  <input type="text" id="crew_search" name="crew_search" v-model="crew_search" placeholder="검색어를 입력하세요." />

  <div class="row">
    <div class="col-6" id="checkbox" @click="business = true">업무용</div>
    <div class="col-6" id="checkbox" @click="business = false">친목용</div>
  </div>

  <div class="crew_search_list">
    <div v-for="(crew, i) in filtered" :key="i" v-bind="crew">
      <div @click="moveToDetail(crew.crew_pk)">{{ crew.crew_name }}</div>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    let AllCrews = reactive({
      crews: [],
    });
    const crew_search = ref("");
    let business = ref(true);
    let isMember = ref(false);
    const crewMember = ref([]);
    const user_pk = store.state.account.userInfo.user_pk;

    onMounted(() => {
      AllCrews.crews = store.state.crew.AllCrews.results;
    });

    console.log(crew_search);

    const filtered = computed(() => {
      return AllCrews.crews.filter((item) => {
        if (crew_search.value) {
          return item.is_business === business.value && item.crew_name.includes(crew_search.value);
        }
        return item.is_business === business.value;
      });
    });

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
    const back = () => {
      router.go(-1);
    };

    return {
      AllCrews,
      filtered,
      crew_search,
      moveToDetail,
      business,
      back,
    };
  },
};
</script>

<style scoped>
#top_box {
  height: 55px;
  margin: auto;

  color: white;
  background-color: #498d6d;
  border-bottom: 0.5px solid #bdbdbd;
}

#top_box_text {
  /* display: flex; */
  text-align: center;
  line-height: 55px;
}

#crew_search {
  width: 100%;
  height: 50px;

  border-top: none;
  border-left: none;
  border-right: none;

  padding-left: 10px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

#checkbox {
  height: 40px;
  text-align: center;
  line-height: 40px;
  padding: 0;
  margin: auto;
}

.crew_search_list {
  border-top: 1px solid rgba(0, 0, 0, 0.2);
}
</style>
