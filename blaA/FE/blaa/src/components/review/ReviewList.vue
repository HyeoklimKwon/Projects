<template>
  <div class="store" @click="moveToDetail">
    <img :src="replaceUrl.value" alt="이미지">
    <br>
    <p>{{review.name}}</p>
  </div>
  
</template>

<script>
import { computed } from '@vue/runtime-core'
import { useRouter } from 'vue-router'
export default {
  props: {
    review: {
      type: Array
    }
  },
  setup(props) {
    const router = useRouter()
    const replaceUrl = computed(() => {
      return props.review.image.replace('media/', 'api/v1/')
    })

    console.log(replaceUrl.value)
    
    const moveToDetail = () => {
      router.push({
        name: 'detailReview',
        params: {
          store_pk: props.review.store_pk,
          store_name: props.review.name
        }
      })
    }
    return {
      moveToDetail,
      replaceUrl
    }
  }
}
</script>

<style scoped>
.store {
  cursor:pointer;
  padding: 5px;
  margin: 5px;
  border-radius: 10px;
  background-color: rgb(202, 255, 197);
}
p {
  margin: 0
}
</style>