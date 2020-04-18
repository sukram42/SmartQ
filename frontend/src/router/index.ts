import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import ShopDetailPage from '../views/ShopDetailPage.vue'
import Counter from '../views/Counter.vue'
import Login from '../views/Login.vue'

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
    path: '/counter/:id',
    name: 'Counter',
    component: Counter
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
