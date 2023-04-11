import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../components/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/account',
    name: 'account',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    meta: { requiresAuth: true }, // user must login before they can be route to this page
    component: () => import(/* webpackChunkName: "about" */ '../components/account.vue')
  }, {
    path: '/chatPage',
    name: 'chatPage',
    meta: { requiresAuth: true }, 
    component: () => import(/* webpackChunkName: "about" */ '../components/chatPage.vue')
  }, {
    path: '/login',
    name: 'loginPage',
    component: () => import(/* webpackChunkName: "about" */ '../components/login.vue')
  }, {
    path: '/signup',
    name: 'signupPage',
    component: () => import(/* webpackChunkName: "about" */ '../components/signup.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (sessionStorage.getItem('isAuth') === 'true') {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router
