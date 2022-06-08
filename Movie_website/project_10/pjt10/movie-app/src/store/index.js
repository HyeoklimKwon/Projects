import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {
  },
  mutations: {
    CREATE_MOVIE(state, newMovie) {
      state.movies.push(newMovie)
    },
    DELETE_MOVIE(state, movieItem) {
      const index = state.movies.indexOf(movieItem)
      state.movies.splice(index, 1)
    },
    SET_LOADING(state, data){
      state.loading = data;
    },
    SET_NOW_PLAYING(state, data){
      state.nowPlaying = data;
    },
  },
  actions: {
    createMovie({ commit }, newMovie){
      commit('CREATE_MOVIE', newMovie)
    },
    deleteMovie({ commit }, movieItem){
      commit('DELETE_MOVIE', movieItem)
    }
  },  
})
