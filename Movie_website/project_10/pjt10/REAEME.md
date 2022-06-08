## Pjt10 TIL

### 수업시간에 배웠던 TodoList 응용해서 MyMovieList 만들기

MovieListVeiw를 router와 이어지게해서 아래 components들이 보여줄 공간 생성하고 import를 한다.

```vue
<template>
  <div>
    <h1>My Movie List</h1>
    <watch-list-form></watch-list-form>   
    <watch-list></watch-list> 
  </div>
</template>

<script>
import WatchList from '@/components/WatchList.vue'
import WatchListForm from '@/components/WatchListForm.vue'


export default {
  name: 'WatchListView',
  components: {
    WatchList, WatchListForm    
  },
}
</script>

<style>

</style>
```

components 폴더에 WatchList, WatchListForm, WatchListItem 등을 생성하여 MovieListView를 구성해준다. 

 WatchListItem 생성하고

``` vue
<template>
    <div>
        {{ movie.title }}
        <button @click="deleteMovie">x</button>
    </div>
  
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'WatchListItem',
    props: {
        movie: Object,
    },
    methods: {
        ...mapActions(['craeteMovie', 'deleteMovie']),

    }

}
</script>

<style>

</style>
```

이 WatchListItem을 담아준다.

```vue
<template>
    <div>
        <watch-list-item
        v-for=" movie in movies"
        :key="movie.date"
        :movie = "movie">
        </watch-list-item>
    </div>
  
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'

export default {
    name: 'WatchList',
    components: { WatchListItem },
    computed: {
        movies() {
            return this.$store.state.movies
        }
    }
  

}
</script>

<style>

</style>
```

그리고 WatchListForm 즉, 추가 할 수 있는 버튼을 만들어준다.

```vue
<template>
  <div>      
      <input type="text" 
      v-model.trim="movieTitle"
      @keyup.enter="createMovie">
      <button
      @click="createMovie">Add</button>
  </div>
</template>

<script>
export default {
    name: 'WatchListForm',
    data() {
        return {
            movieTitle: ''
        }
    },
    methods: {
        createMovie() {
            const newMovie = {
                title: this.movieTitle,
                isCompleted: false,
                date: new Date().getTime()
            }
            this.$store.dispatch('createMovie', newMovie)
            this.movieTitle = ''
        }
    }
}
</script>

<style>

</style>
```



### Axios를 이용하여 tmdb에서 영화 정보 받기

```javascript
import axios from "axios";

const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: "86be6a224df194a9a21faf6e63e1b00b",
    language: "ko-KR",
  },
});

export const movieApi = {
  nowPlaying: () => request.get("movie/now_playing"),    
  movieDetail: (id) =>
    request.get(`movie/${id}`, {
      params: { append_to_response: "videos" },
    }),      
};

```

axios를 이용해서 movieApi에 영화정보들을 담는다. 

