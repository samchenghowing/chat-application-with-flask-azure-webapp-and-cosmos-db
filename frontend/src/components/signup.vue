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

              <v-btn type="submit" block class="mt-2" v-on:click="login">Login</v-btn>
            </v-form>
          </v-sheet>
        </v-col>

        <v-col class="mb-4" cols="12">
          <h1 class="display-2 font-weight-bold mb-3">
            <v-btn v-on:click="recaptcha">Test backend connection</v-btn>
            <v-banner>
              <v-banner-text>
                {{ label }}
              </v-banner-text>
            </v-banner>
          </h1>
        </v-col>

        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            <v-btn v-on:click="$router.push('/')">Back to home</v-btn>
          </h1>
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>

import CryptoJS from 'crypto-js';

export default {
  // https://stackoverflow.com/questions/66597118/undefined-cryptojs-in-vue
  created() {
  //   var bytes  = CryptoJS.AES.decrypt(ciphertext, 'secret key 123');
  //   var originalText = bytes.toString(CryptoJS.enc.Utf8);
  },
  data: () => ({
    label: 'Banner with one line of text.',
    label2: 'back to main page',
    snackbar: false,
    text: `Hello, I'm a snackbar`,
    userName: '',
    password: '',
    nameRules: [
      value => {
        if (value?.length > 3) return true
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
    call1(){
      var aboutAPI = process.env.VUE_APP_API_URL + "/about"   
      fetch(aboutAPI)
      .then((response) => response.text())
      .then((data) => {
        this.label = data
      });
    },
    recaptcha() {
      this.$recaptcha('login').then((token) => {
        console.log(token) // Will print the token
      })
    },
    login(){
      // TO-DO: delay 1 second to slow down hacker

      if (this.userName.length > 3 && this.password.length > 7) {
        this.$recaptcha('login').then((token) => {
          console.log(token) // Will print the token
        })

        // TO-DO: add salt
        var hash = CryptoJS.SHA256(this.password)
        
        var signupAPI = process.env.VUE_APP_API_URL + "/signup"   
        fetch(signupAPI, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            name: this.userName,
            password: this.password,
          })
        })
        .then((response) => response.text())
        .then((data) => {
          this.label = data
        })
      }
    },
    
  },

}
</script>
