<template>
  <div class="row" id="top_box">
    <div class="col-2" id="top_box_text"></div>
    <h5 class="col-8" id="top_box_text">크루</h5>
    <div class="col-2" id="top_box_text" @click="moveListSearch">
      <img src="@/assets/icons/search.png" />
    </div>
  </div>
  <div class="container">
    <div class="row" style="margin-top: 20px; text-align: center">
      <div class="col-8" id="title_text" style="display: flex; align-items: center; font-size: 16px">새로운 크루를 만들어봐요! 💫</div>
      <div class="col-4">
        <div class="newCrewBtn" @click="createCrew">
          <p id="small_title_text">+ 만들기</p>
        </div>
      </div>
    </div>
  </div>
  <hr />
  <div class="container">
    <div class="row">
      <div class="col-8" id="semi_title_text">내 크루</div>
      <div class="col-4" style="text-align: right">더보기</div>
    </div>
  </div>
  <crew-list-my style="padding: 10px"></crew-list-my>
  <hr />
  <div class="container">
    <div class="row">
      <div class="col-8" id="semi_title_text">전체 크루</div>
      <div class="col-4" style="text-align: right">더보기</div>
    </div>
  </div>
  <crew-list-all></crew-list-all>
</template>

<script>
import CrewListAll from "@/components/crew/list/CrewListAll.vue";
import CrewListMy from "@/components/crew/list/CrewListMy.vue";
import { useRouter } from "vue-router";
export default {
  components: {
    CrewListAll,
    CrewListMy,
  },
  setup() {
    const router = useRouter();

    const createCrew = () => {
      router.push({ name: "crewregist" });
    };
    const moveAllList = () => {
      router.push({ name: "allcrewlist" });
    };
    // const moveMyList = () => {
    //   router.push({ name: "mycrewlist" });
    // };

    const moveListSearch = () => {
      router.push({ name: "crewsearch" });
    };

    return {
      createCrew,
      moveAllList,
      // moveMyList,
      moveListSearch,
    };
  },
};
</script>

<style>
.newCrewBtn {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;

  width: 80%;
  height: 40px;
  left: 107px;
  right: 107px;
  top: 600px;

  background: #eec95c;
  border-radius: 100px;
  color: #498d6d;
}
</style>
