<template>
<div style="background-color: #498d6d; padding-top: 20px">
  <div style="padding:10px"> 
    <StoryTopNavbar :isStory="isStory" :isFollow="FollowTap" :isFilter="isFilter" @change="change" />
  </div>
    <div v-if="isFollow && images.value" style="background-color: white; margin-top: 0; padding-top: 10px; padding-bottom: 10px; border-radius: 20px 20px 0 0" >
      <StoryImageCardList :images="images.value" />
    </div>
    
    <div v-else  style="background-color: white; margin-top: 0; padding:20px 10px; border-radius: 20px 20px 0 0; font-weight: 700;">
      <p>팔로우 한 사람이 없습니다</p>
    </div>
</div>

</template>

<script>
import StoryImageCardList from "@/components/story/StoryImageCardList.vue";
import StoryTopNavbar from "@/components/story/StoryTopNavbar.vue";
import { useStore } from "vuex";
import { onBeforeMount, ref, computed } from "vue";

export default {
  components: {
    StoryImageCardList,
    StoryTopNavbar,
  },
  setup() {
    const store = useStore();
    const images = ref([]);
    const isStory = ref(false);
    const isFollow = ref(true);
    const isFilter = ref(false);
    const FollowTap = ref(true);
    const numberOfPages = ref(0);
    const currentPage = ref(1);

    const getPure = async (page = currentPage.value) => {
      const data = {
        isState: "follow",
        page: page,
      };
      await store.dispatch("story/getFollow", data);
      images.value = computed(() => { return store.state.story.images })
      numberOfPages.value = computed(() => {
        return Math.ceil(store.state.story.totalCount / 10);
      });
    };

    window.onscroll = function (e) {
      if (numberOfPages.value.value > currentPage.value) {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
          setTimeout(function () {
            if (numberOfPages.value.value > currentPage.value) {
              // 실행 시킬 함수 구현
              currentPage.value += 1;
              getPure();
            }
          }, 1000);
        }
      }
    };

    onBeforeMount(async () => {
      await getPure();
      // 메세지 하나밖에 없으면
      if (Object.keys(images.value.value[0]).length == 2) {
        isFollow.value = false;
        images.value = {
          created_at: '',
          story_picture: '',
          story_title: "",
          user_pk: {
            image: "",
            nickname: "",
          }
        }
      } else {
        isFollow.value = true;
      }
    });

    return {
      images,
      isStory,
      isFilter,
      FollowTap,
      isFollow
    };
  },
};
</script>

<style></style>
