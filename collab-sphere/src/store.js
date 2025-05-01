import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      isAuthenticated: JSON.parse(localStorage.getItem('isAuthenticated')) || false,
      user: null,
      authtoken: localStorage.getItem('authtoken') || null,
    };
  },
  mutations: {
    setAuthenticated(state, payload) {
      state.isAuthenticated = payload;
    },
    setUser(state, userData) {
      state.user = userData;
    },
    setAuthToken(state, token) {
      state.authtoken = token;
      localStorage.setItem('authtoken', token);
    },
  },
  actions: {
    login({ commit }, userData) {
      commit('setAuthenticated', true);
      commit('setUser', userData);
      commit('setAuthToken', userData.token); // Assuming userData contains the token
    },
    logout({ commit }) {
      commit('setAuthenticated', false);
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
    authtoken: (state) => state.authtoken,
  },
});

export default store;