<template>
  <div class="background6">
      <button @click= "goBack" style="float: left;">
          <img style="width: 70px" src="@/assets/exit.jpg" alt="">          
      </button>
      <h1 style="color: white ; font-family: 'Nanum Pen Script', cursive; font-size: 75px; margin-right: 100px">{{ movie.title }}</h1>     
      
      <div id="app">        
        <TheSearchBar @set-input-value="setInputValue" />
        <main id="video-main">
        <div style="display: flex; justify-content: center; margin-top: 55px; margin-left: 180px" class="video-detail-container">
            <VideoDetail
          v-if="selectedVideo"
          :selected-video="selectedVideo"
        />      
        </div>
      
    </main>
  </div>

  </div>
</template>

<script>
 import axios from 'axios'
 import { mapGetters} from 'vuex'

 import TheSearchBar from '@/components/TheSearchBar'
 import VideoDetail from '@/components/VideoDetail'


export default {
    name: "TheaterView",
    components: {
    TheSearchBar,
    VideoDetail
       
  },
    data() {
    return {
      inputValue: '',
      videos: [],      
      selectedVideo: null,
    }
  },
    computed: {
      ...mapGetters(['movie'])
    },
    methods: {
        goBack(){
            this.$router.go(-1); [2]
        },

        setInputValue() {
      this.inputValue = this.movie.title + '결말 포함'
      // 요청
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const config = {
        params: {
          key: 'AIzaSyCymcXcXQMs4rRVgDT_1mWTZaSRK9OPAvk',
          part: 'snippet',
          type: 'video',
          q: this.inputValue
        }
      }

      axios.get(API_URL, config)
        .then(response => {
          this.videos = response.data.items
          this.selectedVideo = this.videos[0]          
          console.log(this.selectedVideo.id.videoId);                    
        })
    },    
    },
    created() {
        console.log(this.movie.title);
    }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
#TheaterView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#video-main {
  display: flex;
}

.video-detail-container {
  width: 80vw;
}
.background6{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/theaterbackground.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  
}
</style>