import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import ApiService from '../services/api.service'


Vue.use(Vuex)

export default new Vuex.Store({
// export default ({
  state: {
    publicKey: '',
  },
  mutations: {
    setPublicKey (state, publicKey) {
      state.publicKey = publicKey
    },
  },
  actions: {
    fetchPublicKey ({ commit }) {
      return ApiService.get('http://localhost:8081/api/betterpark-payment/Payment.fetch_public_key')
      .then(response => {
        commit('setPublicKey', response.data.public_key)
      })
    },
    chargeAmount (_, charge) {
      return ApiService.post('http://localhost:8081/api/betterpark-payment/Payment.create_customer_pay', charge)
    },
    fetchLicensePlate (_, plateNumber) {
      return ApiService.post('https://test.betterpark.de/api/payment/betterpark/v1.0/fetch', plateNumber, {
        auth: {
          username: 'payment',
          password: 'payment'
        }
      });
    }
  },
  getters: {
    getPublicKey(state) {
      return state.publicKey;
    },
  },
  modules: {
  }
});

