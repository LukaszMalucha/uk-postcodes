import api from "../../api/api.js"

const state = {
  token: window.localStorage.getItem('token'),
  username: window.localStorage.getItem('username'),
  error: null
};


const getters = {
// Check if token exists or not
  isLoggedIn: state => !!state.token || !!state.username,
  getUsername: state => state.username,
  getToken: state => state.token,
  getError: state => state.error,
};


const actions = {
  async getUserInfo({ commit }) {
    const response = await api.userInfo();
    if (response["email"]) {
      const username = response["email"];
      commit('setUsername', username);
      window.localStorage.setItem('username', username);
    }
    else {
      commit('setUsername', null);
    }

  },
};


const mutations = {
// Update user
  setUsername: (state, username) => {
    state.username = username
  },
};


export default {
  state,
  getters,
  actions,
  mutations
}