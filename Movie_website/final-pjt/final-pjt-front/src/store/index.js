import Vue from 'vue'
import Vuex from 'vuex'



import movies from './modules/movies'
import articles from './modules/articles'
import accounts from './modules/accounts'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, movies, articles },
})

