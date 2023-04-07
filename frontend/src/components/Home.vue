<!-- <template>
  <v-container>

  </v-container>
</template> -->
<template>
  <div>
    <h1>Welcome to my chat website!</h1>
    <p>Here you can chat with your classmates in real-time.</p>
    <router-link to="/login">Login</router-link>
    <p></p>
    <router-link to="/register">Register</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>
