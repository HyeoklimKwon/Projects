<template>
  <!-- enctype 파일 업로드에서 무조건 사용 -->
  <div class="d-flex justify-content-center">
    <form @submit.prevent="Sumbit" enctype="multipart/form-data" style="width: 100%">
      <div class="row" id="top_box">
        <div class="col-3" id="top_box_text" style="padding-right: 30px; margin-bottom: 8px" @click="back"><img src="@/assets/icons/arrow-left.png" /></div>
        <h5 class="col-6" id="top_box_text">오출완 작성</h5>
        <div class="col-3" id="top_box_text" style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px">
          <button class="submit-btn" type="submit">제출</button>
        </div>
      </div>
      <div class="container">
        <div id="image">
          <!-- <label for="story_picture">사진 등록</label> -->
          <p id="semi_title_text" style="margin: 0">사진 등록</p>
          <div id="file-button" @click="fileUpload">이미지 불러오기</div>

          <input class="story_picture" id="story_picture" type="file" @change="previewFile" style="display: none" />
          <img class="img_test" src="" height="200" @click="fileUpload" style="z-index: 10" />
          <div v-if="isPictureVaild" style="color: red">사진을 등록해주세요!</div>
        </div>
        <br />
        <div id="title">
          <label style="font-weight: bold; margin-bottom: 4px" for="story_title">문구 입력</label>
          <textarea type="text" placeholder="제목을 입력하세요" v-model="story_title" id="story_title"></textarea>
          <div v-if="isTitleVaild" style="color: red">제목을 입력해주세요!</div>
        </div>
        <br />
        <div>
          <HashTagForm @search-hash-tag="searchHashTag" />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "@/api/axios";
import api from "@/api/api";
import $ from "jquery";
import HashTagForm from "@/components/story/HashTagForm.vue";

export default {
  components: {
    HashTagForm,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const story_picture = ref(null);
    const story_title = ref("");
    const isPictureVaild = ref(false);
    const isTitleVaild = ref(false);
    const image_url = ref("");
    const hashTag = ref([]);
    const hashtag_content = ref("");

    onMounted(() => {
      hashTag.value = [];
      const windowWidth = $(window).width() / 2.3 - 68;
      $("#file-button").css("left", `${windowWidth}px`);
    });

    // 업로드 된 이미지를 미리 확인하는 함수
    const previewFile = (e) => {
      let preview = document.querySelector(".img_test");
      if (e.target.files[0]) {
        story_picture.value = e.target.files[0];
        const reader = new FileReader();

        // 파일명을 가져와서 소문자로 변환
        let fileName = story_picture.value.name.substring(story_picture.value.name.lastIndexOf(".") + 1);
        fileName = fileName.toLowerCase();

        // 파일 형식과 3MB의 파일크기 확인
        if (["jpeg", "png", "gif", "bmp", "jpg", "jfif", "BMP", "webp"].includes(fileName) && story_picture.value.size <= 400000000) {
          reader.onload = (e) => {
            preview.src = e.target.result;
            image_url.value = e.target.result;
          };
          reader.readAsDataURL(story_picture.value);
          // 들어오는 이미지에 따라 height 조절
          let width = preview.naturalWidth;
          let height = preview.naturalHeight;

          console.log(width, height);
          let img_height = height / (width / $(window).width() / (10 / 9));
          preview.height = img_height;
        } else if (story_picture.value.size > 400000000) {
          alert("파일이 용량이 너무 큽니다! 더 용량이 작은 이미지를 선택해주세요");
          preview.src = null;
        } else {
          alert("파일을 다시 선택해 주세요");
          story_picture.value = null;
          preview.src = null;
        }
        // 파일을 선택하지 않았을 떄
      } else {
        story_picture.value = null;
        preview.src = null;
      }
    };

    // $(window).resize(function() {
    //   const preview = document.querySelector('.img_test')

    //   const width = preview.naturalWidth
    //   const height = preview.naturalHeight

    //   const img_height = height / (width / $(window).width() / (10/9))
    //   preview.height = img_height
    // })

    // 파일버튼 교체
    const fileUpload = (e) => {
      e.preventDefault();
      $("#story_picture").click();
    };

    $(window).resize(function () {
      const windowWidth = $(window).width() / 2.3 - 68;
      $("#file-button").css("left", `${windowWidth}px`);
    });

    // 해시태그 값
    const searchHashTag = (hashTag) => {
      hashTag.value = hashTag;
      hashtag_content.value = "";
      for (let i = 0; i < hashTag.value.length; i++) {
        hashtag_content.value += hashTag.value[i];
        if (i < hashTag.value.length - 1) {
          hashtag_content.value += " ";
        }
      }
      // // 마지막 띄어쓰기 제거
      // hashtag_content.value.splice(-1,1)
      // console.log(hashtag_content.value)
    };

    // 제출하는 함수
    const Sumbit = async () => {
      // 사진과 제목 값이 모두 존재할 때 생성
      if (story_picture.value && story_title.value) {
        const form = new FormData();
        form.append("story_picture", story_picture.value);
        form.append("story_title", story_title.value);
        // form.append("file", {
        //   story_picture: story_picture.value,
        //   story_title: story_title.value
        // })
        try {
          const token = store.state.story.Token;
          const res = await axios.post(api.story.story(), form, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
          const index = res.data.story_pk;
          // 해시태그 값이 있다면 생성
          if (hashtag_content.value) {
            try {
              await axios.post(api.story.story() + "hashtag/" + index + "/", {
                hashtag_content: hashtag_content.value,
              });
            } catch (error) {
              console.error(error);
              console.log("해시태그 생성 오류");
            }
          }
          // 작성 후 상세페이지로 이동
          router.push({
            name: "detailStory",
            params: {
              story_pk: index,
            },
          });
        } catch (error) {
          console.log(error);
        }
      } else {
        // 제목과 사진이 입력되지 않았으면 경고문을 띄우기 위한 error
        isPictureVaild.value = story_picture.value ? false : true;
        isTitleVaild.value = story_title.value ? false : true;
      }
    };

    const back = () => {
      router.push({ name: "story" });
    };

    return {
      Sumbit,
      isPictureVaild,
      isTitleVaild,
      story_picture,
      story_title,
      previewFile,
      searchHashTag,
      fileUpload,
      back,
    };
  },
};
</script>

<style scoped>
label {
  font-weight: bold;
}

#top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#sumbit-btn {
  background: #498d6d;
  width: 60px;
  height: 40px;
  border-radius: 20px;
  border: 0px;
  font-weight: bold;
}

#image {
  padding: 20px;
  display: flex;
  flex-direction: column;
  width: 100%;
}

#file-button {
  width: 100%;
  height: 44px;
  margin: 0 0 10px 0;

  display: flex;
  justify-content: center;
  align-items: center;

  background-color: #498d6d;
  color: white;
  border-radius: 8px;
  /* position: relative; */
  /* box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.05); */
  /* top: 140px; */
}

.img_test {
  border: 1px dotted black;
  border-radius: 10px;
  min-height: 200px;
}

#title {
  display: flex;
  padding: 0 20px 20px 20px;
  flex-direction: column;
  align-items: flex-start;
}

#story_title {
  border: 1px solid #c5c6cc;
  border-radius: 12px;
  width: 100%;
  height: 90px;
  padding: 8px;
}
</style>
