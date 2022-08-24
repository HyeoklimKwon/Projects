<template>
  <!-- <div style="width: 100%; height: 500px; background-color: #eea236"></div> -->
  <!-- <div style="width: 100%; height: 500px; background-color: #a94442"></div> -->

  <!-- <div class="row" id="bottom_menu">
    <div class="col" @click.prevent="gostory">
      <img width="25" src="@/assets/footer/home.png" />
    </div>
    <div class="col" @click.prevent="gocrew">
      <img width="25" src="@/assets/footer/group.png" />
    </div>
    <div class="col" @click.prevent="goReview">
      <img width="25" src="@/assets/footer/store.png" />
    </div>
    <div class="col" @click.prevent="goMyProfile">
      <img width="25" src="@/assets/footer/gear.png" />
    </div>
  </div> -->

  <div class="tab-nav-container">
    <div class="tab active" @click.prevent="gostory">
      <i class="fas fa-home"></i>
      <p>Home</p>
    </div>
    <div class="tab" @click.prevent="gocrew">
      <i class="fas fa-users"></i>
      <p>Crew</p>
    </div>
    <div class="tab" @click.prevent="goReview">
      <i class="fas fa-star"></i>
      <p>Review</p>
    </div>
    <div class="tab" @click.prevent="goMyProfile">
      <i class="fas fa-user"></i>
      <p>Profile</p>
    </div>
  </div>
</template>

<script>
import { onMounted } from "@vue/runtime-core";
import { useRouter } from "vue-router";
export default {
  setup() {
    const router = useRouter();

    const gostory = () => {
      router.push({ path: "/story" });
    };

    const gocrew = () => {
      router.push({ path: "/crew" });
    };

    const goMyProfile = async () => {
      router.push({ path: "/profile" });
    };

    const goReview = () => {
      router.push({ path: "/review" });
    };

    onMounted(() => {
      const tabs = document.querySelectorAll(".tab");
      console.log(tabs);
      tabs.forEach((clickedTab) => {
        clickedTab.addEventListener("click", () => {
          tabs.forEach((tab) => {
            tab.classList.remove("active");
          });
          clickedTab.classList.add("active");
          // const clickedTabBGColor = getComputedStyle(clickedTab).getPropertyValue("color");
          // document.body.style.background = clickedTabBGColor;
        });
      });
    });

    return {
      gostory,
      gocrew,
      goMyProfile,
      goReview,
    };
  },
};
</script>

<!-- <style scoped>
#bottom_menu {
  position: fixed;
  bottom: 0px;
  left: 0px;
  width: 100%;
  height: 65px;
  z-index: 100;
  border-top: 1px solid black;
  background-color: white;
  margin: 0;

  text-align: center;
  align-content: center;
  overflow-x: hidden;
}
</style> -->

<style scoped>
.tab-nav-container {
  /* background-color: rgb(226, 226, 226); */
  background-color: white;
  /* border-bottom-right-radius: 20px; */
  /* border-bottom-left-radius: 20px; */
  /* box-shadow: 0 15px 10px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.16); */
  display: flex;
  padding: 10px;
  justify-content: space-between;

  position: fixed;
  bottom: 0px;
  left: 0px;
  width: 100%;
  height: 65px;
  z-index: 10;
}
.tab {
  background-color: white;
  border-radius: 50px;
  cursor: pointer;

  display: inline;
  text-align: center;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
  margin: 0 5px;
  transition: background 0.2s linear;
}
.tab i {
  font-size: 1em;
}
.tab p {
  /* font-weight: bold; */
  font-size: 10px;
  text-align: center;
  overflow: hidden;
  max-width: 0;
}
.tab p {
  /* margin-left: 10px; */
  max-width: 100px;
  transition: max-width 0.2s linear;
}
.tab.active.purple {
  background-color: rgba(91, 55, 183, 0.2);
  color: rgba(91, 55, 183, 1);
}
.tab.active.pink {
  background-color: rgba(201, 55, 157, 0.2);
  color: rgba(201, 55, 157, 1);
}
.tab.active.yellow {
  background-color: rgba(230, 169, 25, 0.2);
  color: rgba(230, 169, 25, 1);
}
.tab.active.teal {
  background-color: rgba(28, 150, 162, 0.2);
  color: rgba(28, 150, 162, 1);
}

.tab.active {
  /* background-color: rgba(28, 150, 162, 0.2); */
  color: #498d6d;
}
</style>
