import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue3 from "bootstrap-vue-3";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-3/dist/bootstrap-vue-3.css";

window.Kakao.init("696e8169dd084134f8ba85be092a70cb");

createApp(App).use(store).use(router).use(BootstrapVue3).mount("#app");
