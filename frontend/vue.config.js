// const FileManagerPlugin = require('filemanager-webpack-plugin-fixed');

module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    index: 'home.html',
    // proxy: "http://127.0.0.1:8000", // xhr only
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:8000',
      },
      '^/admin': {
        target: 'http://127.0.0.1:8000'
      }
    }
  },

  pages: {

    home: {
      template: 'public/index.html',
      entry: 'src/pages/main_home.js',
      filename: 'home.html',
      title: 'VueDjangoPhoto/home.html',
      minify: false,
    },

    post_list: {
      template: 'public/index.html',
      entry: 'src/pages/main_post_list.js',
      filename: 'post_list.html',
      title: 'VueDjangoPhoto/post_list.html',
      minify: false,
    },

    post_detail: {
      template: 'public/index.html',
      entry: 'src/pages/main_post_detail.js',
      filename: 'post_detail.html',
      title: 'VueDjangoPhoto/post_detail.html',
      minify: false,
    },
  },

  // configureWebpack: {
  //   plugins: [
  //     new FileManagerPlugin({
  //       onStart: {
  //         delete: [
  //           '../backend/static/**/',
  //           '../backend/templates/**/',
  //         ]
  //       },

  //       onEnd: {
  //         copy: [
  //           { source: 'dist/static', destination: '../backend/static/' },
  //           { source: 'dist/favicon.ico', destination: '../backend/static/img/' },
  //           { source: 'dist/home.html', destination: '../backend/templates/' },
  //           { source: 'dist/post*.html', destination: '../backend/templates/blog/' },
  //         ],
  //       }
  //     }),
  //   ]
  // }
  css: {
    extract: { ignoreOrder: true },
  },
}
