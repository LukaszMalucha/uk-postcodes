import api from "../../api/api.js"

const state = {
  numbers: null,

};


const getters = {
  getNumbers: state => state.numbers,

};


const actions = {
  async fetchThreeFiver({commit}, payload) {

    const response = await api.threeFiver(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    } else {
      commit("setNumbers", response.numbers);
    }

  },

};


const mutations = {
  setNumbers: (state, numbers) => {
    state.numbers = numbers
  },

};


export default {
  state,
  getters,
  actions,
  mutations
}