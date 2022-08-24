<template>

  <div id="storyParrents" class="justify-content-center">
    <h3>내 스토리</h3>
    <div id="story"></div>
    <!-- <p>{{myStoryList}}</p> -->
  </div>
  
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { onMounted } from "vue";
import axios from "@/api/axios.js";
import api from "@/api/api.js";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();
    const HOST = "https://i7b209.p.ssafy.io";

    const myStoryList = store.state.profile.myStory;
    console.log("myStory : ", myStoryList);

    const storyDetail = (story_pk) => {
      router.push({
        name: "detailStory",
        params: {
          story_pk: story_pk,
        },
      });
    };
    onMounted(() =>{
      console.log(myStoryList)
      const storyDateList = []
    // const length_story = myStoryList.length()
      for (let story of myStoryList){
        
        if (storyDateList.includes(story.created_at.substr(0,10))){
        
          const div = document.getElementsByClassName(`${story.created_at.substr(0,10).replaceAll('-','')}`)[0]
          const Img = document.createElement("img");
          Img.setAttribute('src',"https://i7b209.p.ssafy.io"+story.story_picture)
          Img.setAttribute('id',"imgStory")
          Img.classList.add('mb-5','mx-3')
          Img.onclick = function() {storyDetail(story.story_pk)}
          // Img.setAttribute('@click',`storyDetail(${story.story_pk})`)
          div.appendChild(Img)
      }else {
        storyDateList.push(story.created_at.substr(0,10))
        let parrents = document.querySelector('#story')

        const div = document.createElement('div')
        div.classList.add(`${story.created_at.substr(0,10).replaceAll('-','')}`)

        parrents.append(div)

        const hr = document.createElement('hr');
        div.appendChild(hr)
        const h5 = document.createElement('h5')
        h5.setAttribute('class','dateClass')
        h5.innerText = story.created_at.substr(0,10)
        div.appendChild(h5)
        const Img = document.createElement("img");
        Img.setAttribute('src',"https://i7b209.p.ssafy.io"+story.story_picture)
        Img.setAttribute('id',"imgStory")
        Img.classList.add('mb-5','mx-3')
        Img.onclick = function() {storyDetail(story.story_pk)}
        // Img.setAttribute('onclick',`storyDetail(${story.story_pk})`)
        div.appendChild(Img)

      }
      }

    })
    return {
      HOST,
      myStoryList,
      storyDetail,
    };
  },
};
</script>

<style>
#imgStory {
  width: 40%;
  height: 40%;
}
.dateClass{
  font-weight: bold;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
