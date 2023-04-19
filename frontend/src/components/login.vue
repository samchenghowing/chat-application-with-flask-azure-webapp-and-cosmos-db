<template>  
  <div id="nav">
    <v-container>
      <v-row class="text-center">

        <v-col class="mb-4" cols="12">
          <h1 class="display-2 font-weight-bold mb-3">
            Login
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
                counter
              ></v-text-field>

              <v-btn 
                type="submit" 
                block class="mt-2" 
                :loading="loading"
                v-on:click="login"
                >Login
                <template v-slot:loader>
                  <v-progress-linear indeterminate></v-progress-linear>
                </template>
              </v-btn>
            </v-form>
          </v-sheet>
        </v-col>

        <div class="text-center ma-2">
          <v-snackbar
            v-model="snackbar"
          >
            {{ text }}
          </v-snackbar>
        </div>

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
    snackbar: false,
    loading: false,
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
  watch: {
    loading (val) {
      if (!val) return

      setTimeout(() => (this.loading = false), 2000)
    },
  },

  methods:{
    login(){
      if (this.userName.length > 2 && this.password.length > 7) {
        this.loading = true

        var loginAPI = process.env.VUE_APP_API_URL + "/login"        
        fetch(loginAPI, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            name: this.userName,
            pwHash: CryptoJS.SHA256(this.password).toString(CryptoJS.enc.Base64),
          })
        })
        .then((response) => response.json())
        .then((user) => {
          console.log(JSON.stringify(user))
          this.loading = false
          this.snackbar = true
          this.text = user.status

          // if is vaild user
          if (user.isvalid){
            sessionStorage.setItem('isAuth', 'true');
            sessionStorage.setItem('user', JSON.stringify(user));
            window.dispatchEvent(new CustomEvent('isAuth-changed', {
              detail: {
                isAuth: sessionStorage.getItem('isAuth')
              }
            }));
            this.$router.push('/chatPage')
          }
        })
      }
    },
    
  },

}
</script>
