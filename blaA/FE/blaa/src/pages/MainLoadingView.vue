<template>
  <div id="home">
    <h1 id="loading-text"><b>내 알바, 내 알 바!</b></h1>

    <div id="img-center">
      <img id="loading-logo" src="@/img/blaA.png" />
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  setup() {
    const store = useStore();
    const router = useRouter();

    const isLogin = computed(() => {
      return store.state.account.isLogin;
    });

    const isKakaoLogin = computed(() => {
      return store.state.account.kakaoLogin;
    });

    setTimeout(() => {
      if (isLogin.value || isKakaoLogin.value) {
        router.push("/story");
      } else {
        console.log("로그인 페이지 이동");
        router.push({ name: "login" });
      }
    }, 4500);
    return {
      isLogin,
      isKakaoLogin,
    };
  },
};
</script>

<style scoped>
#home {
  padding: 20px;
  background-color: #eec95c;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  overflow: auto;

  -webkit-animation: slide-out-left 0.8s cubic-bezier(0.55, 0.085, 0.68, 0.53)
    4s both;
  animation: slide-out-left 0.8s cubic-bezier(0.55, 0.085, 0.68, 0.53) 4s both;
}

@-webkit-keyframes slide-out-left {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
}
@keyframes slide-out-left {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(-1000px);
    transform: translateX(-1000px);
    opacity: 0;
  }
}

#loading-text {
  float: right;
  margin-top: 120px;
  /* font-size: 40px; */
  color: white;
  -webkit-animation: tracking-in-expand 1s cubic-bezier(0.215, 0.61, 0.355, 1)
    both;
  animation: tracking-in-expand 1s cubic-bezier(0.215, 0.61, 0.355, 1) both;
}

@-webkit-keyframes tracking-in-expand {
  0% {
    letter-spacing: -0.5em;
    opacity: 0;
  }
  40% {
    opacity: 0.6;
  }
  100% {
    opacity: 1;
  }
}
@keyframes tracking-in-expand {
  0% {
    letter-spacing: -0.5em;
    opacity: 0;
  }
  40% {
    opacity: 0.6;
  }
  100% {
    opacity: 1;
  }
}

#img-center {
  position: relative;
  width: 100%;
  height: 100%;
}

#loading-logo {
  width: 200px;
  height: 200px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -100px;
  margin-top: -100px;
  -webkit-animation: text-focus-in 1.2s cubic-bezier(0.55, 0.085, 0.68, 0.53) 1s
    both;
  animation: text-focus-in 1.2s cubic-bezier(0.55, 0.085, 0.68, 0.53) 1s both;
}

@-webkit-keyframes text-focus-in {
  0% {
    -webkit-filter: blur(12px);
    filter: blur(12px);
    opacity: 0;
  }
  100% {
    -webkit-filter: blur(0px);
    filter: blur(0px);
    opacity: 1;
  }
}
@keyframes text-focus-in {
  0% {
    -webkit-filter: blur(12px);
    filter: blur(12px);
    opacity: 0;
  }
  100% {
    -webkit-filter: blur(0px);
    filter: blur(0px);
    opacity: 1;
  }
}
</style>
