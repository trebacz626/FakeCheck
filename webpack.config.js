const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  entry: ['./static/src/index.js', './static/src/index.scss'],
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "index.css"
    }),
    new VueLoaderPlugin()
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            'sass-loader'
        ]
      },
      {
        test: /\.vue$/,
        use: 'vue-loader'
      }
    ]
  },
  resolve: {
    alias: {
      vue: 'vue/dist/vue.js'
    }
  }
};