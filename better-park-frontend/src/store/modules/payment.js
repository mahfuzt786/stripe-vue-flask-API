import Vue from 'vue'
// import ApiService from '../../services/api.service'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const state = {
  publicKey: '',
}

const mutations = {
  setPublicKey (state, publicKey) {
    Vue.set(state, 'publicKey', publicKey)
  },
}

const actions = {
  // fetchPublicKey ({ commit }) {
  //   return ApiService.get('/Payment.fetch_public_key').then(response => {
  //     commit('setPublicKey', response.data.public_key)
  //   })
  // },
  // chargeAmount ({ commit, getters }, charge) {
  //   return ApiService.post('/Payment.create_payment', charge)
  // },
  // fetchPayment ({ commit }) {
  //   return ApiService.get(`/Payment.get_payment_list`).then(response => {
  //     return response.data.data.payment_list;
  //   })
  // }

  fetchPublicKey ({ commit }) {
    return axios.get('http://localhost:8081/api/betterpark-payment/Payment.fetch_public_key')
    .then(response => {
      console.log(response);
      commit('setPublicKey', response.data.public_key)
    })

  },
  // chargeAmount ({ commit, getters }, charge) {
  //   return axios.post('http://localhost:8081/api/betterpark-payment/Payment.create_payment', charge)
  // },
  // fetchPayment ({ commit }) {
  //   return axios.get(`/Payment.get_payment_list`).then(response => {
  //     return response.data.data.payment_list;
  //   })
  // }
}

const getters = {
  getPublicKey: (state) => {
    return state.publicKey
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}



// export default new Vuex.Store({
//   state: {
//   },
//   mutations: {
//   },
//   actions: {
//     fetchPublicKey ({ commit }) {
//       return axios.get('http://localhost:8081/api/betterpark-payment/Payment.fetch_public_key')
//       // .then(response => {
//       //   console.log(response);
//       //   // commit('setPublicKey', response.data.public_key)
//       // })
  
//     },
//     calculateValuesApi(state, input) {
//       console.log(input)
//       console.log('values', JSON.stringify(input))
//       const formData = new FormData();
//       formData.append('data', JSON.stringify(input));
//       return axios.post('http://localhost/dental-api/', formData)
//       // return axios.post('https://www.alegralabs.com/syed/dental-api/', formData)

//     }
//   },
//   modules: {
//   }
// })
