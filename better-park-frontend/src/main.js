import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'
// import ApiService from './services/api.service'

import Notifications from 'vue-notification'
import VueCardFormat from 'vue-credit-card-validation';

Vue.config.productionTip = false

Vue.prototype.$environment = process.env
Vue.prototype.$store = store;

Vue.use(Notifications);
Vue.use(VueCardFormat);


new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
