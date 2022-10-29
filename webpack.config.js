const path = require('path');

module.exports = {
    name: "skills-project-config", // name of the configuration, shown in output
    entry: "./crosswalkgallery/javascript/index.js", // string | object | array
    // defaults to ./src
    // Here the application starts executing
    // and webpack starts bundling
    output: {
        // options related to how webpack emits results
        path: path.resolve(__dirname, './crosswalkgallery/static'),
        // string (default)
        // the target directory for all output files
        // must be an absolute path (use the Node.js path module)
        filename: 'index-bundle.js',
        // string (default)
        // the filename template for entry chunks
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
            },
            {
                test: /\.jpg$/,
                exclude: /(node_modules)/,
                loader: 'file-loader',
                options: {
                    // Currently browser is not able to load the 
                    // bundled images without this on false
                    esModule: false,
                }
            },
        ]
    }
};