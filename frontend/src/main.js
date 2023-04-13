import { createApp } from 'vue'
import App from './App.vue'
import { VueReCaptcha } from 'vue-recaptcha-v3'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'

loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
  .use(VueReCaptcha, { siteKey: '6Lf-EIAlAAAAAN0-gJgvH3jfJnR2ti1Trb1UGxtp' })
  .mount('#app')
  
