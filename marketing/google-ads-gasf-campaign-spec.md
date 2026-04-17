# Google Ads Campaign Spec — Great American State Fair

## Context
Great American State Fair was announced Apr 14, 2026. Search volume is live and rising as more news cycles hit (expected again at: UFC Freedom 250 / June 14, fair opening / June 25, July 3 events, etc.). We want to capture high-intent "Great American State Fair" searches with paid ads that point to the GASF landing page.

## Campaign name
`Countdown 250 – GASF Search`

## Campaign type
Search (text ads only, no display)

## Daily budget (recommended start)
**$30/day for 7 days to calibrate, then adjust.** Reasoning:
- Tracking is broken on existing campaigns, so budget small until fixed
- $30 × 7 = $210 test budget
- If CPC averages $1–2, this gives 100–200 clicks to learn

## Location targeting
- **Primary:** Washington D.C., Maryland (state), Virginia (state)
- **Secondary:** All 50 states + DC (national tier — since the Fair will draw national visitors)
- Start with primary only. Add secondary if conversion data supports it.

## Audience signals (optional, nice-to-have)
- In-market for travel / events
- Affinity: Patriotism enthusiasts, news junkies, event planners
- Age: 35–65, skew wealthy households

## Ad schedule
- All day, all week to start
- Review after 7 days — may need to concentrate on evening hours if sales data matches the Apr 15 evening-skew pattern

## Landing page
https://countdown250.allamericanball.com/great-american-state-fair-evening

## Ad group 1: `GASF Brand Match`
**Keywords (exact + phrase match):**
```
"great american state fair"
"great american state fair dc"
"great american state fair washington"
"great american state fair 2026"
"great american state fair tickets"
"great american state fair events"
"great american state fair july 3"
"great american state fair july 4"
"great american state fair evening"
"great american state fair national mall"
"great american state fair after"
"great american state fair schedule"
```

**Negative keywords (do not show ads for these):**
```
-jobs
-vendor
-exhibitor
-volunteer
-employment
-career
-hiring
```

## Ad group 2: `DC 250th Event Search`
**Keywords:**
```
"things to do dc july 3 2026"
"things to do dc july 4 weekend 2026"
"america 250 events dc"
"america 250 dc events"
"dc events 250th anniversary"
"independence day events washington dc 2026"
"washington dc july 4 2026"
"july 3 gala dc"
"july 3 black tie dc"
"july 3 events washington"
"dc 250th birthday events"
"america 250 gala"
```

## Ad group 3: `Black Tie DC Evening`
**Keywords:**
```
"black tie gala dc 2026"
"formal event dc july 4"
"dc black tie event"
"dc gala july 4 weekend"
"washington hilton event july 3"
"dc evening events july 4 weekend"
"dc formal ball 2026"
```

## Responsive Search Ads — copy

### Ad 1 (for Ad Group 1: GASF)
**Final URL:** `https://countdown250.allamericanball.com/great-american-state-fair-evening?utm_source=google&utm_medium=cpc&utm_campaign=gasf&utm_content=ad1`

**Headlines (up to 15, Google rotates):**
1. State Fair Evening Plans?
2. The Official Countdown 250 Ball
3. July 3 Black Tie Gala DC
4. Washington Hilton, July 3
5. Great American State Fair Week
6. The Formal Evening of 250th Week
7. After the Fair, the Ball
8. America's 250th Eve Gala
9. 3,000 Guests · 6 Ballrooms
10. Midnight Countdown to 250
11. Independence Eve Washington DC
12. 3 Blocks From the National Mall
13. Tickets Start at $225
14. Liberty · Patriot VIP · Statesman's
15. Lock In Before Prices Rise

**Descriptions (up to 4):**
1. Planning a DC trip for the Great American State Fair? Cap the day with the black-tie formal. July 3, Washington Hilton. Midnight countdown.
2. The Official Countdown 250 Ball. 3,000 guests, 6 ballrooms, 4 stages. Get tickets before prices increase.
3. Formal evening finale of Great American State Fair Week. Three blocks from the National Mall. Black tie. Tickets $225–$1,700.
4. Independence Eve at the iconic Washington Hilton. Premium open bars, live entertainment, midnight countdown. Reserve now.

**Sitelinks (4):**
- State Fair Evening Guide → `/great-american-state-fair-evening`
- Ticket Tiers → `/#tickets`
- Venue Info → `/#venue`
- About the Ball → `/#about`

**Callouts (6–8):**
- Washington Hilton
- July 3, 2026
- 7 PM – 1 AM
- Black Tie Gala
- 3,000 Guests
- Premium Open Bars
- Midnight Countdown
- All-Inclusive

**Structured snippet:**
- **Type:** Services
- **Values:** VIP Reception, Reserved Seating, Premium Open Bar, Midnight Countdown, Hero Awards Ceremony, Live Entertainment

### Ad 2 (for Ad Group 2: DC 250th Event Search)
**Headlines:**
1. America 250 DC Events Guide
2. July 3 Gala Washington DC
3. The Official Countdown 250 Ball
4. 250th Birthday Eve Celebration
5. DC's Premier America 250 Gala
6. July 4 Weekend Plan
7. Washington Hilton, July 3
8. Tickets Start at $225
9. Black Tie America 250 Gala
10. 3,000 Guest Ballroom Spectacle

**Descriptions:**
1. Planning your 250th anniversary DC trip? The Countdown 250 Ball is Independence Eve's premier black-tie gala. Lock in tickets.
2. 3,000 guests, 6 ballrooms, 4 stages, midnight countdown. July 3, Washington Hilton. Tickets from $225. Get yours now.

### Ad 3 (for Ad Group 3: Black Tie Evening)
**Headlines:**
1. Black Tie Gala DC July 3
2. Washington Hilton July 3
3. Formal Ball 250th Anniversary
4. The Official Countdown 250 Ball
5. DC's Premier July 3 Formal
6. Midnight Countdown Gala
7. Tickets Start at $225
8. Black Tie · Open Bar · Live Music
9. Presidential Stage Seating
10. America's 250th Eve Gala

**Descriptions:**
1. The formal evening of July 3. Washington Hilton. 3,000 guests. Black tie. Open bars. Midnight countdown to America's 250th year.
2. Reserved Presidential Stage seating available in Statesman's Concierge tier ($1,700). All tiers include premium open bars and entertainment.

## Tracking code
Add `?aff=googleGasf` (if Eventbrite allows) or use `gasfAds` as a separate Eventbrite tracking link.
**OR** (simpler) — use UTM params on the landing page URL. The GASF landing page is the landing target, not Eventbrite directly, so UTMs work.

All final URLs should include:
`?utm_source=google&utm_medium=cpc&utm_campaign=gasf&utm_content=[ad-variant]`

## Budget escalation rule
- If CPA (cost per conversion) < $50 after 200 clicks, increase budget to $60/day
- If CPA > $200 after 200 clicks, pause and rethink
- Track Eventbrite orders that come via the GASF landing page through UTMs / referrer analytics

## What to do right now
1. Log into Google Ads
2. Create new campaign → Search → Sales goal
3. Set budget: $30/day
4. Set locations: DC, MD, VA
5. Create the three ad groups with keywords above
6. Paste the ad copy for each
7. Set sitelinks, callouts, structured snippets
8. Point landing page URL to `/great-american-state-fair-evening`
9. Publish as paused → final review → enable
