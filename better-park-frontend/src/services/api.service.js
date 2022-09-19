import axios from 'axios'


const ApiService = {
  _401interceptor: null,

  init (baseUrl, router) {
    axios.defaults.baseURL = baseUrl
    axios.defaults.timeout = 500000
    axios.defaults.headers.common['Content-Type'] = 'application/json'
    axios.defaults.headers.common['Accept'] = 'application/json'
    this._router = router;
  },

  removeHeader () {
    delete axios.defaults.headers.common['Authorization']
  },

  get (resource) {
    return axios.get(resource)
  },

  post (resource, data) {
    return axios.post(resource, data)
  },

  custom (reqData) {
    return axios(reqData)
  },

}

export default ApiService
