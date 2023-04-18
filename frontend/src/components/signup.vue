<template>  
  <div id="nav">
    <v-container>
      <v-row class="text-center">

        <v-col class="mb-4" cols="12">
          <h1 class="display-2 font-weight-bold mb-3">
            Signup
          </h1>
          <v-sheet width="300" class="mx-auto">
            <v-form fast-fail @submit.prevent>
              <v-text-field
                v-model="userName"
                label="User Name"
                :rules="nameRules"
              ></v-text-field>

              <v-text-field
                v-model="password"
                :rules="passwordRules"
                :type="'password'"
                label="Password"
                hint="At least 8 characters"
              ></v-text-field>

              <v-text-field
                v-model="confirmPassword"
                :rules="passwordRules"
                :type="'password'"
                label="confirm Password"
                hint="At least 8 characters"
              ></v-text-field>
              <vue-recaptcha
                  ref="recaptcha"
                  @verify="onCaptchaVerified"
                  @expired="onCaptchaExpired"
                  size="invisible"
                  sitekey="6LfJA0gUAAAAAA4YDXBubWMll55x5xLpyzu6n60G">
                </vue-recaptcha>

              <v-btn type="submit" block class="mt-2" v-on:click="signup">signup</v-btn>
            </v-form>
          </v-sheet>

          <div class="text-center ma-2">
            <v-snackbar
              v-model="snackbar"
            >
              {{ text }}
            </v-snackbar>
          </div>
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>

import CryptoJS from 'crypto-js';

export default {
  // https://stackoverflow.com/questions/66597118/undefined-cryptojs-in-vue
  data: () => ({
    snackbar: false,
    text: `Hello, I'm a snackbar`,
    userName: '',
    password: '',
    nameRules: [
      value => {
        if (value?.length > 2) return true
        return 'User name must be at least 3 characters.'
      },
    ],
    passwordRules: [
      value => {
        if (value?.length < 8) return 'Min 8 characters'
        return true
      },
    ],

  }),

  methods:{
    signup(){
      if (this.userName.length > 2 && this.password.length > 7) {

        var signupAPI = process.env.VUE_APP_API_URL + "/signup"   
        fetch(signupAPI, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            name: this.userName,
            pwHash: CryptoJS.SHA256(this.password).toString(CryptoJS.enc.Base64),
          })
        })
        .then((response) => response.json())
        .then((data) => {
          this.snackbar = true
          this.text = data.status
          if(data.signup){
            this.$router.push('/login')
            alert("Signup success")
          }
        })
      }
    },
    
  },

}
</script>
