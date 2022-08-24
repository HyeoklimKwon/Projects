<template>
  <div class="row" id="top_box">
    <div class="col-2" id="top_box_text" @click="moveToPrevious"><img src="@/assets/icons/arrow-left.png" /></div>
    <h5 class="col-8" id="top_box_text">스케줄</h5>
    <div class="col-2" id="top_box_text"></div>
  </div>
  <div class="calendarbox" >
    <DatePicker :attributes='state.schedules' v-model ="date" is-expanded />   
  </div>
  <div>
    <hr>     
    <div class="d-flex justify-content-between ">
      <p  class="d-flex justify-content-between align-items-center" style="padding-top:4.2px; padding-left : 5px "><b>근무정보</b></p>
      <span style="  padding-right : 10px " @click="moveToRegisterSchedule" class="material-symbols-outlined">edit_calendar</span>
    </div>
    <div id="schedulebuttons" class="d-flex justify-content-center">
   
    <div v-if="state.isworkbuttonon">      
        <button @click="workon(date.getFullYear(),date.getMonth(),date.getDate())" class="scheduleworkbuttonon "><b >근무 보기</b></button>
        <button @click="breakon(date.getFullYear(),date.getMonth(),date.getDate())" class="schedulebreakbuttonoff "><b>휴무 보기</b></button>            
    </div>
    <div v-else>
      <button @click="workon(date.getFullYear(),date.getMonth(),date.getDate())" class="scheduleworkbuttonoff "><b >근무 보기</b></button>
      <button @click="breakon(date.getFullYear(),date.getMonth(),date.getDate())" class="schedulebreakbuttonon "><b>휴무 보기</b></button>
    </div>
    </div>
     <br>  
    <div v-if="state.isworkbuttonon">      
      <div v-for="(worker, i) in state.workers" :key="i">
        <div class="workbreakbox d-flex  align-items-center">
          <div style="padding-left: 20px">
            <b>                            
              근무  &nbsp;&nbsp; |  &nbsp;&nbsp;&nbsp;&nbsp;               
            </b>            
          </div >
          <div>
            <img id = "chatprofile" class="imgProfile" :src="HOST + worker.image" alt="">           
          </div>
          <div>
            <b>
              {{ longnicknametoshort(worker.nickname) }} &nbsp;&nbsp;:  &nbsp;&nbsp;   
            </b>
          </div>
          <div>
            <b>
              {{worker.crew_starthour.substr(0,5)}}~{{worker.crew_endhour.substr(0,5)}}
            </b>
          </div>
        </div>
        <br>
      </div>
    </div>
    <div v-else>
      <div v-for="(worker, i) in state.workers" :key="i">
        <div class="breakworkbox d-flex  align-items-center">
          <div style="padding-left: 20px">
            <b>              
              휴무  &nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;  
            </b>            
          </div>
          <div>
            <b>
              <img id = "chatprofile" class="imgProfile" :src="HOST + worker.image" alt="">{{ longnicknametoshort(worker.nickname) }}
            </b>
          </div>
        </div>
        <br>
      </div>     

    </div> 

   
  
  </div>
     
</template>

<script >
import { useRoute, useRouter } from "vue-router";
import { ref, reactive, onMounted } from 'vue'
import axios from "@/api/axios.js"
import api from "@/api/api.js";
import popover from "bootstrap/js/dist/popover";


export default {
  setup() {
    const HOST = ref("https://i7b209.p.ssafy.io");    
    const router = useRouter();
    const route = useRoute()
    const date = ref(new Date())
    const crew_pk = Number(route.params.crew_pk)    
    const moveToRegisterSchedule = () => {
      router.push({ name: "scheduleregister" });
    };
    const state = reactive({
      schedules : [],
      isworkbuttonon : false,
      workers : [], 
    })

    onMounted( async () => {
      let schedules = [];
      await axios.get(api.crew.registercrewschedule(crew_pk)).then((response)=> {
        response.data.forEach(element => {
          console.log(element);         
          schedules.push({
            dot : element.color,
            dates : element.crew_day, 
            popover : {
              label : element.name+ " : "+ element.crew_starthour + "~" + element.crew_endhour,
              slot: 'todo-row',
               visibility: 'focus'
            }   

          })
          state.schedules = schedules
        });
      })
    })

    const logcon = (() => {
      console.log("hello");
    })

    const onedigittotwodigitmonth = ((month)=> {
      if ( Number(month) < 9) {
        return 0 + String(month+1)        
      } else {
        return month
      }
      
    })
    const onedigittotwodigitday = ((month)=> {
      if ( Number(month) < 10) {
        return 0 + String(month)        
      } else {
        return month
      }
      
    })

    const longnicknametoshort= ((nickname) => {
      if (nickname.length > 8) {
        return nickname.substr(0,5) + "..."        
      }
      return nickname

    })

    const workon = (async (workyear,workmonth,workdate) => {
      state.isworkbuttonon = true
      const finddate = workyear +"-"+ onedigittotwodigitmonth(workmonth) +"-"+ onedigittotwodigitday(workdate)       
      await axios.get(api.crew.getworklist(crew_pk, finddate),  {
        params : {
        work : 1
      }}).then((response)=>{
        state.workers = response.data
      } )

    })

    const breakon = (async (workyear,workmonth,workdate) => {
      state.isworkbuttonon = false
      const finddate = workyear +"-"+ onedigittotwodigitmonth(workmonth) +"-"+ onedigittotwodigitday(workdate)
      await axios.get(api.crew.getworklist(crew_pk, finddate),  {
        params : {
        work : 0
      }}).then((response)=>{
        console.log(response.data);
        state.workers = response.data
      } )
         
    })

    const moveToPrevious = () => {
      router.go(-1)
    }

    return {
     moveToRegisterSchedule,
     date,
     crew_pk,
     state,
     logcon,
     breakon,
     workon,
     onedigittotwodigitmonth,
     onedigittotwodigitday,
     HOST,
     longnicknametoshort,
     moveToPrevious
 
    }  
}
}
</script>

<style>
#top_box_text {
  /* display: flex; */
  text-align: center;
  line-height: 55px;
} 

#top_box {
  height: 55px;
  margin: auto;

  color: white;
  background-color: #498d6d;
}

.calendarbox{
  display : flex;
  justify-content: center;
  margin-left : 20px;
  margin-right: 20px;
  margin-top: 20px;
  border : solid seagreen;
  border-radius: 10px;
}

.scheduleworkbuttonon{
width: 131px;
height: 38px;
background: #1294F2;
border : solid rgb(120, 183, 238) 2px ;
border-radius: 20px;
margin-right : 13px;
}

.scheduleworkbuttonoff{
width: 131px;
height: 38px;
background: #D9D9D9;
border : solid rgb(164, 161, 161) 2px ;
border-radius: 20px;
margin-right : 13px;
}

.schedulebreakbuttonon{
  width: 131px;
  height: 38px;
  background: #1294F2;
  border : solid rgb(120, 183, 238) 2px;
  border-radius: 20px;
  margin-left : 13px;
}

.schedulebreakbuttonoff{
width: 131px;
height: 38px;
background: #D9D9D9;
border : solid rgb(164, 161, 161) 2px;
border-radius: 20px;
margin-left : 13px;

}

.workbreakbox {
  height: 100px ; 
  background-color: rgba(229, 141, 31, 0.55);
  border-radius: 20px;
  margin-left: 10px;
  margin-right: 10px;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
}

.breakworkbox {
  height: 100px ; 
  background-color: #D9D9D9;
  border-radius: 20px;
  margin-left: 10px;
  margin-right: 10px;
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
}

#chatprofile{
  width: 35px;
  height: 35px;
  border-radius: 70%;
  overflow: hidden;
  margin-right : 13px

}

.boxshawdow{
  box-shadow: 0px 4px 80px rgba(0, 0, 0, 0.07), 0px 0.893452px 17.869px rgba(0, 0, 0, 0.0417275), 0px 0.266004px 5.32008px rgba(0, 0, 0, 0.0282725);
}
</style>