<template>
  <form @submit.prevent="submitForm" enctype="multipart/form-data">
    <!-- <label for="crew_title">제목</label><br /> -->
    <input type="text" id="crew_title" name="crew_title" v-model="article.crew_title" placeholder="제목을 입력해주세요." /><br />
    <!-- <label for="crew_content">내용</label><br /> -->
    <textarea id="crew_content" name="crew_content" v-model="article.crew_content" cols="35" rows="5" placeholder="내용을 입력해주세요."></textarea><br />

    <label for="images">이미지 첨부</label>
    <input type="file" id="images" name="images" multiple="multiple" @change="previewFile" /><br />

    <div class="row" style="text-align: center; margin: 0; padding: 0">
      <div class="col-3" style="line-height: 60px; padding-left: 20px">공개 여부</div>
      <div class="col-9">
        <div id="crew_private">
          <input type="radio" id="crew_private1" name="crew_private" value="false" v-model="article.crew_private" />
          <label for="crew_private1">공개</label>
          <input type="radio" id="crew_private2" name="crew_private" value="true" v-model="article.crew_private" />
          <label for="crew_private2">비공개</label>
          <br />
        </div>
      </div>
    </div>

    <div class="row" style="text-align: center; margin: 0; padding: 0">
      <div class="col-3" style="line-height: 60px; padding-left: 20px">핀 고정</div>
      <div class="col-9">
        <div id="crew_pin">
          <input type="radio" id="crew_pin1" name="crew_pin" value="true" v-model="article.crew_pin" />
          <label for="crew_pin1">게시물 고정</label>
          <input type="radio" id="crew_pin2" name="crew_pin" value="false" v-model="article.crew_pin" />
          <label for="crew_pin2">고정 해제</label>
          <br />
        </div>
      </div>
    </div>

    <button class="submitBtn" type="submit">등록</button>
  </form>
</template>

<script>
import { computed, reactive, ref } from "vue";
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
      images: [],
    });

    if (props.type === "modify") {
      Object.assign(article, store.state.crew.article);
    }

    const submitForm = () => {
      let error = true;
      let msg = "";
      console.log("제목: " + article.crew_title);
      !article.crew_title && ((msg = "제목을 입력하세요."), (error = false));
      error && !article.crew_content && ((msg = "내용을 입력하세요."), (error = false));
      error && article.crew_private == "null" && ((msg = "공개 여부를 선택하세요."), (error = false));

      if (!error) alert(msg);
      else processingArticle();
    };

    const previewFile = (e) => {
      if (e.target.files) {
        article.images = e.target.files;
      } else {
        alert("파일을 다시 선택해 주세요");
        article.images = null;
      }
    };

    const processingArticle = async () => {
      const articleData = new FormData();
      console.log("이미지 어케 받는겨", article.images);
      articleData.append("crew_title", article.crew_title);
      articleData.append("crew_content", article.crew_content);
      articleData.append("crew_private", article.crew_private);
      articleData.append("crew_pin", article.crew_pin);
      for (var i = 0; i < article.images.length; i++) {
        // console.log("이미지들", article.images[i]);
        articleData.append("images", article.images[i]);
      }

      if (props.type === "regist") {
        console.log("글 등록");
        await store.dispatch("crew/registArticle", {
          crew_pk: route.params.crew_pk,
          article: articleData,
        });
      } else {
        console.log("글 수정");
        await store.dispatch("crew/modifyArticle", {
          crew_article_pk: route.params.crew_article_pk,
          article: articleData,
        });
      }
    };

    const moveList = () => {
      router.push({ name: "articlelist", params: { crew_pk: route.params.crew_pk } });
    };

    const reload = computed(() => {
      return article;
    });

    return {
      article,
      submitForm,
      moveList,
      previewFile,
    };
  },
};
</script>

<style scoped>
#crew_title {
  width: 100%;
  height: 50px;

  border-top: none;
  border-left: none;
  border-right: none;

  padding-left: 10px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

#crew_content {
  width: 100%;
  height: 350px;

  border-top: none;
  border-left: none;
  border-right: none;

  padding-left: 10px;
  padding-top: 15px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.submitBtn {
  position: absolute;
  width: 54px;
  height: 32px;
  left: 290px;
  top: 11px;

  font-family: "Pretendard-Regular";
  font-weight: 600;
  /* transition: 0.25s; */

  width: 60px;
  height: 36px;

  background: #e58d1f;
  color: white;
  border-radius: 20px;
  border: 0;
}

#crew_private,
#crew_pin {
  padding: 15px 10px 0px 0px;
}
#crew_private input[type="radio"],
#crew_pin input[type="radio"] {
  display: none;
}
#crew_private input[type="radio"] + label,
#crew_pin input[type="radio"] + label {
  display: inline-block;
  cursor: pointer;
  height: 30px;
  width: 100px;
  border: 1px solid #498d6d;
  line-height: 30px;
  text-align: center;
  font-weight: bold;
  font-size: 13px;
}
#crew_private input[type="radio"] + label,
#crew_pin input[type="radio"] + label {
  background-color: #fff;
  color: #498d6d;
}
#crew_private input[type="radio"]:checked + label,
#crew_pin input[type="radio"]:checked + label {
  background-color: #498d6d;
  color: #fff;
}
</style>
