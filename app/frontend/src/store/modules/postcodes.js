import api from "../../api/api.js"

const state = {
  formError: null,
  result: null,
};


const getters = {
  getFormError: state => state.formError,
  getResult: state => state.result
};


const actions = {
  async fetchStandardValidation({commit}, payload) {
    const response = await api.standardValidation(payload)
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    } else {
      commit("setResult", response.result);
      setTimeout(() => document.getElementById("result").style.display = "none", 5000);
    }

  },
  performSetFormError({commit}, error) {
    commit("setFormError", error);
  },
};


const mutations = {
  setFormError: (state, formError) => {
    state.formError = formError
  },
  setResult: (state, result) => {
    state.result = result
  }
};


export default {
  state,
  getters,
  actions,
  mutations
}