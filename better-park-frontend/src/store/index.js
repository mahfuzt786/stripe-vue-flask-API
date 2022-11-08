import axios from 'axios';
import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import ApiService from '../services/api.service'


Vue.use(Vuex)

export default new Vuex.Store({
// export default ({
  state: {
    publicKey: '',
    confirmPlateNumber: '',
    licensePlate: '',
    parkingFee: '',
    parkingFeeDiscount: '',
  },
  mutations: {
    setPublicKey (state, publicKey) {
      state.publicKey = publicKey
    },
    setConfirmlicensePlate (state, confirmPlateNumber) {
      state.confirmPlateNumber = confirmPlateNumber
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
      return ApiService.get(process.env.VUE_APP_API_CALL + 'Payment.fetch_public_key')
      .then(response => {
        commit('setPublicKey', response.data.public_key)
      })
    },
    chargeAmount (_, charge) {
      return ApiService.post(process.env.VUE_APP_API_CALL + 'Payment.create_customer_pay', charge)
    },
    createPaymentIntent (_, charge) {
      return ApiService.post(process.env.VUE_APP_API_CALL + 'Payment.create_payment_intent', charge)
    },
    confirmLicensePlate ({ commit }, confirmPlateNumber) {
        commit('setConfirmlicensePlate', confirmPlateNumber.licensePlate)
    },
    // fetchLicensePlate (_, plateNumber) {
    fetchLicensePlate ({ commit }, plateNumber) {
      // return ApiService.post('https://test.betterpark.de/api/payment/betterpark/v1.0/fetch', plateNumber, {
      //   auth: {
      //     username: 'payment',
      //     password: 'payment'
      //   }
      // });

      // console.log(plateNumber)
      const params = {
        licensePlate: { toJSON: () => plateNumber.licensePlate }
      };

      return axios.get(process.env.VUE_APP_API_CALL + 'Payment.fetch', { params } ).then(response => {
        commit('setlicensePlate', response.data.licensePlate)
        commit('setParkingFee', response.data.parkingProcesses[0].parkingFee)
      })
    },
    fetchDiscount ({ commit }) {
      return ApiService.get(process.env.VUE_APP_API_CALL + 'Payment.discount').then(response => {
        commit('setParkingFeeDiscount', response.data.parkingFee)
      })
    },
  },
  getters: {
    getPublicKey(state) {
      return state.publicKey;
    },
    getConfirmLicensePlate(state) {
      return state.confirmPlateNumber;
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

