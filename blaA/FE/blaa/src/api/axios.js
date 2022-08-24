import Axios from "axios";

const axios = Axios.create({});

axios.interceptors.request.use(
  (config) => {
    let token = sessionStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }
)

export default axios;