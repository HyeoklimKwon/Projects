import axios from 'axios'
import api from '@/api/api'

export default {
  namespaced: true,
  state: {
    token : sessionStorage.getItem('token'),
    messages : [],
    to_userProfile : "",
    from_userProfile : "",
    allusers : [],
  },
  mutations: {
    GET_TOPROFILE(state, userpk) {
      state.to_userProfile = userpk
    },
    GET_ALLUSERS(state, payload) {
      state.allusers = payload
    },
  },
  actions: {
    async getToProfile({commit, state}, userpk) {
      try {        
        const res = await axios.get(api.accounts.pkinfo(userpk), {
          headers: {
            Authorization: `Baerer ${state.token}`
          }
        })
        commit('GET_TOPROFILE',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },

    async getAllUsers({commit, state}) {
      try {        
        const res = await axios.get(api.accounts.searchallusers(), {
          headers: {
            Authorization: `Bearer ${state.token}`
          }
        })
        commit('GET_ALLUSERS',res.data)
      } catch(error) {
        // 에러 발생시
        console.log(error)
      }
    },

  },
  getters: {},
};
