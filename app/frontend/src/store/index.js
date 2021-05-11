import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import postcodes from './modules/postcodes';
import threefiver from './modules/threefiver';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    postcodes,
    threefiver
  }
});