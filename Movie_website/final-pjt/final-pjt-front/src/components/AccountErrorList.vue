<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field">
      <br>      
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          <p> 
            {{ error }}
          </p>          
        </li>
      </ul>
    </p>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
