<template>
  <v-container>
    <v-row class="text-center">

      <v-col class="mb-4" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to COMP 3334!
        </h1>
      </v-col>

      <v-col class="mb-4" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          <v-btn v-on:click="call1">Click me to test the Rest API</v-btn>
          <v-banner>
            <v-banner-text>
              {{ label }}
            </v-banner-text>
          </v-banner>
        </h1>
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          <v-btn v-on:click="call2">{{ label2  }}</v-btn>
        </h1>
      </v-col>


      <div class="text-center ma-2">
    <v-btn
      @click="snackbar = true"
    >
      Open Snackbar
    </v-btn>
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
</template>

<script>

export default {
  name: 'HelloWorld',

  data: () => ({
    label: 'Banner with one line of text.',
    label2: 'Lets test Json',
    snackbar: false,
    text: `Hello, I'm a snackbar`,


    ecosystem: [
      {
        text: 'vuetify-loader',
        href: 'https://github.com/vuetifyjs/vuetify-loader/tree/next',
      },
      {
        text: 'github',
        href: 'https://github.com/vuetifyjs/vuetify/tree/next',
      },
      {
        text: 'awesome-vuetify',
        href: 'https://github.com/vuetifyjs/awesome-vuetify',
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
    call2(){
      // fetch("/api/users")
      // .then((response) => response.text())
      // .then((data) => {
      //   alert(data)
      //   var mydata = JSON.parse(data);
      //   this.label = "Hi " + mydata[0].userName
      //   this.label2 = "Hi " + mydata[1].userName
      // });
      router.push({ path: 'home' })

    },
    
  },

}
</script>
