<template>
  <div>
    <h1>My Account</h1>
    <div class="account-info">
      <div class="profile-picture">
        <img :src="profilePicture" alt="Profile Picture" />
      </div>
      <div class="details">
        <h2>{{ fullName }}</h2>
        <p>{{ email }}</p>
        <button @click="editProfile">Edit Profile</button>
      </div>
    </div>
    <div class="settings">
      <h2>Settings</h2>
      <ul>
        <li>
          <router-link to="/account/change-password"
            >Change Password</router-link
          >
        </li>
        <li>
          <router-link to="/account/privacy-settings"
            >Privacy Settings</router-link
          >
        </li>
        <li>
          <router-link to="/account/delete-account">Delete Account</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "AccountPage",
  data() {
    return {
      fullName: "xxx",
      email: "abcd@1234567890.com",
      profilePicture: "https://via.placeholder.com/150",
    };
  },
  methods: {
    editProfile() {
      this.$router.push("/account/edit-profile");
    },
  },
};
</script>
  
  <style>
.account-info {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.profile-picture {
  margin-right: 1rem;
}

.profile-picture img {
  border-radius: 50%;
}

.details h2 {
  margin: 0;
  font-size: 2rem;
}

.details p {
  margin: 0;
  font-size: 1.2rem;
}

.settings h2 {
  margin-top: 2rem;
  font-size: 1.5rem;
}

.settings ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.settings li {
  margin-bottom: 0.5rem;
}

.settings a {
  text-decoration: none;
  color: #333;
}
</style>
  