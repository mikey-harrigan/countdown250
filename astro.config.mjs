import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://countdown250.allamericanball.com',
  base: '/',
  vite: {
    plugins: [tailwindcss()],
  },
});
