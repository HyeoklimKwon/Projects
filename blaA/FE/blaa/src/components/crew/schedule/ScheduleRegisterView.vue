<template>
  <br>  
   
    <div class="calendarbox">
      <br>
      <DatePicker style="overflow: scroll;" v-model="range" mode = "dateTime" is-range  is-expanded>
        <template v-slot = "{ inputValue, inputEvents }">
        <hr>
          <div class="group">
            <label class="button groupItem" for="start">Start &nbsp;</label>
            <input type="text" id="start" :value="inputValue.start" v-on="inputEvents.start" class="input">
            <hr>
            <label class="button groupItem" for="end">End &nbsp;&nbsp;</label>
            <input type="text" id="end" :value="inputValue.end" readonly class="input">  
          </div>              
          <hr>
          <form style="m">  
            <div class="form-group">
              <select  name="color" @change="putcolor($event)" class="form-control" id="exampleFormControlSelect1">
                <option value="">근무 선택</option>
                <option value="grey">휴가</option>
                <option value="red">오전 근무</option>
                <option value="blue">오후 근무</option>
                <option value="purple">풀타임</option>
                <option value="teal">대타</option>
              </select>
            </div>                    
          </form>
          <br>
          <div class="d-flex justify-content-center">
            <b-button pill variant="success" @click.prevent="showtime(inputValue.start, inputValue.end)">등록하기</b-button>
            <div>&nbsp;</div>  
            <b-button pill variant="outline-danger" @click="moveToSchedule">뒤로가기</b-button>            
          </div>
          <br>
        </template>
      </DatePicker>
      <br>         
    </div>

 
     
</template>

<script>

import { useRoute, useRouter } from 'vue-router'
import { ref, reactive } from 'vue'
import { useStore } from "vuex";
import axios from "@/api/axios.js"
import api from "@/api/api.js";


export default {
   
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter();
    const input = ref("")
    const crew_pk = route.params.crew_pk
    const date = ref(new Date())
    const userInfo = store.state.account.userInfo;
    date.value.setDate(Number(date.value.getDate()))

    const range = reactive({
      start : new Date(),
      end : date.value,     

    })
    const info = reactive({
      color : "",
      crew_pk : crew_pk,
      user_pk : userInfo.user_pk,
      content : "",
    })

    const daytoString = ((a) => {
      return a.slice(0,4) +"-"+ a.slice(5,7) +"-"+ a.slice(8,10)
    })
    const timetoString = ((a) => {
      if (a[12] == ":") {        
        if (a.slice(16,18) == "PM") {
          return  String(Number(a[11]) + 12)+ ":" + a.slice(13,15); 
        } else {
          return "0" +a[11] + ":" + a.slice(13,15);
        } 
              
      } else {        
        if (a.slice(17,19) == "PM") {
          return String(Number(a.slice(10,13)) + 12) + ":" + a.slice(14,16);          
        } else {
          return  a.slice(10,13)  + ":" + a.slice(14,16);
        }  
      }                  
    })
    const showtime =  (async (a,b) => {
      console.log("crew_day :" + daytoString(a));
      console.log("color :" + info.color);
      console.log("crew_starthour :" + timetoString(a));
      console.log("crew_endhour :" + timetoString(b));
      console.log("user :" + userInfo.user_pk);
      
      // const data = {
      //   crew_day : daytoString(a),
      //   color : info.color,
      //   crew_starthour : timetoString(a),
      //   crew_endhour : timetoString(b),             
      // }             
      await axios.post(api.crew.registercrewschedule(info.crew_pk), {
        crew_day : daytoString(a),
        color : info.color,
        crew_starthour : timetoString(a),
        crew_endhour : timetoString(b),      
        user : Number(userInfo.user_pk)             
      }).then((response) => {
        console.log(response);
        moveToSchedule()

      })
    })


    const putcolor = ((event) => {
      info.color = event.target.value
    })

    const moveToSchedule = (() => {
      router.push({ name: "schedule" });   
    })
    
    // const showresult = (() => {
    //   console.log(state.date);
    // })

    return {
      crew_pk,
      range,
      showtime,
      putcolor,
      input,
      moveToSchedule,
      info,
      date,
      daytoString,
      timetoString
      // showresult
    }
  
}
}
</script>

<style>
.calendarbox{
  display : flex;
  justify-content: center;
  margin-left : 20px;
  margin-right: 20px;
}

</style>