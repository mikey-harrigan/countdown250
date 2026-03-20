# Countdown250 Ball - Project Guide

## About This Project

This is the official website for the **All-American Countdown 250 Ball**, a once-in-a-generation patriotic celebration on **Friday, July 3, 2026** at the **Washington Hilton, Washington, D.C.** The event launches the historic July 4th, 2026 weekend marking the 250th anniversary of the United States.

### The Organization
- **Producer**: Merrifield Venture Partners, LLC d/b/a GoCity Group
- **Contact**: Mike Harrigan (Mike@headstrong1.com)
- **Facebook**: facebook.com/AllAmericanBall2025/
- **Prior Event**: All American Inaugural Ball (allamericanball.com) - 8 quadrennial editions over 30+ years

### Event Details
- **Event**: All-American Countdown 250 Ball
- **Date**: Friday, July 3, 2026
- **Time**: 7:00 PM - 1:00 AM (Liberty ticket entry at 9 PM)
- **Venue**: Washington Hilton, 1919 Connecticut Avenue NW, Washington, D.C. 20009
- **Capacity**: ~3,000 guests
- **Format**: 6 party zones, 4 stages, midnight countdown celebration
- **Dress Code**: Black tie / formal
- **Eventbrite**: https://www.eventbrite.com/e/all-american-countdown-250-ball-tickets-1982528927390
- **Refund Policy**: No refunds

### Event Pitch
Fifty years ago, Washington D.C. hosted the Bicentennial celebration. Now, on July 3, 2026, America celebrates 250 years. The Countdown 250 Ball fuses a New Year's Eve-style midnight countdown with the elegance of a presidential gala, the patriotic spirit of the Fourth of July, tributes to All-American heroes, and star-studded entertainment across a massive ballroom complex.

### Ticket Tiers (prices increase in future tiers)
1. **Liberty Ticket** (9 PM-1 AM) - $195 (early) up to $495. Full ball access, open bar, bands/DJs, attractions, reception-style.
2. **Patriot VIP Ticket** (7 PM-1 AM) - $395 (early) up to $995. VIP reception 7-9PM with buffet dinner + full ball.
3. **Statesman Concierge Pass** (7 PM-1 AM) - $1,495 (early) up to $5,000. Dedicated concierge, reserved Presidential Stage seating, private bars, premium buffet, backstage access, private photographer, commemorative gifts, program recognition. (Most Popular)
4. **Founders Host Package** - $12,500. 3 Statesman passes + half-page program tribute + multiple stage announcements.
5. **Presidential Host Package** - $18,500. 4 Statesman passes + full-page program tribute + multiple stage announcements.

### Venue: The Washington Hilton
Historic venue that has hosted presidents, world leaders, the White House Correspondents' Dinner, and countless national events. Site of the 1981 assassination attempt on President Reagan.

### What's Included (All Tiers)
- Vast patriotic ballroom complex
- Immersive attractions and roaming entertainers
- 6 party zones, 4 stages and dance floors
- Midnight countdown celebration
- Star-studded entertainment lineup
- Culinary stations and premium open bars
- All-American Hero Lifetime Achievement Awards
- Patriotic performances by veterans and first responders
- Live webcast

### Distinguished Guest Categories
Elected officials, business/civic leaders, media personalities, influencers, celebrities, professional athletes, decorated veterans, first responders, community leaders.

### Past Event Reference (All American Inaugural Ball 2025)
The most recent ball was Jan 18, 2025 at Hyatt Regency Capitol Hill. Featured Sean Spicer as MC, Lee Greenwood honored, Buzz Aldrin received Lifetime Achievement Award. 2,000 guests, 6 party zones, 3 dance floors. Had Gold ($250-$500), Platinum VIP ($550-$850), and Presidential Pass tiers. Entertainment included Thunderball, The Sicilian Tenors, Doug Segree, JJ Rupp, Matt Oakley, Julian Awari, Mark Fletcher, Dan Schoener (mentalist), DJ Freedom.

---

## Tech Stack

- **Framework**: Astro (static site generator - ships zero JS by default, great for SEO)
- **Styling**: Tailwind CSS v4 via `@tailwindcss/vite` plugin
  - **NOT** `@astrojs/tailwind` (that requires Tailwind v3)
  - Theme colors/fonts defined in `src/styles/global.css` using `@theme` directive (no `tailwind.config.mjs`)
- **Deployment**: Two environments (see Deployment section below)
  - **Preview**: GitHub Pages (auto-deploys on push to `main`)
  - **Production**: Static files uploaded to gate.com (Hostway) hosting (TODO: set up)
- **Domain**: Managed through gate.com (Hostway)
- **Base path**: `base: '/countdown250'` in `astro.config.mjs` for subfolder deployment
- **GitHub repo**: https://github.com/mikey-harrigan/countdown250
- **No database, no auth** - just a static site linking to Eventbrite for tickets

### Node.js / npm on Windows (MINGW64)

Node isn't always on the PATH in Git Bash. If `npm` or `npx` commands fail with "not recognized", prefix them:
```
PATH="/c/Program Files/nodejs:$PATH" npm run dev
```

## URL / SEO Strategy

### Domain Architecture
- **Primary domain**: `allamericanball.com` should be the long-term brand hub
- **Event URLs**: Use subfolders (e.g., `allamericanball.com/countdown250/`) NOT subdomains
  - Subfolders share domain authority; subdomains are treated as separate sites by Google
- **After events end**: Keep old event pages live as archives, with links to the current/next event
- **Current situation**: countdown250.allamericanball.com is a subdomain (suboptimal). New site should deploy to `allamericanball.com/countdown250/` when possible
- **Standalone domain**: countdown250ball.com can redirect to the subfolder for branding

### SEO Requirements
- Proper meta tags (title, description, Open Graph, Twitter Cards) on every page
- Structured data (JSON-LD) for Event schema
- Semantic HTML (proper heading hierarchy, landmark roles)
- Fast page loads (Lighthouse 95+)
- Mobile-first responsive design
- Sitemap.xml and robots.txt
- Canonical URLs
- Image alt text on every image
- Internal linking between pages

### Important Notice (Required on Site)
"This event is an independently produced celebration honoring America's 250th anniversary and is not affiliated with or endorsed by the U.S. Semiquincentennial Commission or the America250 Foundation."

---

## Writing Style & Tone

### DO
- Write with confident, patriotic energy
- Keep copy tight and punchy - shorter is better
- Use active voice
- Let the event speak for itself - it's genuinely impressive
- Be direct: "3,000 guests. 6 party zones. 4 stages."
- Sound professional and upscale - this is a $195-$18,500 ticket event

### DO NOT
- Use em dashes excessively (or at all if possible)
- Use the "It's not X; it's Y" construction
- Use bad millennial humor or try-hard quips
- Use AI-sounding language ("elevate", "harness", "leverage", "delve", "tapestry")
- Be overly wordy - if a section runs long, trim it
- Oversell with superlatives when the facts are compelling on their own

### COPYWRITING GUIDELINE FOR NON-TECHNICAL USERS
The user (Mike) tends to write long, verbose copy. When he provides text:
1. Gently suggest more concise alternatives
2. Show a trimmed version alongside the original
3. Explain why shorter copy often converts better (people skim, especially on mobile)
4. But ultimately respect his wishes if he prefers the longer version
5. Frame it as "here's a tighter option" not "your version is too long"

---

## Photo Library

Photos are stored in `public/images/` with this structure:
- `event-photos/` - Photos from past AAB events (2013, 2017, 2025)
- `logos/` - Brand logos (Countdown250, AAB, partner logos)
- `performers/` - Headshots/photos of performers and entertainers
- `honorees/` - Photos of past award honorees
- `venue/` - Venue photos
- `misc/` - Ribbons, buttons, decorative elements

A detailed photo catalog with labels is in `public/images/photo-catalog.json`.

---

## Deployment / Pushing Changes to Production

### IMPORTANT: After making ANY code changes, Claude MUST:
1. Commit and push to GitHub (this updates the preview site automatically)
2. Ask the user: "Want me to push these changes live to the production site?"
3. If yes, run the deploy-to-prod script (see below)

The users of this project are non-technical. They do not know git. Claude should handle ALL git operations automatically (staging, committing with a clear message, pushing) after making changes. Never ask the user to run git commands manually.

### Two Deployment Environments

#### 1. Preview Site (GitHub Pages) - ACTIVE
- **URL**: https://mikey-harrigan.github.io/countdown250/
- **How it works**: Automatically rebuilds when code is pushed to the `main` branch
- **Use for**: Sharing with team for feedback before going live

#### 2. Production Site (gate.com / Hostway) - TODO: SET UP
- **URL**: https://allamericanball.com/countdown250/
- **How it works**: Static files uploaded via FTP to the Hostway server
- **Status**: Not yet configured. Needs FTP credentials from gate.com hosting panel.

### Deploy to Production Script

When Hostway/gate.com FTP access is set up, create a `deploy.sh` script in the project root:

```bash
#!/bin/bash
# Deploy to production (allamericanball.com/countdown250/)
# Requires: FTP_HOST, FTP_USER, FTP_PASS environment variables
# These should be stored in a .env file (never committed to git)

set -e

echo "Building site..."
PATH="/c/Program Files/nodejs:$PATH" npm run build

echo "Uploading to production..."
# TODO: Replace with actual FTP details once gate.com credentials are obtained
# Option A: lftp (if available)
# lftp -e "mirror -R --delete dist/ /countdown250/ ; quit" -u $FTP_USER,$FTP_PASS $FTP_HOST
#
# Option B: If gate.com supports rsync/SSH
# rsync -avz --delete dist/ $FTP_USER@$FTP_HOST:/path/to/countdown250/
#
# Option C: If only browser-based file manager is available,
# Claude should instruct the user to upload the dist/ folder contents manually.

echo "Production deploy complete!"
echo "Live at: https://allamericanball.com/countdown250/"
```

### To set up production deployment:
1. Log into gate.com hosting panel for allamericanball.com
2. Find FTP credentials (host, username, password)
3. Create a `.env` file in the project root with those credentials
4. Update `deploy.sh` with the correct FTP command
5. Update `astro.config.mjs` site URL back to `https://allamericanball.com` for production builds

### Git Workflow (for Claude, not for humans)
- Always `git pull origin main` before starting work to avoid conflicts
- Stage specific changed files (not `git add -A` to avoid secrets)
- Write clear commit messages describing what changed
- Push to `origin main` after every commit
- If merge conflicts occur, resolve them (never force push)

---

## Project Structure

```
countdown250/
  public/
    images/              # All photos organized by category
      photo-catalog.json # AI-labeled metadata for all 54 event photos
    favicon.svg
    robots.txt
  src/
    components/          # UI sections (Hero, Navbar, Countdown, About, etc.)
    layouts/             # BaseLayout with SEO meta, JSON-LD, OG tags
    pages/               # Each .astro file = a route (index.astro)
    styles/
      global.css         # Tailwind v4 @theme config (colors, fonts)
  astro.config.mjs       # Site URL, base path, Tailwind vite plugin
  package.json
  tsconfig.json
  .gitignore
  CLAUDE.md              # This file
```

---

## Design Guidelines

- **Color palette**: Navy (#0a3161), Red (#b31942), Gold (#c9a84c), Cream (#faf8f5), White
- **Typography**: Clean, elegant serif for headings (Playfair Display), clean sans-serif for body (Inter)
- **Aesthetic**: Upscale, patriotic, clean. Think presidential gala invitation, not county fair flyer.
- **Mobile-first**: Design for phones first, then scale up
- **Photography**: Use real event photos from the photo library to build credibility
- **CTAs**: Primary action is always "Buy Tickets" linking to Eventbrite

---

## Current Site Status

The site is fully built as a single-page layout. All sections are validated for desktop (1280px) and mobile (375px).

### Page Sections (in order)
1. **Navbar** - Fixed, transparent-to-solid on scroll. Hamburger menu on mobile.
2. **Hero** - Full-viewport with ballroom photo background, navy gradient overlay. Title, stats, CTAs.
3. **Countdown** - Live countdown timer to July 3, 2026 7PM ET. Updates every second.
4. **About** - Two-column (text + photo). "Why July 3rd Matters" subsection.
5. **Experience** - 8 feature cards with gold icons on navy background. Photo strip.
6. **Venue** - Washington Hilton history highlights with gold bullet points.
7. **Guests** - Guest categories in cream pills. Photo collage.
8. **Gallery** - Masonry photo grid from past events.
9. **Tickets** - 3 ticket tier cards + 2 host packages. All link to Eventbrite.
10. **Footer** - Red CTA banner, quick links, social, legal disclaimer.

### What's Not Yet Done
- Production deployment to allamericanball.com/countdown250/ (needs gate.com FTP credentials)
- Domain DNS not pointed yet
- countdown250ball.com redirect to allamericanball.com/countdown250/
