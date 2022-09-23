import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import ApiService from '../services/api.service'


Vue.use(Vuex)

export default new Vuex.Store({
// export default ({
  state: {
    publicKey: '',
    licensePlate: '',
    parkingFee: '',
    parkingFeeDiscount: '',
  },
  mutations: {
    setPublicKey (state, publicKey) {
      state.publicKey = publicKey
    },
    setlicensePlate (state, licensePlate) {
      state.licensePlate = licensePlate
    },
    setParkingFee (state, parkingFee) {
      state.parkingFee = parkingFee
    },
    setParkingFeeDiscount (state, parkingFeeDiscount) {
      state.parkingFeeDiscount = parkingFeeDiscount
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
    // fetchLicensePlate (_, plateNumber) {
    fetchLicensePlate ({ commit }, plateNumber) {
      // return ApiService.post('https://test.betterpark.de/api/payment/betterpark/v1.0/fetch', plateNumber, {
      //   auth: {
      //     username: 'payment',
      //     password: 'payment'
      //   }
      // });

      return ApiService.get('http://localhost:8081/api/betterpark-payment/Payment.fetch', plateNumber).then(response => {
        commit('setlicensePlate', response.data.licensePlate)
        commit('setParkingFee', response.data.parkingProcesses[0].parkingFee)
      })
    },
    fetchDiscount ({ commit }) {
      return ApiService.get('http://localhost:8081/api/betterpark-payment/Payment.discount').then(response => {
        commit('setParkingFeeDiscount', response.data.parkingFee)
      })
    },
  },
  getters: {
    getPublicKey(state) {
      return state.publicKey;
    },
    getlicensePlate(state) {
      return state.licensePlate;
    },
    getParkingFee(state) {
      return state.parkingFee;
    },
    getParkingFeeDiscount(state) {
      return state.parkingFeeDiscount;
    }
  },
  modules: {
  }
});

