<template>
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li v-if="currentPage !== 1" class="page-item"><a class="page-link" href="#" @click="Onclick(1)">&lt;&lt;</a></li>
    <li v-if="currentPage > 5" class="page-item"><a class="page-link" href="#" @click="Onclick((idx -1)*5 + 1)">&lt;</a></li>
    <!-- 페이지네이션 5개씩 쪼개서 만들기 -->
    <li v-for="page in pageList" :key="page" class="page-item" :class="currentPage === page ? 'active' : ''"><a class="page-link" href="#" @click="Onclick(page)">{{ page }}</a></li>
    <li v-if="nextList" class="page-item"><a class="page-link" href="#" @click="Onclick((idx + 1)*5 + 1)">&gt;</a></li>
    <li v-if="numberOfPages !== currentPage" class="page-item"><a class="page-link" href="#" @click="Onclick(numberOfPages)">&gt;&gt;</a></li>
  </ul>
</nav>
</template>

<script>
import { computed, ref } from '@vue/runtime-core'
export default {
  props: {
    currentPage: {
      type: Number,
      required: true
    },
    numberOfPages: {
      type: Number,
      required: true
    },
    idx: {
      type: Number,
      required: true
    }
  },
  emits: ['click'],
  setup(props, {emit}) { 
    const nextList = computed(() => {
      return Math.floor(props.numberOfPages / 5) > (props.currentPage - 1) / 5
    })

    const pageList = computed(() => {
      const list = ref([])
      if ((props.idx + 1) * 5 > props.numberOfPages) {
        for (let num = (props.idx * 5)+ 1; num <= props.numberOfPages; num++) {
          list.value.push(num)
        }
      } else {
        for (let num = (props.idx * 5)+ 1; num <= ((props.idx + 1) * 5); num++) {
          list.value.push(num)
        }
      }
      return list.value
    })
    
    const Onclick = (page) => {
      emit('click', page)
    }
    return {
      Onclick,
      pageList,
      nextList
    }
  }
}
</script>

<style scoped>
.activate {
  background-color: blue;
}
</style>