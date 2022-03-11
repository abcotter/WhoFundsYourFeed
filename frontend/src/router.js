import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from './components/Main.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Main
  },
  {
    path: '/:userid',
    component: Main
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
