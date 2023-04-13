import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import { VueReCaptcha } from "vue-recaptcha-v3";
import router from './router'

loadFonts()

createApp(App)
  .use(VueReCaptcha, { siteKey: "6Lf-EIAlAAAAAN0-gJgvH3jfJnR2ti1Trb1UGxtp" })
  .use(router)
  .use(vuetify)
  .mount('#app')
