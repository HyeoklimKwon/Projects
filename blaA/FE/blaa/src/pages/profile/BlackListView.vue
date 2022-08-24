<template>
  <div id="blacklist">
    <div id="blacklist-header">
      <img src="@/img/closeIcon.png" @click="close" />
      <h2 id="blacklist-text">신고하기</h2>
      <button @click.prevent="setBlackList">등록</button>
    </div>
    <hr />

    <form>
      <label for="blacklist-category">신고 사유</label>
      <select id="blacklist-category" v-model="blackList.black_reason">
        <option value="null">신고 사유 선택</option>
        <option value="부적절한 닉네임">부적절한 닉네임</option>
        <option value="욕설/혐오 발언">욕설/혐오 발언</option>
        <option value="악의적인 리뷰">악의적인 리뷰</option>
        <option value="기타">기타</option>
      </select>
      <small>{{ categoryMessage }}</small>

      <br /><br />

      <label for="blacklist-reason">신고 내용</label>
      <textarea
        id="blacklist-reason"
        rows="10"
        v-model="blackList.black_content"
      ></textarea>
      <small>{{ reasonMessage }}</small>
    </form>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();

    const blackList = ref({
      black_reason: null,
      black_content: null,
      user_pk: route.params.user_pk,
    });

    const close = () => {
      var closeBlackList = confirm(
        "작성한 내용이 저장되지 않습니다. 계속 하시겠습니까?"
      );

      if (closeBlackList) {
        router.go(-1);
      }
    };

    const categoryMessage = ref(null);
    const reasonMessage = ref(null);

    const setBlackList = () => {
      let err = true;

      if (!blackList.value.black_content) {
        err = true;
        categoryMessage.value = "신고 사유를 반드시 선택해야 합니다.";
        setTimeout(() => {
          categoryMessage.value = "";
          err = false;
        }, 3000);
      }

      if (!blackList.value.black_reason) {
        err = true;
        reasonMessage.value = "신고 내용을 반드시 작성해야 합니다.";
        setTimeout(() => {
          reasonMessage.value = "";
          err = false;
        }, 3000);
      }

      if (err) {
        axios
          .post(api.profile.setBlackList(), blackList.value)
          .then((response) => {
            console.log("blacklist response : ", response);
            alert("신고 완료!");
            router.push({
              name: "userProfile",
              user_pk: route.params.user_pk,
            });
          })
          .catch((err) => {
            console.log("blacklist err : ", err);
            alert("신고 오류");
          });
      }
    };

    return {
      blackList,
      close,
      categoryMessage,
      reasonMessage,
      setBlackList,
    };
  },
};
</script>

<style scoped>
#blacklist {
  padding: 20px;
}

#blacklist-header {
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  width: 25px;
  height: 25px;
  left: 25px;
  top: 25px;
}

#blacklist-text {
  width: 95%;
  height: 30px;
  left: 45px;
  top: 27px;

  font-family: "Lato";
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 30px;

  align-items: center;
  text-align: center;
}

button {
  width: 80px;
  height: 40px;
  left: 285px;
  top: 33px;
  background: #498d6d;
  border-radius: 20px;
  border: #498d6d;
  margin-left: auto;

  color: #000000;
  font-family: "Roboto";
  font-style: normal;
  font-weight: 700;
  font-size: 17px;
}

label {
  float: left;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: bold;
  font-size: 17px;
  color: black;
}

select {
  width: 100%;
  height: 50px;
  padding: 5px 5px 5px 5px;
  border: solid 2px #c5c6cc;
  border-radius: 8px;

  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;

  font-family: "Noto Sans KR";
  font-weight: 600;
  font-size: 1rem;
  color: #444;
  background-color: #fff;
}

select:focus {
  border: 2px #498d6d solid;
  outline: none;
}

textarea {
  width: 100%;
  padding: 10px;
  border-radius: 12px;
  border: 2px solid #c5c6cc;

  font-family: "Noto Sans KR";
  font-size: 15px;
}

textarea:focus {
  border: 2px #498d6d solid;
  outline: none;
}
</style>
