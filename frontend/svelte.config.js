import adapter from '@sveltejs/adapter-auto';
import preprocess from 'svelte-preprocess';
import path from 'path';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: [
        preprocess({
            postcss: true
        })
    ],

    kit: {
        adapter: adapter(),
        vite: {
            resolve: {
                alias: {
                    $components: path.resolve('./src/components/'),
                    $src: path.resolve('./src/'),
                    $types: path.resolve('./src/types/'),
                    $lib: path.resolve('./src/lib/'),
                }
            }

        }
    }
};

export default config;