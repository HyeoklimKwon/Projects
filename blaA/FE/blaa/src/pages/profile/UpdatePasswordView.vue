<template>
  <div id="update-password">
    <div>
      <h1 class="update-text">비밀번호 수정</h1>
      <hr />
    </div>

    <form>
      <label for="update-oldpassword">현재 비밀번호</label>
      <input
        id="update-oldpassword"
        type="password"
        v-model="updatePassword.old_password"
        placeholder="Password"
        autocomplete="off"
      />
      <small>현재 비밀번호가 올바르지 않습니다.</small>
      <br />

      <label for="update-newpassword">새로운 비밀번호</label>
      <input
        id="update-newpassword"
        type="password"
        v-model="updatePassword.password"
        placeholder="New Password"
        autocomplete="off"
      />
      <small>비밀번호는 6자리 이상이어야 합니다.</small>
      <br />

      <label for="update-checkpassword">비밀번호 확인</label>
      <input
        id="update-checkpassword"
        type="password"
        v-model="updatePassword.password2"
        placeholder="Check new password"
        autocomplete="off"
      />
      <small>비밀번호가 일치하지 않습니다.</small>
      <br />
      <br />

      <div style="margin-top: 20px">
        <button id="btn-before" @click.prevent="before">이전</button> &nbsp;
        <button id="btn-update" @click.prevent="update">수정</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    const userInfo = store.state.account.userInfo;

    const updatePassword = ref({
      old_password: null,
      password: null,
      password2: null,
    });

    const before = () => {
      router.go(-1);
    };

    const update = async () => {
      let err = true;
      let msg = "";

      err &&
        !updatePassword.value.old_password &&
        ((msg = "비밀번호를 입력해주세요"), (err = false));
      err &&
        updatePassword.value.password.length < 6 &&
        ((msg = "비밀번호는 6자리 이상이어야 합니다"), (err = false));
      err &&
        updatePassword.value.password != updatePassword.value.password2 &&
        ((msg = "비밀번호가 일치하지 않습니다"), (err = false));

      if (!err) {
        alert(msg);
      } else {
        await axios
          .put(
            api.profile.updateMyPW(route.params.user_pk),
            updatePassword.value
          )
          .then((response) => {
            console.log(response);
            console.log("userInfo : ", userInfo);
            const updateInfo = userInfo;
            updateInfo.password = updatePassword.value.password;
            console.log("update password ; ", updateInfo.password);
            store.commit("account/USER_INFO", updateInfo);
            console.log("updateInfo : ", userInfo);
            alert("비밀번호 변경이 완료되었습니다");
            router.push({
              name: "myInfo",
              params: {
                user_pk: route.params.user_pk,
              },
            });
          })
          .catch((err) => {
            console.log(err);
            if (err.response.data.old_password) {
              alert("회원정보에 등록된 비밀번호와 일치하지 않습니다.");
              updatePassword.value.old_password = null;
              updatePassword.value.password = null;
              updatePassword.value.password2 = null;
            }
          });
      }
    };

    return {
      updatePassword,
      before,
      update,
    };
  },
};
</script>

<style scoped>
#update-password {
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

form {
  align-items: center;
  width: 100%;
  vertical-align: middle;
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
