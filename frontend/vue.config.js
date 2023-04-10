const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,

    pluginOptions: {
      vuetify: {}
    }
})
module.exports = {
    // https://cli.vuejs.org/config/#devserver-proxy
    devServer: {
        port: 3000,
        proxy: {
            '/api': {
                target: 'https://localhost:8080',
                ws: true,
                changeOrigin: true
            }
        }
    },

    pluginOptions: {
      vuetify: {}
    }
}
