<template>
  <v-app>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue';
import account from './components/account.vue';

export default {
  name: 'App',

  components: {
    HelloWorld,
    Home,
    account,

  },

  data: () => ({
    //
  }),
}
</script>
<style>
#app {
  font-family: Arial, sans-serif;
}
</style>