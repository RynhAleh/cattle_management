const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    webSocketServer: false,
    proxy: {
      '/api': {
        target: 'http://0.0.0.0:8000',
        changeOrigin: true,
      },
    },
  },
};
