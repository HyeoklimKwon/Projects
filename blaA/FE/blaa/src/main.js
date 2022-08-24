import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue3 from "bootstrap-vue-3";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-3/dist/bootstrap-vue-3.css";
import "v-calendar/dist/style.css";
import { Calendar, SetupCalendar, DatePicker } from "v-calendar";

window.Kakao.init(process.env.VUE_APP_KAKAO_JAVASCRIPT);

createApp(App).use(store).use(router).use(BootstrapVue3).use(SetupCalendar).component("DatePicker", DatePicker).component("Calendar", Calendar).mount("#app");
