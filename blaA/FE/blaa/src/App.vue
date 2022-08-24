<template>
  <header-view></header-view>
  <div class="app" style="padding-bottom: 80px">
    <router-view></router-view>
  </div>
  <footer-view v-if="isLogin"></footer-view>
</template>

<script>
import HeaderView from "@/components/HeaderView.vue";
import FooterView from "@/components/FooterView.vue";
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  components: {
    FooterView,
    // HeaderView,
  },

  setup() {
    const store = useStore();

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    return {
      isLogin,
    };
  },
};
</script>

<style>
@font-face {
  font-family: "Pretendard-ExtraLight";
  src: url("https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-ExtraLight.woff")
    format("woff");
  font-weight: 200;
  font-style: normal;
}
@font-face {
  font-family: "Pretendard-Regular";
  src: url("https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff")
    format("woff");
  font-weight: 200;
  font-style: normal;
}

* {
  font-family: "Pretendard-Regular";
}

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

#title_text {
  font-weight: 800;
  font-size: 18px;
}

#semi_title_text {
  font-weight: 600;
  font-size: 16px;
}

#small_title_text {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 0;
}

#small_text {
  font-size: 12px;
}

.member_icon {
  width: 16px;
  height: 14px;
}

.submit-btn {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 60px;
  height: 36px;

  background: #e58d1f;
  color: white;
  border-radius: 20px;
  border: 0;

  font-family: "Pretendard-Regular";
  font-weight: 400;
}
</style>
