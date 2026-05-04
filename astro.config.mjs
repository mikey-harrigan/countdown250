import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://countdown250.allamericanball.com',
  base: '/',
  integrations: [
    sitemap({
      filter: (page) =>
        !/\/(homepage-|home-original-archive|hosted-group-tables-preview|tickets-preview)/.test(page),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
