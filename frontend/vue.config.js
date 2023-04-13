const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,

    pluginOptions: {
      vuetify: {}
    }
})
module.exports = {
    publicPath: process.env.NODE_ENV === "production" ? "/COMP3334/" : "/",

    pluginOptions: {
      vuetify: {}
    }
}
