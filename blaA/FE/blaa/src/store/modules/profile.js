import axios from "@/api/axios.js";
import api from "@/api/api.js";

const profileStore = {
  namespaced: true,
  state: {
    updateMyInfo: [],
    myFollower: [],
    myFollowing: [],
    myStory: [],
    myReview: [],
    myCrew: [],
    myInfo: [],
  },
  mutations: {
    UPDATE_MY_INFO: (state, myInfo) => {
      state.myInfo = myInfo;
    },
    GET_MY_FOLLOWER: (state, myFollower) => {
      state.myFollower = myFollower;
    },
    GET_MY_FOLLOWING: (state, myFollowing) => {
      state.myFollowing = myFollowing;
    },
    GET_MY_STORY: (state, myStory) => {
      state.myStory.push(myStory);
    },
    GET_MY_REVIEW: (state, myReview) => {
      state.myReview = myReview;
    },
    GET_MY_CREW: (state, myCrew) => {
      state.myCrew = myCrew;
    },
    GET_MY_INFO: (state, myInfo) => {
      state.myInfo = myInfo;
    },
  },
  actions: {
    updateMyInfo(context, user_pk) {
      axios
        .put(api.profile.updateMyInfo(user_pk))
        .then((response) => {
          context.commit("");
        })
        .catch((err) => {});
    },
    getMyFollower(context, user_pk) {
      axios
        .get(api.profile.myFollow(user_pk), {
          params: {
            type: "follow",
          },
        })
        .then((response) => {
          console.log("팔로우 response", response);
          console.log("response data : ", response.data);
          const followerData = {
            count: null,
            next: null,
            previous: null,
            results: [],
          };
          console.log(response.data.count);
          followerData.count = response.data.count;
          followerData.next = response.data.next;
          followerData.previous = response.data.previous;
          followerData.results = response.data.results;

          context.commit("GET_MY_FOLLOWER", followerData);
        })
        .catch((err) => {
          console.log("팔로우 err : ", err);
        });
    },
    getMyFollowing(context, user_pk) {
      axios
        .get(api.profile.myFollow(user_pk), {
          params: {
            type: "following",
          },
        })
        .then((response) => {
          console.log("팔로잉 response", response);
          console.log("response data : ", response.data);
          const followingData = {
            count: null,
            next: null,
            previous: null,
            results: [],
          };
          console.log(response.data.count);
          followingData.count = response.data.count;
          followingData.next = response.data.next;
          followingData.previous = response.data.previous;
          followingData.results = response.data.results;

          context.commit("GET_MY_FOLLOWING", followingData);
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getMyStory(context, user_pk) {
      axios.get(api.profile.myStory(user_pk)).then((response) => {
        console.log("response : ", response);
        console.log("response data : ", response.data);

        context.commit("GET_MY_STORY", response.data);
        console.log("state myStory", context.state.myStory);
      });
    },
    getMyReview(context, user_pk) {
      axios
        .get(api.profile.myReview(user_pk))
        .then((response) => {
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getMyCrew(context, user_pk) {
      axios
        .get(api.profile.myCrew(user_pk), {})
        .then((response) => {
          console.log("crew response", response);
          context.commit("GET_MY_CREW", response.data);
        })
        .catch((err) => {
          console.log("crew error : ", err);
        });
    },
    getMyInfo(context, user_pk) {
      axios.get(api.profile.myInfo());
    },
  },
};

export default profileStore;
