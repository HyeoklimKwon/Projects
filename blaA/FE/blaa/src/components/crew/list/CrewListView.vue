<template>
  <button @click="moveMyList">내 크루</button>
  <button @click="moveAllList">전체 크루</button>
  <router-view></router-view><br />
  <button @click="createCrew">새 크루 생성하기</button>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  setup() {
    const router = useRouter();

    const createCrew = () => {
      router.push({ name: "crewregist" });
    };
    const moveAllList = () => {
      router.push({ name: "allcrewlist" });
    };
    const moveMyList = () => {
      //router.push("/crew/list/mylist/" + this.user_pk);
    };

    return {
      createCrew,
      moveAllList,
      moveMyList,
    };
  },
};
</script>

<style></style>
