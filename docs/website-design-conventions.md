# Website Design Conventions — Countdown 250 Ball

**Last updated:** 2026-04-29
**Purpose:** Recovery / handoff doc for design language decisions made on the homepage and Hosted Tables page.

---

## Color terminology (Mike's vocabulary, locked)

When Mike uses these phrases in chat, they map to specific Tailwind classes:

| Mike says | Means | Hex | Tailwind class |
|---|---|---|---|
| **navy blue** *(primary)* | Old Glory Blue / America 250 official | `#002868` | `bg-navy`, `text-navy` |
| **navy-dark blue** | Darkest navy, used for high-impact moments | `#001a45` | `bg-navy-dark` |
| **navy light blue** | Hover states, accent only | `#0d3d7a` | `bg-navy-light` |
| **"white"** *(quotes)* | Cream — Mike's word for the existing light bg | `#faf8f5` | `bg-cream` |
| **gold** | Brand accent gold | (see global.css) | `bg-gold`, `text-gold` |
| **red** | Accent red — patriotic + scarcity | (see global.css) | `bg-red`, `text-red` |

### The primary brand blue: `navy blue` (`#002868`)
- This is **Old Glory Blue / Pantone 282 C** — the official US flag color and the America 250 Commission's brand color
- Use as the dominant section bg
- White or cream text on it; gold for emphasis

### When user says "change the bg color, also change text colors so they're appropriate"
This is a standing rule — every bg-color change should cascade through to text/border/divider/CTA color updates so contrast and readability stay clean. Don't ask, just do it. If you change to a dark bg, dark text becomes light. If gold-feature is appropriate (e.g., Statesman amenities), use gold for headlines and bold spans.

---

## Section bgs (current state, 2026-04-29)

| Section | Bg | Notes |
|---|---|---|
| Hero | (Hero component) | Photographic hero |
| About / value | navy (or cream depending on layout) | |
| Heroes / "Celebrating American Heroes" | **navy** | Was cream; user changed to navy — gold + white text on navy |
| Experience / "Your All-Inclusive Experience" | **cream** | Was a champagne gradient; user changed to cream. Has new "Be A Part Of History" red eyebrow above the H2. |
| Tickets / "Three Ticket Options" | **navy** | Was navy-dark; standardized to navy primary |
| Hosted Tables / "Host a Party Inside the Party" | **navy** | Was white; gold-feature treatment because it's a Statesman amenity |
| Sponsorship contact bar | navy-dark | Thin separator between Hosted Tables and Quotes |
| Social Proof / quotes | navy | |
| Footer CTA banner | navy | Now opens with 5 gold stars + "Be A Part Of History" |

---

## Recurring patterns

### Section heading rhythm
```
[Eyebrow]                    text-red font-bold tracking-[0.3em] uppercase text-xs sm:text-sm mb-3
[H2]                         text-3xl sm:text-4xl md:text-5xl font-bold text-{navy or white} mb-4 font-heading leading-tight
[Gold divider]               w-20 h-px bg-gold mx-auto mb-6
[Body]                       text-{navy/85 or white/85} text-lg leading-relaxed
```

### "Eyebrow" style
Used above section H2s and inside benefit panels. Always:
`text-{accent-color} font-bold tracking-[0.25em] uppercase text-xs sm:text-sm`

Examples on the live site: "A Distinguished Tradition", "Benefits to Hosts", "Be A Part Of History", "PLUS THESE ELITE UPGRADES:".

### Gold CTA button (signature pattern)
```
class="bg-gradient-to-b from-gold to-[#B8954A] hover:from-[#D9B864] hover:to-gold text-navy-dark px-9 py-4 text-sm font-bold tracking-[0.12em] uppercase rounded shadow-xl hover:shadow-2xl hover:-translate-y-0.5 ring-1 ring-gold/30 ring-offset-2 ring-offset-navy"
```
Used for: Statesman ticket "Host your Own Party Inside the Party" CTA, Hosted Tables page Create/Join cards, Hosted Tables "Explore Hosted Tables" button, page closing CTA.

### Eventbrite CTAs
All ticket-purchase CTAs use:
- `class="eventbrite-checkout"` — required for the Eventbrite checkout integration
- `href={ticketUrl}` — the `?aff=websitemain` affiliate URL

**Never strip the `eventbrite-checkout` class or the `aff=websitemain` query param.**

---

## Typography

- **Headings:** `font-heading` (loaded in BaseLayout)
- **Body:** Tailwind default sans-serif
- **Italic mood lines** (e.g., "These Honored Guests will receive our inaugural"): `font-heading italic` for serif-italic feel

---

## Spacing rhythm

- **Section padding:** `py-12 pb-20 sm:pt-16 sm:pb-28` (typical)
- **Tight section pairs** (e.g., two same-color sections): reduce to `pb-8 sm:pb-12` + `pt-8 sm:pt-10` — combined ~64–88px gap, not 128–176px
- **Below H2:** `mb-4` between H2 and divider
- **Below divider:** `mb-6` between divider and body
- **Between sections of body content:** `mb-10 sm:mb-12`

---

## Image conventions

- **Photos in carousels / cards:** `<img>` with `loading="lazy"` (first slide may be `loading="eager"`)
- **PNG with transparency** (medal, logos): use `<picture>` with `<source srcset="...webp" type="image/webp">` + `<img src="...png">` fallback
- **All images compressed** to display-size + Pillow optimization. Max widths typical:
  - Hero photos: 1600px
  - Carousel slides: 1600px
  - Logo / medal: 800–1000px
- **Compression scripts** in `scripts/` (compress_homepage_fat.py, png_to_webp.py, compress_experience.py, compress_heroes.py, swap_medal.py)

---

## Carousel pattern

- Class on container: `.heroes-carousel` or `.experience-carousel`
- Each slide: `<div class="carousel-slide">` (first one gets `active`)
- Dots match: each `<button class="carousel-dot">` (first one `active`)
- **Dot count must equal slide count** — Check #5 in the audit catches this
- Init: `initFadeCarousel('.heroes-carousel', 6500)` (6500ms per slide for heroes, 5500ms for experience)

---

## Footer

- "Be A Part Of History" replaces "Be There When History Is Made" (changed 2026-04-29)
- Opens with a row of 5 gold stars (★ ★ ★ ★ ★) — visual separator from the same-color navy testimonial section above

---

## Removed sections (don't bring back unless explicitly asked)

- ❌ "It's Almost Time" red urgency section *(removed 2026-04-29)*
- ❌ "Common Questions" inline FAQ on the homepage *(removed 2026-04-29; the dedicated `/faq` page is still live)*
- ❌ Gold "Special Perk for Statesman's Pass Holders" banner above Hosted Tables *(removed 2026-04-29)*
- ❌ "Hosted Group Tables / Gather your crew" badge on the Statesman ticket *(removed earlier)*
- ❌ "Learn More About the Statesman's Experience" link on the Statesman ticket *(removed earlier; the `/statesmans-pass` page still exists at the URL but is not currently linked from the homepage)*

---

## Audit + deploy hygiene

Before every push, run:
```
python scripts/audit_assets.py
```
6 checks must all PASS:
1. Image existence
2. Internal route resolution
3. In-page anchor resolution
4. Duplicate IDs
5. Carousel dot/slide match
6. Dead/missing named imports

GitHub Actions auto-deploys to GitHub Pages on push to `main`. Failures (typically TypeScript compile errors) text Mike directly. Deploy time: ~60–90 seconds.

---

## Backups

- This repo: `C:\Users\USER\countdown250` (working tree + git history)
- Cross-session memory backups: `C:\Users\USER\claude-backups\YYYY-MM-DD\` (per Mike's standing protocol; CLAUDE.md memory references this)
- Important docs (this file + `hosted-tables-program.md`) live in `docs/` so they travel with the codebase
