import api from "../../api/api.js"

const state = {
  formError: null,
  result: null,
  postcode: null,
};


const getters = {
  getFormError: state => state.formError,
  getResult: state => state.result,
  getPostcode: state => state.postcode,
};


const actions = {
  async fetchStandardValidation({commit}, payload) {
    commit("setPostcode", null);
    const response = await api.standardValidation(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    } else {
      commit("setResult", response.result);
      var trimmedPostcode = payload.postcode.replace(" ", "");
      commit("setPostcode", trimmedPostcode);

      console.log(response.result);
      setTimeout(() => document.getElementById("result").style.display = "none", 6000);
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
  },
  setPostcode: (state, postcode) => {
    state.postcode = postcode
  },
};


export default {
  state,
  getters,
  actions,
  mutations
}