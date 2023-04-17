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

</script>
