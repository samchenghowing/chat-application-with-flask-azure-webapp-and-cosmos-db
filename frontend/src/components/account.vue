<template>
  <div>
    <h1>My Account</h1>
    <div class="account-info">
      <div class="profile-picture">
        <img :src="profilePicture" alt="Profile Picture" />
      </div>
      <div class="details">
        <h2>{{ userName }}</h2>
        <p>{{ email }}</p>
        <button @click="editProfile">Edit Profile</button>
      </div>
    </div>
    <div class="settings">
      <h2>Settings</h2>
      <ul>
        <!-- <li>
          <router-link to="/account/change-password"
            >Change Password</router-link
          >
        </li> -->
        <!-- <li>
          <router-link to="/account/privacy-settings"
            >Privacy Settings</router-link
          >
        </li> -->
        <li>
          <button @click="deleteAccount()">Delete Account</button>
        </li>
      </ul>
    </div>
    <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        width="1024"
      >
        <v-card>
          <v-card-title>
            <span class="text-h5">User Profile</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="userName"
                    label="Name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="email"
                    label="Email"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="oldpassword"
                    label="Old Password*"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="password"
                    label="New Password*"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog = false"
            >
              Cancel
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click.prevent="updateSetting()"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>
  
  <script>
import CryptoJS from 'crypto-js';

export default {
  name: "AccountPage",
  mounted(){
    var obj = JSON.parse(sessionStorage.user)
    this.userName = obj["User info"]["name"]
    this.email = obj["User info"]["email"]
  },
  data() {
    return {
      userName: '',
      email: '',
      oldpassword: '',
      password: '',
      dialog: false,
      profilePicture: "https://via.placeholder.com/150",
    };
  },
  methods: {
    deleteAccount() {
      if (confirm("Are you sure to delete your account?") == true) {
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]

        var loginAPI = process.env.VUE_APP_API_URL + "/account/deleteAccount"        
        fetch(loginAPI, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            userID: userID,
            name: name,
            pwHash: pwHash,
          })
        })
        .then((response) => response.json())
        .then((data) => {
          if(data.isvalid){
            this.$router.push('/login')
            alert("You account is deleted")
          }
        })
      } else { }
    },
    editProfile() {
      this.dialog = true
    },
    updateSetting() {
      this.dialog = false
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]

      var editAPI = process.env.VUE_APP_API_URL + "/account/updateProfile"   
        fetch(editAPI, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            userID: userID,
            name: name,
            oldpwHash: pwHash,
            newname: this.userName,
            newemail: this.email,
            newpwHash: CryptoJS.SHA256(this.password).toString(CryptoJS.enc.Base64),
          })
        })
        .then((response) => response.json())
        .then((data) => {
          alert(JSON.stringify(data))
        })
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
  