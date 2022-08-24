<template>
  <div class="tr_hashTag_area">
    <p><strong>해시태그 구현</strong></p>
    <div class="form-group">
      <input type="hidden" value="" name="tag" id="rdTag" />
    </div>

    <ul id="tag-list"></ul>
                
    <div class="form-group">
      <input type="text" id="tag" size="7" placeholder="엔터로 해시태그를 등록해주세요." style="width: 300px;"/>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import { ref } from 'vue'

export default {
  setup(props, {emit}) {
    // 문서가 준비되었으면 해당 함수를 실행
    $(document).ready(function() {
      // 해시태그가 Array 형태로 저장되어 있음
      const tag = ref([])
      const counter = ref(0)

      function addTag (value) {
        tag.value.push(value)
        counter.value += 1
      }

      // marginTag는 필더를 사용해 tag안에 값을 array로 넘긴다.
      function marginTag () {
        return Object.values(tag).filter(function (word) {
          return word !== ""
        })
      }
      
      // 클라이언트에 제공
      $('#tag-form').on('submit', function() {
        const value = marginTag() // tag Array를 반환
        $('#rdTag').val(value)

        $(this).submit()
      })

      $('#tag').on('keypress', function(e) {
        const self = $(this)

        // 엔터나 스페이스바를 입력하였을 떄 실행
        if (e.key === 'Enter' || e.keyCode == 32) {
          const tagValue = self.val() // 태그 값 가져오기

          if (tagValue !== ""){
            // tag 안에 있는 값을 하나씩 순회하면서 검사
            const result = Object.values(tag.value).filter(function (word) {
              return word === tagValue
            })

            // 태그 중복방지 (바로 전것과 비교)
            if (result.length == 0){
              // 태그 추가 및 개별 css 적용
              $('#tag-list').append("<li class='tag-item' style='display: inline; margin-left: 5px; background-color:greenyellow; border-radius: 5px; padding: 0px 5px 0px 5px;'>" + tagValue + "<span class='del-btn' style='cursor:pointer' idx='"+counter.value+"'>x</span></li>")
              addTag(tagValue)
              self.val("")
            } else {
              alert("태그값이 중복됩니다.")
            }
          }
          // 스페이스 시 빈공간 방지
          e.preventDefault()
        }
      })
      // 삭제
      $(document).on('click', '.del-btn', function() {
        const index = $(this).attr('idx')
        // 해당 번호 삭제
        tag.value.splice(index, 1)
        // del 버튼이 속해있는 li 태그를 삭제
        $(this).parent().remove()
      })
      emit('search-hash-tag', tag.value)
    }) 
  }
}
</script>

<style scoped>
/* li 태그 앞에 점 제거 */
ul {
  list-style: none;
}
.tag-item {
  background-color: greenyellow;
  border-radius: 50%;
}
</style>