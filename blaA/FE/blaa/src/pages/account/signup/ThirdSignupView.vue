<template>
  <h3>회원가입 3단계</h3>

  <input
    id="signup-nickname"
    v-model="user.nickname"
    placeholder="Enter nickname"
  />
  &nbsp;
  <button @click.prevent="nicknameCheck">중복확인</button>
  <br />

  <select id="signup-category" v-model="user.category">
    <option value="null">업종 카테고리</option>
    <option
      :key="c"
      v-for="(category, c) in category_list"
      :value="category.job_main_category"
    >
      {{ category.job_main_category }}
    </option>
  </select>

  <div>
    <select id="signup-sido" v-model="user.sido" @change="getGu(user.sido)">
      <option value="null">시/도</option>
      <option :key="s" v-for="(si, s) in si_list" :value="si.sido_code">
        {{ si.sido_name }}
      </option>
    </select>
    &nbsp;

    <select
      id="signup-gugun"
      v-model="user.gugun"
      @change="getDong(user.sido, user.gugun)"
    >
      <option value="null">구/군</option>
      <option :key="g" v-for="(gu, g) in gu_list" :value="gu.gugun_code">
        {{ gu.gugun_name }}
      </option>
    </select>
    &nbsp;

    <select id="signup-dong" v-model="user.dong">
      <option value="null">동/면/리</option>
      <option :key="d" v-for="(dong, d) in dong_list" :value="dong.dong_code">
        {{ dong.dong_name }}
      </option>
    </select>
  </div>

  <div>
    <button @click.prevent="before">이전</button> &nbsp;
    <button @click.prevent="signup">가입</button>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import axios from "axios";
import api from "@/api/api.js";
import router from "@/router/index.js";

export default {
  setup() {
    const store = useStore();

    const user = ref({
      nickname: null,
      category: null,
      sido: null,
      gugun: null,
      dong: null,
    });

    store.dispatch("account/getCategoryList");
    store.dispatch("account/getSiList");

    const nicknameCheck = () => {
      if (user.value.nickname == null) {
        alert("먼저 닉네임을 입력해주세요.");
      } else {
        const sendNickname = { nickname: user.value.nickname };
        axios
          .post(api.accounts.nicknameCheck(), sendNickname)
          .then((response) => {
            console.log("response : ", response);
            console.log("response status : ", response.status);
            if (response.status === 200 || response.status === 201) {
              alert("사용 가능한 닉네임입니다.");
            }
          })
          .catch((error) => {
            console.log("error : ", error);
            alert("이미 사용중인 닉네임입니다.");
            user.value.nickname = null;
          });
      }
    };

    const category_list = computed(() => {
      return store.state.account.category;
    });

    const si_list = computed(() => {
      return store.state.account.si;
    });

    const gu_list = computed(() => {
      return store.state.account.gu;
    });

    const dong_list = computed(() => {
      return store.getters["account/dong_list"];
    });

    const getGu = (sido) => {
      if (sido != null) {
        console.log("selected sido : ", sido);
        store.dispatch("account/getGuList", sido);
        user.value.gugun = null;
        user.value.dong = null;
      }
    };

    const getDong = (sido, gugun) => {
      if (sido != null && gugun != null) {
        store.dispatch("account/getDongList", {
          sido: user.value.sido,
          gugun: user.value.gugun,
        });
        user.value.dong = null;
      }
    };

    const before = () => {
      router.go(-1);
    };

    const signup = () => {
      let err = true;
      let msg = "";

      err &&
        !user.value.nickname &&
        ((msg = "닉네임을 입력해주세요"), (err = false));
      err &&
        !user.value.category &&
        ((msg = "카테고리를 선택해주세요"), (err = false));
      err &&
        !user.value.sido &&
        ((msg = "시/도를 선택해주세요"), (err = false));
      err &&
        !user.value.gugun &&
        ((msg = "구/군을 선택해주세요"), (err = false));
      err &&
        !user.value.dong &&
        ((msg = "동/면/리를 선택해주세요"), (err = false));

      if (!err) {
        alert(msg);
      } else {
        store.commit("account/SET_SIGNUP_NICKNAME", user.value.nickname);

        store.commit("account/SET_SIGNUP_CATEGORY", user.value.category);

        var sido = document.getElementById("signup-sido");
        const sido_name = sido.options[sido.selectedIndex].text;
        var gugun = document.getElementById("signup-gugun");
        const gugun_name = gugun.options[gugun.selectedIndex].text;
        var dong = document.getElementById("signup-dong");
        const dong_name = dong.options[dong.selectedIndex].text;

        const region = sido_name + " " + gugun_name + " " + dong_name;
        console.log(region);
        store.commit("account/SET_SIGNUP_REGION", region);

        axios
          .post(api.accounts.signup(), store.state.account.signupUser)
          .then((response) => {
            console.log("vuex signupUser : ", store.state.account.signupUser);
            console.log("response : ", response);

            if (response.status === 201) {
              console.log("회원가입 성공");
              router.push({ name: "home" });
              console.log(
                "회원가입 후 vuex : ",
                store.state.account.signupUser
              );
              alert("회원가입 완료!");
            } else {
              console.log("회원가입 문제 발생");
              console.log("회원가입 문제 에러코드 : ", response.status);
            }
          });
      }
    };

    return {
      user,
      nicknameCheck,
      category_list,
      si_list,
      gu_list,
      dong_list,
      getGu,
      getDong,
      before,
      signup,
    };
  },
};
</script>

<style></style>
