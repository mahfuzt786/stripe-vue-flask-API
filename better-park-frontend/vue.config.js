const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],

  publicPath: '/syed/park-stripe/better-park-frontend/dist/', //for server build
  // publicPath: '/', // for localhost

  devServer: {
    // public: 'localhost:8080',
    headers: {
      'Access-Control-Allow-Origin' : '*'
    }
  }
})
