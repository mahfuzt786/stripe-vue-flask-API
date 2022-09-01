import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import home from './components/Home.vue';
import page1 from './components/page1.vue';
import page2 from './components/page2.vue';
import page3 from './components/page3.vue';
import page4 from './components/page4.vue';
import page5 from './components/page5.vue';
import page5_1 from './components/page5_1.vue';
import page6 from './components/page6.vue';
import page7 from './components/page7.vue';
import hello from './components/HelloWorld.vue';

Vue.use(VueRouter);

const routes = [
  {path:'/',component:home},
  {path:'/page1',component:page1},
  {path:'/page2',component:page2},
  {path:'/page3',component:page3},
  {path:'/page4',component:page4},
  {path:'/page5',component:page5},
  {path:'/page5_1',component:page5_1},
  {path:'/page6',component:page6},
  {path:'/page7',component:page7},
  {path:'/hello',component:hello},
];
const router = new VueRouter({
  routes
})

Vue.config.productionTip = false

new Vue({
  vuetify,
  router:router,
  render: h => h(App)
}).$mount('#app')
