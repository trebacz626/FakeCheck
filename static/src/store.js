import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);
export const store = new Vuex.Store({
  state: {
    base_url: '',
    current_account_id: null
  },
  mutations: {
    setCurrentAccount(state, account_id) {
      state.current_account_id = account_id;
    }
  },
  getters: {
    currentAccountId: state => {
      return state.current_account_id;
    },
    baseUrl: state => {
      return state.base_url;
    }
  }
});