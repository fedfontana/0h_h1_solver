import adapter from '@sveltejs/adapter-static';
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
        /* prerender: {
            default: true,
        }, */
        adapter: adapter({
            fallback: 'index.html',
        }),
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