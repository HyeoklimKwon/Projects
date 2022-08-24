import api from '@/api/api'
import axios from 'axios'
import { dataChange } from '@/hooks/dateChange'

export default {
  namespaced: true,
  state: {
    reviews: [],
    total_reviews: 0,
    review: [],
    reviewBtn: [],
    reviewStar: 0,
    detailReview: [],
    searchStores: [],
    Token: sessionStorage.getItem('token')
  },
  mutations: {
    GET_REVIEWS(state, payload){
      state.reviews = payload
    },
    GET_REVIEW(state, payload){
      const {
        yyyyMMdd
      } = dataChange()

      state.reviewStar = payload.splice(-1, 1)[0].review_star_static
      state.reviewBtn = payload.splice(-1, 1)[0].review_button_static
      state.review = payload

      state.review.forEach(ele => {
        ele.created_at = yyyyMMdd(ele.created_at)
      })
      // 버튼 점수의 비율 계산
      if (state.review.length) {
        for (let type in state.reviewBtn) {
          state.reviewBtn[type] = (state.reviewBtn[type] / state.review.length)
        }
      }
    },
    GET_DETAIL_REVIEW(state, payload){
      const {
        yyyyMMdd
      } = dataChange()
      state.detailReview = payload
      state.detailReview['created_at'] = yyyyMMdd(state.detailReview['created_at'])
    },
    LIKE_ONE_REIVEW(state, payload){
      const review_pk = payload.review_pk
      // 해당값으로 리뷰를 갱신
      const idx = state.review.findIndex(ele => ele.review_pk == review_pk)
      state.review[idx].like_users = payload.like_users
      state.review[idx].like_user_count = payload.like_user_count
    },
    LIKE_DETAIL_REVIEW(state, payload) {
      state.detailReview.like_users = payload.like_users
      state.detailReview.like_user_count = payload.like_user_count
    },
    UPDATE_TOTAL_REVIEWS(state, payload) {
      state.total_reviews = payload
    }
  },
  actions: {
    async getReviews({commit, state}, data) {
      try {
        const res = await axios.get(api.review.store(), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          },
          params: {
            page: data.page,
            search: data.searchText
          }
        })
        commit('UPDATE_TOTAL_REVIEWS', res.data.count)
        commit('GET_REVIEWS', res.data.results)
      } catch(error) {
        console.error(error)
      } 
    },
    async getReview({commit, state}, store_pk) {
      try {
        const res = await axios.get(api.review.review(store_pk),{
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_REVIEW', res.data)
      } catch (error) {
        console.error(error)
      }
    },
    async getDetailReview({commit, state}, review_pk) {
      try {
        const res = await axios.get(api.review.reviewDetail(review_pk), {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        commit('GET_DETAIL_REVIEW', res.data)
      } catch (error) {
        console.error(error)
      }
    },
    async likeOneReview({commit, state}, data) {
      const review_pk = data.review_pk
      try {
        const res = await axios.post(api.review.like(review_pk), {}, {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        const data = {
          review_pk: review_pk,
          like_users: res.data.like_users,
          like_user_count: res.data.like_user_count
        }
        if (data.isDetail) {
          console.log(state.detailReview)
          commit('LIKE_DETAIL_REVIEW',data)
        } else {
          commit('LIKE_ONE_REIVEW', data)
        }
      } catch(error) {
        console.error(error)
      }
    },
    async makeReviews({state}, data) {
      const isStore = data.isStore
      const store = {
        form: data.form,
        store_pk: data.store_pk
      }
      const review = {
        oneline_review: data.oneline_review,
        star: data.star,
        chosen_button: data.type
      }
      // 스토어 정보가 없어 새로 생성시
      if (isStore) {
        try {
          console.log(data.name)
          // 한번 더 스토어 정보가 있나 확인
          const res = await axios.get(api.review.store(), {
            headers: {
              Authorization: `Bearer ${state.Token}`
            },
            params: {
              search: data.name
            }
          })
          // 그래도 없으면 생성 진행
          if (res.data.count == 0) {
            try {
              const res = await axios.post(api.review.store(), store.form, {
                headers: {
                  "Content-Type": "multipart/form-data",
                  Authorization: `Bearer ${state.Token}`
                }
              })
              store.store_pk = res.data.store_pk
            } catch (error) {
              console.error(error)
            }
          } else {
            store.store_pk = res.data.results[0].store_pk
          }
        } catch(error) {
          console.error(error)
        }
      }
      // 리뷰 생성
      try {
        const res = await axios.post(api.review.review(store.store_pk), review, {
          headers: {
            Authorization: `Bearer ${state.Token}`
          }
        })
        console.log(res.data)
      } catch(error) {
        console.error(error)
      }
    }
      
  },
  getters: {},
};
