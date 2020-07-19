import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/start',
    name: 'starter',
    meta: {layout: 'empty'},
    component: () => import('@/views/Welcome.vue')
  },
  {
    path: '/sign-up',
    name: 'register',
    meta: {layout: 'entry'},
    component: () => import('@/views/Register.vue')
  },
  {
    path: '/login',
    name: 'login',
    meta: {layout: 'entry'},
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/forget',
    name: 'reset',
    meta: {layout: 'entry'},
    component: () => import('@/views/ForgetPassword.vue')
  },
  {
    path: '/',
    name: 'home',
    meta: {layout: 'empty', requiresAuth: true},
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/collections/:id',
    name: 'collection',
    meta: {layout: 'empty', requiresAuth: true},
    component:() => import('@/views/Collection.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    meta: {layout: 'empty', requiresAuth: true},
    component:() => import('@/views/Profile.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next()
      return
    }
    next('/start') 
  } else {
    next() 
  }
})


export default router
