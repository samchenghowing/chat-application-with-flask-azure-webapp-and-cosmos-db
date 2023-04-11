<!-- import { createRouter, createWebHashHistory } from 'vue-router' -->

<!-- <template>
  <v-container>

  </v-container>
</template> -->
<template>
  <div>
    <h2 class="display-2 font-weight-bold mb-3">COMP3334</h2>
    <h1>Welcome to my chat website!</h1>
    <p>Here you can chat with your classmates in real-time.</p>
    <router-link to="/login">Log In</router-link>
    <p></p>
    <router-link to="/signup">Sign Up</router-link>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
// const routes = [
//   {
//     path: '/signIn',
//     name: 'Sign In',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ './signIn.vue')
//   },
// ];

// const router = createRouter({
//   history: createWebHashHistory(process.env.BASE_URL),
//   routes
// })

</script>
