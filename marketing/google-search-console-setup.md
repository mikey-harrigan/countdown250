# Google Search Console — Setup & Indexing Speed-up

## Why
Google Search Console (GSC) is where you tell Google "I made this site, please show it in search." It's also how you get early warnings if anything breaks SEO (broken pages, mobile issues, security problems) and how you speed up indexing new pages like the GASF landing page.

It's free. Takes ~10 minutes to set up. Adds 1–2 days of speed to new page indexing.

## Step-by-step (Mike does, ~10 min)

### 1. Open Google Search Console
- Go to `https://search.google.com/search-console/`
- Sign in with `CountdownAmerica250@gmail.com` (the event email) if possible — keeps analytics / marketing tools consolidated.

### 2. Add your property
- Click **Add property** (or the dropdown near top-left if you already have properties)
- Select **URL prefix** (not Domain — URL prefix is simpler for GitHub Pages)
- Enter: `https://countdown250.allamericanball.com`
- Click **Continue**

### 3. Verify ownership
Google will offer several verification methods. Use **HTML tag** (easiest for this site):

1. Copy the meta tag Google shows you (looks like `<meta name="google-site-verification" content="xxxxxxxx" />`)
2. **Paste that tag in this chat** — Claude will add it to `BaseLayout.astro` and push to the site
3. After Claude pushes (~2 min), click **Verify** in GSC

### 4. Submit your sitemap
After verification succeeds:

1. In GSC left sidebar, click **Sitemaps**
2. Under "Add a new sitemap", enter: `sitemap-index.xml`
3. Click **Submit**

Google will start crawling all pages listed in the sitemap, including the new GASF landing page.

### 5. Request indexing for the new page (speed hack)
1. In GSC, click the **URL inspection** bar at top
2. Paste: `https://countdown250.allamericanball.com/great-american-state-fair-evening`
3. Press Enter → Google loads the page data
4. Click **Request indexing**
5. Google prioritizes it in their crawl queue (usually gets indexed within 24–48 hours vs. 1–2 weeks for natural crawl)

### 6. (Optional but recommended) Link GSC to Google Analytics / Ads
In GSC → **Settings** → **Associations** → link to Google Ads account. This enables useful cross-reporting.

## What to check after setup

After 48 hours, return to GSC:
- **Performance** tab: see what keywords brought people to your site
- **Pages** tab: confirm GASF landing page is "Indexed"
- **Core Web Vitals**: site performance (should be green — Astro sites are fast)
- **Mobile usability**: should be zero errors (we designed mobile-first)

## What I'll do on my end when you paste the verification tag
1. Add it to `src/layouts/BaseLayout.astro` `<head>`
2. Commit & push (~30 sec)
3. Tell you it's live so you can hit Verify in GSC

## Other pages worth requesting indexing for (after verification)
In addition to `/great-american-state-fair-evening`:
- `/` (home)
- `/statesmans-pass`
- `/press`
- `/faq`
- `/schedule`
- `/honorees`

Batch-request them. Takes 1 min per page.
