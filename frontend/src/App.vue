<!-- import { createRouter, createWebHistory } from 'vue-router' -->

<template>
  <div id="nav">
    <Header />
    <router-link to="/">Home</router-link> |
    <router-link to="/account">Account</router-link>
    <p></p>
    <router-link to="/chatPage">Chat</router-link>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/header.vue'
export default {
  name: "HomePage",
  components:{
    Header
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
