const config = {
    content: ['./src/**/*.{html,js,svelte,ts}'],

    theme: {
        extend: {}
    },

    plugins: [],

    safelist: [{
            pattern: /gap-(x|y)-(5|4|2|1)/
        },
        {
            pattern: /rounded-(xl|2xl|3xl)/
        },
        {
            pattern: /bg-(red|blue|green)-(200|500)/
        }
    ]
};

module.exports = config;