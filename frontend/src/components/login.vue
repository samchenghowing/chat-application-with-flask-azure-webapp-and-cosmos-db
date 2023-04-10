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

              <v-btn type="submit" block class="mt-2" v-on:click="login">Login</v-btn>
            </v-form>
          </v-sheet>
        </v-col>

        <v-col class="mb-4" cols="12">
          <h1 class="display-2 font-weight-bold mb-3">
            <v-btn v-on:click="call1">Test backend connection</v-btn>
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
          <v-btn
            @click="snackbar = true"
          >
            Open Snackbar
          </v-btn>
        </v-col>


        <div class="text-center ma-2">
          <v-snackbar
            v-model="snackbar"
          >
            {{ text }}

            <template v-slot:actions>
              <v-btn
                color="pink"
                variant="text"
                @click="snackbar = false"
              >
                Close
              </v-btn>
            </template>
          </v-snackbar>
        </div>

      </v-row>
    </v-container>
  </div>
</template>

<script>

export default {

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
      fetch("/api/about")
      .then((response) => response.text())
      .then((data) => {
        this.label = data
      });
    },
    login(){
      // TO-DO: delay 1 second to slow down hacker
      if (this.userName.length > 3 && this.password.length > 8) {
        fetch("/api/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ 
            name: this.userName,
            password: this.userName,
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
