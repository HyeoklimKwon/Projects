import axios from "axios";
import api from "@/api/api.js";

async function login(user, success, fail) {
  await axios.post(api.accounts.login(), user).then(success).catch(fail);
}

async function findByToken(token, success, fail) {
  await axios
    .get(api.accounts.currentUserInfo(), {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then(success)
    .catch(fail);
}

export { login, findByToken };
