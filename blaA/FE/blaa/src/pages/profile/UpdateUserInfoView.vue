<template>
  <div id="update-info">
    <h1 class="update-text">회원정보 수정</h1>
    <hr />

    <form>
      <label for="update-email">이메일</label>
      <input
        id="update-email"
        type="text"
        v-model="updateInfo.email"
        placeholder="Enter email"
        disabled
      />
      <br /><br />

      <label for="update-name">이름</label>
      <input
        id="update-name"
        type="text"
        v-model="updateInfo.name"
        placeholder="Enter name"
        disabled
      />
      <br /><br />

      <label for="update-tel">휴대폰</label>

      <div id="input-tel">
        <input id="update-tel1" type="text" v-model="tel1" />
        <b> - </b>
        <input id="update-tel2" type="text" v-model="tel2" />
        <b> - </b>
        <input id="update-tel3" type="text" v-model="tel3" />
      </div>
      <small>{{ telMessage }}</small
      ><br />

      <hr style="border-style: dotted" />

      <label for="update-nickname">닉네임</label>
      <div class="in-line">
        <input
          id="update-nickname"
          type="text"
          v-model="updateInfo.nickname"
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

      <div>
        <label>현재 근무 중인 직장이 있습니까?</label> <br />
        <input
          type="radio"
          id="selectYes"
          v-model="updateInfo.is_alba"
          value="true"
        />
        <label for="selectYes">예</label>
        <input
          type="radio"
          id="selectNo"
          v-model="updateInfo.is_alba"
          value="false"
        />
        <label for="selectNo">아니오</label>
      </div>
      <br /><br />

      <label v-if="isAlba" for="update-category">근무 중인 업종</label>
      <label v-else for="update-category">관심 업종</label>
      <select id="update-category" v-model="updateInfo.category">
        <option value="null">업종 카테고리</option>
        <option
          :key="c"
          v-for="(category, c) in category_list"
          :value="category.job_main_category"
        >
          {{ category.job_main_category }}
        </option>
      </select>
      <small>{{ categoryMessage }}</small>

      <!-- <div>
        <select id="update-sido" v-model="sido" @change="getGu(sido)">
          <option value="null">시/도</option>
          <option :key="s" v-for="(si, s) in si_list" :value="si.sido_name">
            {{ si.sido_name }}
          </option>
        </select>
        &nbsp;

        <select
          id="update-gugun"
          v-model="gugun"
          @change="getDong(sido, gugun)"
        >
          <option value="null">구/군</option>
          <option :key="g" v-for="(gu, g) in gu_list" :value="gu.gugun_code">
            {{ gu.gugun_name }}
          </option>
        </select>
        &nbsp;

        <select id="signup-dong" v-model="dong">
          <option value="null">동/면/리</option>
          <option
            :key="d"
            v-for="(dong, d) in dong_list"
            :value="dong.dong_code"
          >
            {{ dong.dong_name }}
          </option>
        </select>
      </div> -->

      <div style="margin-top: 20px">
        <button id="btn-before" @click.prevent="before">이전</button> &nbsp;
        <button id="btn-update" @click.prevent="update">수정</button>
      </div>
    </form>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { ref, computed } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();

    const userInfo = store.state.account.userInfo;
    console.log("userInfo : ", userInfo);

    const tel = userInfo.tel.split("-");
    const tel1 = ref(tel[0]);
    const tel2 = ref(tel[1]);
    const tel3 = ref(tel[2]);

    const telMessage = ref(null);
    const nicknameMessage = ref(null);
    const categoryMessage = ref(null);

    // const region = userInfo.region.split(" ");
    // const sido = ref("");
    // for (var i = 0; i < store.state.account.si.length; i++) {
    //   if (store.state.account.si[i].sido_name == region[0]) {
    //     sido.value = store.state.account.si[i].sido_code;
    //     console.log("sido.value : ", sido.value);
    //   }
    // }

    // console.log("sido: ", sido.value);
    // const gugun = ref("");
    // for (var j = 0; j < store.state.account.dong.length; j++) {
    //   if (store.state.account.gu[j].gugun_name == region[1]) {
    //     gugun.value = store.state.account.gu[j].gugun_code;
    //   }
    // }

    // const dong = ref("");
    // for (var k = 0; k < store.state.account.dong.length; k++) {
    //   if (store.state.account.gu[k].dong_name == region[2]) {
    //     dong.value = store.state.account.gu[k].dong_code;
    //   }
    // }

    store.dispatch("account/getCategoryList");
    // store.dispatch("account/getSiList");

    const nicknameCheck = () => {
      if (updateInfo.value.nickname == null) {
        alert("먼저 닉네임을 입력해주세요.");
      } else {
        const sendNickname = { nickname: updateInfo.value.nickname };
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
            updateInfo.value.nickname = null;
          });
      }
    };

    const category_list = computed(() => {
      return store.state.account.category;
    });

    // const si_list = computed(() => {
    //   return store.state.account.si;
    // });

    // const gu_list = computed(() => {
    //   return store.state.account.gu;
    // });

    // const dong_list = computed(() => {
    //   return store.getters["account/dong_list"];
    // });

    // const getGu = (sido) => {
    //   if (sido != null) {
    //     console.log("selected sido :", sido);
    //     store.dispatch("account/getGuList", sido);
    //     gugun.value = null;
    //     dong.value = null;
    //   }
    // };

    // const getDong = (sido, gugun) => {
    //   if (sido != null && gugun != null) {
    //     store.dispatch("account/getDongList", {
    //       sido: sido,
    //       gugun: gugun,
    //     });
    //     dong.value = null;
    //   }
    // };

    const updateInfo = ref({
      email: userInfo.email,
      name: userInfo.name,
      tel: null,
      nickname: userInfo.nickname,
      category: userInfo.category,
      region: userInfo.region,
      is_alba: userInfo.is_alba,
    });
    console.log("updateInfo", updateInfo.value);

    const isAlba = computed(() => {
      return updateInfo.value.is_alba;
    });

    // const checkPassword = () => {
    //   var password = prompt("비밀번호를 입력해주세요!");

    //   if (password) {
    //     axios
    //       .post(api.accounts.login(), {
    //         email: userInfo.email,
    //         password: password,
    //       })
    //       .then((response) => {
    //         console.log("유저 정보 조회 성공 : ", response);
    //       })
    //       .catch((err) => {
    //         console.log("유저 정보 조회 실패 : ", err);
    //         router.go(-1);
    //         alert("비밀번호가 틀립니다!");
    //         checkPassword();
    //       });
    //   } else {
    //     router.go(-1);
    //   }
    // };

    // if (!store.state.account.kakaoLogin) {
    //   checkPassword();
    // }

    const before = () => {
      router.go(-1);
    };

    const update = () => {
      // updateInfo.value.region =
      //   sido.value + " " + gugun.value + " " + dong.value;

      updateInfo.value.tel = tel1.value + "-" + tel2.value + "-" + tel3.value;
      console.log("수정완료 전 updateInfo : ", updateInfo.value);
      axios
        .put(api.profile.myInfo(route.params.user_pk), updateInfo.value)
        .then(async (response) => {
          alert("회원 정보 수정 완료!");
          store.commit("account/USER_INFO", response.data);
          await store.dispatch("account/getMyCrewList", userInfo.value.user_pk);
          router.push({
            name: "myinfo",
            params: { user_pk: route.params.user_pk },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      userInfo,
      nicknameCheck,
      updateInfo,
      isAlba,
      tel1,
      tel2,
      tel3,
      telMessage,
      nicknameMessage,
      categoryMessage,
      before,
      update,
      // sido,
      // gugun,
      // dong,
      category_list,
      // si_list,
      // gu_list,
      // dong_list,
      // getGu,
      // getDong,
      // checkPassword,
    };
  },
};
</script>

<style scoped>
#update-info {
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
  padding-top: 40px;
  padding-bottom: 50px;
}

.update-text {
  font-family: "Inter";
  font-style: normal;
  font-weight: 700;
  font-size: 35px;
  line-height: 30px;
  text-align: center;
  margin-bottom: 30px;
}

label {
  float: left;
  font-family: "Inter";
  font-style: normal;
  font-weight: bold;
  color: black;
}

input[type="text"],
input[type="email"] {
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
}

input::placeholder {
  color: #d9d9d9;
}

input:focus {
  border: 2px #eec95c solid;
  outline: none;
}

input[type="radio"] {
  display: none;
}

input[type="radio"] + label {
  display: inline-block;
  cursor: pointer;
  width: 70px;
  height: 30px;
  border: 2px solid #d9d9d9;
  line-height: 30px;
  text-align: center;
  font-weight: bold;
  font-size: 13px;
  background-color: #ffffff;
  color: #498d6d;
  border-radius: 100px;
}

input[type="radio"]:checked + label {
  background-color: #eec95c;
  border: 2px solid #eec95c;
  color: #498d6d;
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

#btn-before {
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

#btn-update {
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
