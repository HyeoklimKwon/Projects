<template>
  <div id="signup">
    <div id="signup-top">
      <h1 class="signup-text">회원가입</h1>
      <div class="signup-step">
        <div class="yellow-circle"><b class="signup-num">1</b></div>
        <img class="arrow" src="@/img/yellow_arrow.png" />
        <div class="yellow-circle"><b class="signup-num">2</b></div>
        <img class="arrow" src="@/img/yellow_arrow.png" />
        <div class="gray-circle"><b class="signup-num">3</b></div>
      </div>
    </div>

    <form>
      <label for="signup-email">이메일</label>
      <div class="in-line">
        <input
          id="signup-email"
          type="email"
          name="email"
          v-model="user.email"
          placeholder="E-mail"
        />
        <input
          type="button"
          name="email"
          value="중복확인"
          @click.prevent="emailCheck"
        />
      </div>
      <small>{{ emailMessage }}</small>
      <br />

      <b id="password-form">
        <label v-if="!kakaoLogin" for="signup-password"> 비밀번호 </label>
        <input
          id="signup-password"
          type="password"
          v-model="user.password"
          placeholder="Password"
          autocomplete="off"
        />
        <small>{{ passwordMessage }}</small>
        <br /><br />

        <label for="signup-checkpassword"> 비밀번호 확인 </label>
        <input
          id="signup-checkpassword"
          type="password"
          placeholder="Password"
          autocomplete="off"
        />
        <small>{{ checkPasswordMessage }}</small>
        <br /><br />
      </b>

      <label for="signup-name"> 이름 </label>
      <input
        id="signup-name"
        type="text"
        v-model="user.name"
        placeholder="Name"
      />
      <small>{{ nameMessage }}</small>
      <br /><br />

      <label for="signup-tel"> 휴대폰 </label> <br />

      <div id="input-tel">
        <input id="signup-tel1" type="text" v-model="user.tel1" />
        <b class="tel-text"> - </b>
        <input id="signup-tel2" type="text" v-model="user.tel2" />
        <b class="tel-text"> - </b>
        <input id="signup-tel3" type="text" v-model="user.tel3" />
      </div>
      <small>{{ telMessage }}</small>
      <br /><br />
      <div>
        <button class="btn-before" @click.prevent="before">이전</button> &nbsp;
        <button class="btn-next" @click.prevent="next">다음</button>
      </div>
      <br /><br />
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import { useCookies } from "vue3-cookies";
import router from "@/router/index.js";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const store = useStore();
    const { cookies } = useCookies();

    const user = ref({
      email: null,
      password: "",
      name: null,
      tel1: null,
      tel2: null,
      tel3: null,
    });

    const emailMessage = ref(null);
    const passwordMessage = ref(null);
    const checkPasswordMessage = ref(null);
    const nameMessage = ref(null);
    const telMessage = ref(null);

    onMounted(() => {
      const kakaoLogin = store.state.account.kakaoLogin;
      console.log("kakaoLogin : ", kakaoLogin);
      if (kakaoLogin) {
        user.value.email = store.state.account.kakaoUserInfo.email;
        console.log(user.value.email);
        document.getElementById("signup-email").disabled = true;
        document.getElementById("btnEmailCheck");

        user.value.password = cookies.get("access-token");
        document.getElementById("signup-password").style.display = "none";
        document.getElementById("signup-checkpassword").style.display = "none";
        document.getElementById("password-form").textContent = "";

        user.value.name = store.state.account.kakaoUserInfo.name;
        document.getElementById("signup-name").disabled = true;
      }
    });

    const emailCheck = () => {
      if (!user.value.email) {
        // alert("먼저 이메일을 입력해주세요.");
        emailMessage.value = "먼저 이메일을 입력해주세요";
        setTimeout(() => {
          emailMessage.value = "";
        }, 3000);
      } else {
        console.log(user.value.email);
        const sendEmail = { email: user.value.email };
        axios
          .post(api.accounts.emailCheck(), sendEmail)
          .then((response) => {
            console.log(response.status);
            if (response.status === 200 || response.status === 201) {
              // alert("사용 가능한 이메일입니다.");
              emailMessage.value = "사용 가능한 이메일입니다.";
              setTimeout(() => {
                emailMessage.value = "";
              }, 3000);
            }
          })
          .catch((error) => {
            console.log("error : ", error);
            // alert("이미 사용중인 이메일입니다.");
            emailMessage.value = "이미 사용중인 이메일입니다.";
            setTimeout(() => {
              emailMessage.value = "";
            }, 3000);
            user.value.email = null;
          });
      }
    };

    const before = () => {
      router.go(-1);
    };

    const next = () => {
      let err = true;

      err &&
        !user.value.email &&
        ((emailMessage.value = "이메일을 입력해주세요."),
        console.log("email"),
        setTimeout(() => {
          emailMessage.value = "";
        }, 3000),
        (err = false));

      if (!store.state.account.kakaoLogin) {
        err &&
          !user.value.password &&
          ((passwordMessage.value = "비밀번호를 입력해주세요."),
          setTimeout(() => {
            passwordMessage.value = "";
          }, 3000),
          (err = false));

        console.log("length : ", user.value.password.length);
        err &&
          user.value.password.length < 6 &&
          ((passwordMessage.value = "비밀번호는 6자리 이상이어야 합니다."),
          setTimeout(() => {
            passwordMessage.value = "";
          }, 3000),
          (err = false));

        err &&
          !document.getElementById("signup-checkpassword").value &&
          ((checkPasswordMessage.value = "비밀번호를 다시 한 번 입력해주세요."),
          setTimeout(() => {
            checkPasswordMessage.value = "";
          }, 3000),
          (err = false));

        err &&
          user.value.password !=
            document.getElementById("signup-checkpassword").value &&
          ((checkPasswordMessage.value = "비밀번호가 일치하지 않습니다."),
          setTimeout(() => {
            checkPasswordMessage.value = "";
          }, 3000),
          (err = false));
      }

      err &&
        !user.value.name &&
        ((nameMessage.value = "이름을 입력해주세요."),
        setTimeout(() => {
          nameMessage.value = "";
        }, 3000),
        (err = false));

      err &&
        (!user.value.tel1 || !user.value.tel2 || !user.value.tel3) &&
        ((telMessage.value = "휴대폰 번호를 입력해주세요."),
        setTimeout(() => {
          telMessage.value = "";
        }, 3000),
        (err = false));

      if (!err) {
        return;
      } else {
        const tel =
          user.value.tel1 + "-" + user.value.tel2 + "-" + user.value.tel3;

        store.commit("account/SET_SIGNUP_EMAIL", user.value.email);
        store.commit("account/SET_SIGNUP_PASSWORD", user.value.password);
        store.commit("account/SET_SIGNUP_NAME", user.value.name);
        store.commit("account/SET_SIGNUP_TEL", tel);

        router.push({ name: "category" });
      }
    };

    return {
      user,
      emailMessage,
      passwordMessage,
      checkPasswordMessage,
      nameMessage,
      telMessage,
      emailCheck,
      before,
      next,
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
  padding-top: 20px;

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

#input-tel {
  width: 100%;
  display: block;
}

#signup-tel1 {
  width: 20%;
  display: inline;
}

#signup-tel2,
#signup-tel3 {
  width: 30%;
  display: inline;
}

.tel-text {
  font-weight: bold;
  font-size: 30px;
  color: #d9d9d9;
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
