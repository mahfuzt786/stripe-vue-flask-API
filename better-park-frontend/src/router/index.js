import Vue from 'vue'
import VueRouter from 'vue-router'

import home from '../components/Home.vue';
import page1 from '../components/page1.vue';
import page2 from '../components/page2.vue';
import page3 from '../components/page3.vue';
import page4 from '../components/page4.vue';
import page5 from '../components/page5.vue';
import page5_1 from '../components/page5_1.vue';
import page6 from '../components/page6.vue';
import PaymentStripe from '../components/PaymentStripe.vue';
import page7 from '../components/page7.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: home
  },
  {
    path: '/home',
    component: home
  },
  {
    path: '/page1',
    component: page1
  },
  {
    path:'/page2',
    component:page2
  },
  {
    path:'/page3',
    component:page3
  },
  {
    path:'/page4',
    component:page4
  },
  {
    path:'/page5',
    component:page5
  },
  {
    path:'/page5_1',
    component:page5_1
  },
  {
    path:'/page6',
    component:page6
  },
  {
    path:'/paymentstripe',
    component:PaymentStripe
  },
  {
    path:'/page7',
    component:page7
  },
];

const router = new VueRouter({
  routes,
  // mode: 'hash'
  // base: process.env.BASE_URL
})

export default router
