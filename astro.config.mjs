import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://mikey-harrigan.github.io',
  base: '/countdown250',
  vite: {
    plugins: [tailwindcss()],
  },
});
