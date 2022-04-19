import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-auto';
import path from 'path';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    kit: {
        adapter: adapter(),
        vite: {
            resolve: {
                alias: {
                    $components: path.resolve('./src/components/'),
                    $src: path.resolve('./src/'),
                    $types: path.resolve('./src/types/'),
                    $lib: path.resolve('./lib')
                }
            }

        }
    },

    preprocess: [
        preprocess({
            postcss: true
        })
    ]
};

export default config;