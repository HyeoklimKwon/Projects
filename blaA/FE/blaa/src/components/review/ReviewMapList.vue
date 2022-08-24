<template>
  <hr>
  <div @click="selectStore" style="cursor: pointer">
    <div v-if="isStore">
      <p>{{ searchChild.place_name }}</p>
      <p>{{ searchChild.address_name }}</p>
    </div>
    <div v-else>
      <p>{{ searchChild.name }}</p>
      <p>{{ searchChild.region }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    searchChild: Object,
    isStore: Boolean
  },
  emits: ['select-store'], 
  setup(props, {emit}) {
    const selectStore = () => {
      if (props.isStore) {
        const data = {
          store_pk: 0,
          name: props.searchChild.place_name,
          region: props.searchChild.address_name
        }
        emit('select-store', data)  
      } else {
        const data = {
          store_pk: props.searchChild.store_pk,
          name: props.searchChild.name,
          region: props.searchChild.region
        }
        emit('select-store', data)  
      }  
    }
    return {
      selectStore
    }
  }
}
</script>

<style>

</style>