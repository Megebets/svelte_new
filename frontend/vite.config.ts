import { defineConfig } from 'vite';
import { sveltekit } from '@sveltejs/kit/vite';
import path from 'path';

export default defineConfig({
  plugins: [sveltekit()],
  kit: {
    alias: {
      $components: path.resolve('src/components'), // изменено на правильный путь
    }
  }
});
