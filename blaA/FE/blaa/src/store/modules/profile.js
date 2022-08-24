import axios from "@/api/axios.js";
import api from "@/api/api.js";

const profileStore = {
  namespaced: true,
  state: {
    followerList: null,
    followingList: null,
    myStory: [],
    reviewList: [],
    crewList: [],
  },
  mutations: {
    GET_FOLLOWER_LIST: (state, followerList) => {
      state.followerList = followerList;
    },
    GET_FOLLOWING_LIST: (state, followingList) => {
      state.followingList = followingList;
    },
    GET_MY_STORY: (state, myStory) => {
      state.myStory = myStory;
    },
    GET_REVIEW_LIST: (state, reviewList) => {
      state.reviewList = reviewList;
    },
    GET_CREW_LIST: (state, crewList) => {
      state.crewList = crewList;
    },
  },
  actions: {
    async getFollowerList(context, user_pk) {
      await axios
        .get(api.profile.myFollow(user_pk), {
          params: {
            type: "follower",
          },
        })
        .then((response) => {
          context.commit("GET_FOLLOWER_LIST", response.data);
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getFollowingList(context, user_pk) {
      await axios
        .get(api.profile.myFollow(user_pk), {
          params: {
            type: "following",
          },
        })
        .then((response) => {
          console.log("팔로잉 response", response);
          context.commit("GET_FOLLOWING_LIST", response.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getMyStory(context, user_pk) {
      await axios.get(api.profile.myStory(user_pk)).then((response) => {
        console.log("response : ", response);
        console.log("response data : ", response.data);

        context.commit("GET_MY_STORY", response.data);
        console.log("state myStory", context.state.myStory);
      });
    },
    async getReviewList(context, user_pk) {
      await axios
        .get(api.profile.myReview(user_pk))
        .then((response) => {
          console.log("review response :  ", response);
          context.commit("GET_REVIEW_LIST", response.data);
        })
        .catch((err) => {
          console.log("review err : ", err);
        });
    },
    async getCrewList(context, user_pk) {
      await axios
        .get(api.profile.myCrew(user_pk), {})
        .then((response) => {
          console.log("crew response", response);
          context.commit("GET_CREW_LIST", response.data);
        })
        .catch((err) => {
          console.log("crew error : ", err);
        });
    },
  },
};

export default profileStore;
