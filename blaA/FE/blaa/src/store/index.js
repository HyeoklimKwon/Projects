import { createStore } from "vuex";
import test from "./modules/test";
import chat from "./modules/chat";
import crew from "./modules/crew";
import story from "./modules/story";
import account from "./modules/account";
import review from "./modules/review";
import profile from "./modules/profile";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  modules: {
    //
    test,
    chat,
    crew,
    story,
    account,
    review,
    profile,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
});
