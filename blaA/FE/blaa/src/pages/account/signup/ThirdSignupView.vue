<template>
  <div id="signup">
    <div id="signup-top">
      <h1 class="signup-text">회원가입</h1>
      <div class="signup-step">
        <div class="yellow-circle"><b class="signup-num">1</b></div>
        <img class="arrow" src="@/img/yellow_arrow.png" />
        <div class="yellow-circle"><b class="signup-num">2</b></div>
        <img class="arrow" src="@/img/yellow_arrow.png" />
        <div class="yellow-circle"><b class="signup-num">3</b></div>
      </div>
    </div>

    <form>
      <label for="signup-nickname">닉네임</label>
      <div class="in-line">
        <input
          id="signup-nickname"
          type="text"
          v-model="user.nickname"
          placeholder="Nickname"
        />
        <input
          type="button"
          name="nickname"
          value="중복확인"
          @click.prevent="nicknameCheck"
        />
      </div>
      <small>{{ nicknameMessage }}</small>
      <br />

      <label v-if="is_alba" for="signup-category">근무 중인 업종</label>
      <label v-else for="signup-category">관심 업종</label>
      <select id="signup-category" class="select-value" v-model="user.category">
        <option value="null">업종 카테고리</option>
        <option
          :key="c"
          v-for="(category, c) in category_list"
          :value="category.job_main_category"
        >
          {{ category.job_main_category }}
        </option>
      </select>
      <small>{{ categoryMessage }}</small
      ><br /><br />

      <div>
        <label v-if="is_alba" for="signup-region">근무 중인 지역</label>
        <label v-else for="signup-region">관심 지역</label>
        <br />
        <select
          id="signup-sido"
          class="select-value"
          v-model="user.sido"
          @change="getGu(user.sido)"
        >
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
          <option
            :key="d"
            v-for="(dong, d) in dong_list"
            :value="dong.dong_code"
          >
            {{ dong.dong_name }}
          </option>
        </select>
      </div>
      <small>{{ regionMessage }}</small> <br /><br />

      <div>
        <button class="btn-before" @click.prevent="before">이전</button> &nbsp;
        <button class="btn-next" @click.prevent="signup">등록</button>
      </div>
      <br /><br />
    </form>
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

    const is_alba = computed(() => {
      return store.state.account.signupUser.is_alba;
    });

    const nicknameMessage = ref(null);
    const categoryMessage = ref(null);
    const regionMessage = ref(null);

    const nicknameCheck = () => {
      if (user.value.nickname == null) {
        setTimeout(() => {
          nicknameMessage.value = "먼저 닉네임을 입력해주세요.";
        }, 3000);
      } else {
        const sendNickname = { nickname: user.value.nickname };
        axios
          .post(api.accounts.nicknameCheck(), sendNickname)
          .then((response) => {
            console.log("response : ", response);
            console.log("response status : ", response.status);
            if (response.status === 200 || response.status === 201) {
              setTimeout(() => {
                nicknameMessage.value = "사용 가능한 닉네임입니다.";
              }, 3000);
            }
          })
          .catch((error) => {
            console.log("error : ", error);
            setTimeout(() => {
              nicknameMessage.value = "이미 사용 중인 닉네임입니다.";
            }, 3000);
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

      err &&
        !user.value.nickname &&
        ((nicknameMessage.value = "닉네임을 입력해주세요."),
        setTimeout(() => {
          nicknameMessage.value = "";
        }, 3000),
        (err = false));
      err &&
        !user.value.category &&
        ((categoryMessage.value = "카테고리를 선택해주세요"),
        setTimeout(() => {
          categoryMessage.value = "";
        }, 3000),
        (err = false));
      err &&
        !user.value.sido &&
        ((regionMessage.value = "시/도를 선택해주세요"),
        setTimeout(() => {
          regionMessage.value = "";
        }, 3000),
        (err = false));
      err &&
        !user.value.gugun &&
        ((regionMessage.value = "구/군을 선택해주세요"),
        setTimeout(() => {
          regionMessage.value = "";
        }, 3000),
        (err = false));
      err &&
        !user.value.dong &&
        ((regionMessage.value = "동/면/리를 선택해주세요"),
        setTimeout(() => {
          regionMessage.value = "";
        }, 3000),
        (err = false));

      if (!err) {
        return;
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
              router.push({ name: "login" });
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
      is_alba,
      nicknameMessage,
      categoryMessage,
      regionMessage,
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

<style scoped>
#signup {
  padding-left: 40px;
  padding-right: 40px;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  overflow: auto;
  text-align: center;
  width: 100%;
  height: 100%;
  padding-top: 70px;

  -webkit-animation: fade-in 1.2s cubic-bezier(0.39, 0.575, 0.565, 1) both;
  animation: fade-in 1.2s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}

@-webkit-keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

#signup-top {
  margin-top: 40px;
  width: 100%;
  text-align: center;
  margin-bottom: 15px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.signup-text {
  font-family: "Inter";
  font-style: normal;
  font-weight: 700;
  font-size: 35px;
  line-height: 30px;
  text-align: center;
  margin-bottom: 30px;
}

.signup-step {
  text-align: center;
  display: flex;
  height: 50px;
  line-height: 50px;
  align-items: center;
  justify-content: center;
}

.yellow-circle {
  width: 50px;
  height: 50px;
  background-color: #eec95c;
  border-radius: 50%;
  float: left;
  position: relative;
}

.gray-circle {
  width: 50px;
  height: 50px;
  background-color: #d9d9d9;
  border-radius: 50%;
  float: left;
  position: relative;
}

.signup-num {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 30px;
  line-height: 36px;
  text-align: center;
  color: #ffffff;
  position: absolute;
  left: 50%;
  top: 45%;
  transform: translate(-50%, -50%);
}

.arrow {
  float: left;
  max-height: 100%;
  vertical-align: middle;
  margin-left: 10px;
  margin-right: 10px;
}

label {
  float: left;
  font-family: "Inter";
  font-style: normal;
  font-weight: bold;
  color: black;
}

input {
  width: 100%;
  height: 50px;
  padding: 5px;
  border: solid 2px #d9d9d9;
  border-radius: 8px;
}

.in-line {
  position: relative;
}

input[type="button"] {
  position: absolute;
  width: 90px;
  height: 40px;
  bottom: 5px;
  right: 5px;
  border-radius: 100px;
  background-color: #eec95c;
  border: #eec95c;
  font-weight: bold;
}

small {
  float: left;
  font-family: Inter;
  font-style: normal;
  font-size: 15px;
  color: red;
}

input::placeholder {
  color: #d9d9d9;
}

input:focus {
  border: 2px #eec95c solid;
  outline: none;
}

select {
  width: 100%;
  height: 50px;
  padding: 5px;
  border: solid 2px #d9d9d9;
  border-radius: 8px;
}

select:focus {
  border: 2px #eec95c solid;
  outline: none;
}

.select-value::part(button) {
  color: #ffffff;
  background-color: #f00;
  padding: 5px;
  border-radius: 5px;
}

.select-value::part(listbox) {
  padding: 10px;
  margin-top: 5px;
  border: 1px solid red;
  border-radius: 5px;
}

#signup-sido,
#signup-gugun,
#signup-dong {
  width: 30%;
}

.btn-before {
  width: 100px;
  height: 40px;
  border: 2px solid #eec95c;
  border-radius: 100px;
  background-color: #ffffff;
  color: #498d6d;
  font-family: "Roboto";
  font-style: normal;
  font-weight: 500;
}

.btn-next {
  width: 100px;
  height: 40px;
  background: #eec95c;
  border: #eec95c;
  border-radius: 100px;
  color: #498d6d;
  font-family: "Roboto";
  font-style: normal;
  font-weight: 500;
}
</style>
