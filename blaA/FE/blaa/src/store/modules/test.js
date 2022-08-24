import axios from "axios";
import api from "@/api/api";

export default {
  namespaced: true,
  state: {
    //
    data: "잘 나오고 있습니다.",
  },
  mutations: {},
  actions: {
    // api는 아래와 같이 작성
    test() {
      axios.get(api.accounts.login()).then((res) => {
        console.log(res.data);
      });
    },
  },
  getters: {
    example(state) {
      return state.data + " 예제입니다";
    },
  },
};
