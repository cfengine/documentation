const TerserPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

const jsFiles = [
    'google_analytics_search.js',
    'jquery-1.9.1.min.js',
    'jquery-migrate-1.2.1.min.js',
    'jquery.sidr.min.js',
    'custom.js',
    'dropdown.js',
];

module.exports = {
    entry: {
        main: jsFiles.map(file => `${__dirname}/_assets/js/${file}`)
    },
    output: {
        filename: 'bundle.min.js',
        path: __dirname + '/_site/assets',
    },
    optimization: {
        minimize: true,
        minimizer: [new TerserPlugin(), new CssMinimizerPlugin()],
    },
    module: {
        rules: [
            {
                test: /\.less$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "less-loader",
                ],
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.min.css'
        }),
    ],
};
