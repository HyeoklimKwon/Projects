<template>
  <div style="padding: 0 20px 20px 20px">
    <div class="tr_hashTag_area">
      <p id="semi_title_text" style="margin: 0">해시태그</p>

      <div class="form-group">
        <input type="hidden" value="" name="tag" id="rdTag" />
      </div>
      <div style="margin: 12px 0">
        <div id="tag-list" :style="{ minHeight: adjustHeight.value }"></div>
      </div>

      <div class="form-group">
        <input type="text" id="tag" size="7" placeholder="#은 제외하고 작성해주세요" style="width: 100%" />
      </div>
      <div id="reset" @click="reset">초기화</div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import { ref, onBeforeMount, computed } from "vue";

export default {
  props: {
    isHashTag: Boolean,
  },
  emits: ["search-hash-tag"],
  setup(props, { emit }) {
    const tag = ref([]);
    const adjustHeight = ref(0);

    onBeforeMount(() => {
      // 값 초기화
      tag.value = [];
      $("#tag-list").empty();
      emit("search-hash-tag", tag.value);
    });

    const reset = (e) => {
      $("#tag-list").empty();
      tag.value = [];
      $("#tag").val("");
      e.preventDefault();
    };

    // 문서가 준비되었으면 해당 함수를 실행
    $(document).ready(function () {
      // 해시태그가 Array 형태로 저장되어 있음
      const counter = ref(0);

      function addTag(value) {
        tag.value.push(value);
        counter.value += 1;
      }

      // marginTag는 필더를 사용해 tag안에 값을 array로 넘긴다.
      function marginTag() {
        return Object.values(tag).filter(function (word) {
          return word !== "";
        });
      }

      // 클라이언트에 제공
      $("#tag-form").on("submit", function () {
        const value = marginTag(); // tag Array를 반환
        $("#rdTag").val(value);

        $(this).submit();
      });

      $("#tag").on("keypress", function (e) {
        const self = $(this);

        // 엔터나 스페이스바를 입력하였을 떄 실행
        if (e.key === "Enter" || e.keyCode == 32) {
          const tagValue = self.val(); // 태그 값 가져오기

          if (tagValue !== "") {
            // tag 안에 있는 값을 하나씩 순회하면서 검사
            const result = Object.values(tag.value).filter(function (word) {
              return word === tagValue;
            });

            // 태그 중복방지 (바로 전것과 비교)
            if (result.length == 0) {
              // 태그 추가 및 개별 css 적용
              $("#tag-list").append(
                "<span class='tag-item' style='margin: 0 8px 7px 0; display: inline; background-color:rgb(101, 172, 139); border-radius: 5px; padding: 8px; font-weight:400; '>" +
                  tagValue +
                  "<span class='del-btn' style='cursor:pointer; margin:0px 3px;' idx='" +
                  counter.value +
                  "'>X</span></span>"
              );
              let totalWidth = 0;
              $("#tag-list > span").each((index, item) => {
                totalWidth += $(item).width() + 8;
              });
              adjustHeight.value = computed(() => {
                return Math.ceil(totalWidth / $("#tag-list").width()) * 40;
              });
              console.log(adjustHeight.value.value);
              addTag(tagValue);
              self.val("");
              emit("search-hash-tag", tag.value);
            } else {
              alert("태그값이 중복됩니다.");
            }
          }
          // 스페이스 시 빈공간 방지
          e.preventDefault();
        }
      });

      // 삭제
      $(document).on("click", ".del-btn", function () {
        const index = $(this).attr("idx");
        // 해당 번호 삭제
        tag.value.splice(index, 1);
        // del 버튼이 속해있는 li 태그를 삭제
        $(this).parent().remove();
        emit("search-hash-tag", tag.value);
      });
    });
    return {
      reset,
      adjustHeight,
    };
  },
};
</script>

<style scoped>
/* li 태그 앞에 점 제거 */
#tag-list {
  padding: 0px;
  max-width: 100%;
  max-height: 100%;
}

ul > li {
  margin-bottom: 20px;
}

#tag {
  border: 1px solid #c5c6cc;
  border-radius: 12px;
  padding: 8px;
}

#reset {
  float: right;
  font-size: 14px;
  margin: 5px;
  cursor: pointer;
}
</style>
