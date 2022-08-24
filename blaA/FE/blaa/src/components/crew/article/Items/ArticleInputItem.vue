<template>
  <div>
    <label for="crew_title">제목</label>
    <input type="text" id="crew_title" name="crew_title" v-model="article.crew_title" /><br />
    <label for="crew_content">내용</label><br />
    <textarea id="crew_content" name="crew_content" v-model="article.crew_content" cols="35" rows="5"></textarea><br />
    <input type="radio" id="crew_private" name="crew_private" value="false" v-model="article.crew_private" />공개<br />
    <input type="radio" id="crew_private" name="crew_private" value="true" v-model="article.crew_private" />비공개<br />
    <input type="radio" id="crew_pin" name="crew_pin" value="true" v-model="article.crew_pin" />핀 고정<br />
    {{ article.crew_pin }}
    <button v-if="type === 'regist'" @click="checkValue">등록</button>
    <button v-else @click="checkValue">수정</button>
    <button @click="moveList">목록</button>
  </div>
</template>

<script>
import { computed, reactive } from "vue";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
export default {
  props: {
    type: {
      type: String,
    },
  },
  setup(props) {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const article = reactive({
      image_update: false,
      crew_title: "",
      crew_content: "",
      crew_private: false,
      crew_pin: false,
    });

    if (props.type === "modify") {
      Object.assign(article, store.state.crew.article);
    }

    const checkValue = () => {
      let error = true;
      let msg = "";
      console.log("제목: " + article.crew_title);
      !article.crew_title && ((msg = "제목을 입력하세요."), (error = false));
      error && !article.crew_content && ((msg = "내용을 입력하세요."), (error = false));
      error && article.crew_private == "null" && ((msg = "공개 여부를 선택하세요."), (error = false));

      if (!error) alert(msg);
      else {
        if (props.type === "regist") registArticle();
        else modifyArticle();
      }
    };

    const registArticle = async () => {
      console.log("글 등록");
      await store.dispatch("crew/registArticle", {
        crew_pk: route.params.crew_pk,
        article: article,
      });
      alert("등록이 완료되었습니다.");
      moveList();
    };

    const modifyArticle = async () => {
      console.log("글 수정");
      await store.dispatch("crew/modifyArticle", {
        crew_article_pk: route.params.crew_article_pk,
        article: article,
      });
      alert("수정이 완료되었습니다.");
      moveList();
    };

    const moveList = () => {
      router.push({ name: "articlelist" });
    };

    const reload = computed(() => {
      return article;
    });

    return {
      // modify,
      article,
      checkValue,
      moveList,
      registArticle,
    };
  },
};
// export default {data() {
//     return {
//       crew_title: "",
//       crew_content: "",
//       crew_private: "",
//       crew_pin: "false",
//     };
//   },
//   props: {
//     crew_pk: Number,
//   },
//   methods: {
//     // 입력값 체크하기 - 체크가 성공하면 registBook 호출
//     checkValue() {
//       // 사용자 입력값 체크하기
//       // isbn, 제목, 저자, 가격, 설명이 없을 경우 각 항목에 맞는 메세지를 출력
//       let err = true;
//       let msg = "";
//       console.log("유저: " + this.userName);
//       err && !this.crew_title && ((msg = "제목 입력해주세요"), (err = false), this.$refs.crew_title.focus());
//       err && !this.crew_content && ((msg = "내용 입력해주세요"), (err = false), this.$refs.crew_content.focus());

//       if (!err) alert(msg);
//       // 만약, 내용이 다 입력되어 있다면 registBook 호출
//       else this.registArticle();
//     },

//     registArticle() {
//       console.log(this.$route.params.crew_pk);
//       axios
//         .post(
//           url + "crews/article/" + this.$route.params.crew_pk + "/",
//           {
//             crew_title: this.crew_title,
//             crew_content: this.crew_content,
//             crew_private: this.crew_private,
//             crew_pin: this.crew_pin,
//           },
//           {
//             headers: {
//               auth,
//             },
//           }
//         )
//         .then(({ data }) => {
//           console.log(data);
//           // 서버에서 정상적인 값이 넘어 왔을경우 실행.
//           let msg = "등록이 완료되었습니다.";
//           alert(msg);
//           this.moveCrew();
//         })
//         .catch((error) => console.log(error));
//     },
//     moveCrew() {
//       this.$router.push({ name: "articlelist", params: { crew_pk: this.$route.params.crew_pk } });
//     },};
</script>

<style></style>
