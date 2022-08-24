<template>
  <div class="my-modal">
    <div class="overlay" @click="$emit('close-modal')">
      <div class="modal-card">
        <!-- 여기에 원하는 대로 자신이 커스텀 할 수 있음 -->
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .my-modal, .overlay {
    width: 100%;
    height: 100%;
    /* 상단에 고정되어 있어야 하므로 */
    position: fixed;
    /* top: 0px;
    left: 0px; */
  }
  /* 모달이 떳을 떄 뒤에 배경화면을 안보이게 */
  .overlay {
    background-color:rgba(255,255,255,0.5);
  }

  .modal-card {
    position: relative;
    max-width: 80%;
    margin:auto;
    margin-top: 30px;
    padding: 20px;
    background-color: white;
    min-height: 300px;
    z-index:10;
    opacity: 1 !important;
  }
</style>