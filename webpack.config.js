const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const mode = process.env.NODE_ENV || 'development';

module.exports = {
  entry: './src/index.tsx', // main entry file
  mode,
  devtool: mode === 'development' ? 'inline-source-map' : false,
  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),
    clean: true, // clear dist before build
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // auto inject bundle
    }),
  ],
  devServer: {
    static: path.join(__dirname, 'dist'),
    port: 3000,
    hot: true,
    open: true,
    compress: true,
  },
  optimization: {
    splitChunks: {
      chunks: 'all', // better caching
    },
  },
};
