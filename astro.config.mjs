import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://countdown250.allamericanball.com',
  base: '/',
  // Partner-channel short URLs. Each entry maps a clean, brandable
  // short path → the homepage with an Eventbrite `aff=` tracking
  // code appended. The BaseLayout.astro affiliate-pass-through
  // script picks up the `aff=` on landing, stores it in
  // sessionStorage, and rewrites every outbound Eventbrite link
  // on every page the visitor browses so the tracking code reaches
  // checkout. End result: countdown250.allamericanball.com/rpv
  // serves as a brand-safe short link RPV can paste anywhere, and
  // every ticket bought through that funnel shows up in Eventbrite
  // under the matching tracking link (e.g. `RPV`).
  //
  // To add a new partner: drop another row here AND create the
  // matching tracking link in Eventbrite so reports show it by name.
  redirects: {
    '/rpv': '/?aff=RPV',
  },
  integrations: [
    sitemap({
      filter: (page) =>
        !/\/(homepage-|home-original-archive|hosted-group-tables-preview|tickets-preview|liquid-blue-preview|entertainment-preview|partners-preview|american-icons-preview|statesmans-pass|freedom-bell-|space-blue-preview|icons-vote-preview|rpv)/.test(page),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
