import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import ShopDetailPage from '../views/ShopDetailPage.vue'
import Counter from '../views/Counter.vue'
import newShop from '../views/newShop.vue'
import Login from '../views/Login.vue'
import addUser from '../views/addUser.vue'
import QRCode from '../views/QRCode.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/shopDetail/:shopID',
    name: 'ShopDetail',
    component: ShopDetailPage
  },
  {
    path: '/counter/:shopID',
    name: 'Counter',
    component: Counter
  },
  {
    path: '/newShop',
    name: 'newShop',
    component: newShop
  },
  {
    path: '/qrCode/:shopID',
    name: 'qrCOde',
    component: QRCode
  },
  {
    path: '/addUser/:shopID/:userID',
    name: 'addUser',
    component: addUser
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/shop',
    name: 'Shop',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Shop.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
