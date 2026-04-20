# GASF Google Ads Campaign — Launch Playbook

**Last updated: 2026-04-20**
**Status: Ready to launch**
**Execution time: ~30-40 min**

---

## 🛑 BEFORE YOU LAUNCH — Do these first (10 min)

### 1. Fix the NYC Ball Drop bleed
NYC Ball Drop is currently at **$200/day with 0 tracked conversions over 30 days** ($5,084 spent). Don't stack a new campaign on top.

**Decide one:**
- **Option A (recommended):** Cut NYC Ball Drop to **$50/day** so we can see if pixel-enabled conversions come in now (pixels went live Apr 19)
- **Option B:** Pause NYC Ball Drop entirely while GASF launches
- **Option C:** Leave NYC Ball Drop alone — accept $200/day burn continues

My vote: A. Gives it one more week with real conversion tracking before killing it.

### 2. Verify Google Ads conversion action is actually active
Google Ads → Goals → Conversions. Look at the **"Purchase"** conversion action:
- Status should say **"Recording conversions"** or similar — NOT "No recent conversions" (that was the old broken state)
- "Count" setting should be **"One"** for purchases (not "Every")
- Conversion window: **30 days** click / **1 day** view

If it still says "Needs attention" — stop and tell me. The pixel is on Eventbrite but Google Ads might not be receiving events yet. We'll troubleshoot before launching.

### 3. Confirm Visa ••••4884 isn't flagged
Overnight briefing flagged Meta had a payment error and Google Ads may have similar card issues. Log into Google Ads → Billing & payments → make sure no warnings. $30/day × 7 days = $210 hold.

---

## 🎯 CAMPAIGN CONFIG — Step by step

Open Google Ads. Top left: **Create → New campaign**.

### Step 1 — Goal
- Select **"Create a campaign without a goal's guidance"** (NOT Sales/Leads/Traffic — those add features we don't want)
- Click Continue

### Step 2 — Campaign type
- Select **Search**
- Click Continue

### Step 3 — Conversion goals
- Click **"Use account-level goals"**
- Make sure "Purchase" is the ONLY included goal
- If other goals are listed (Page views, Engagement), click each and remove them from this campaign
- Click Continue

### Step 4 — Campaign name
```
Countdown 250 - GASF Search
```

### Step 5 — Bidding
- **Bid strategy:** Manual CPC with Enhanced CPC **(NOT auto-bidding)**
- Reason: We have 0 conversion history for this campaign. Auto-bidding has nothing to learn from. Manual CPC gives you price control.
- Set max CPC: **$3.00** (adjust down after first week of data)

### Step 6 — Networks
- ✅ Google Search
- ❌ Uncheck Search Partners
- ❌ Uncheck Display Network

### Step 7 — Locations
- **Target: Washington D.C., Maryland, Virginia**
- Click "Location options" → select **"Presence: People in or regularly in your targeted locations"** (NOT "People interested in")

### Step 8 — Languages
- English only

### Step 9 — Audience (optional but helpful)
Under **Audience segments**, add as "Observation" (not Targeting):
- In-market → Event Tickets
- In-market → Travel / Event Planning
- Affinity → News Junkies
- Affinity → Travel Buffs / Luxury Travelers
- Demographics → Household Income: **Top 10%** and **Top 11-20%**

Observation mode = these don't restrict who sees your ads; they just let you analyze performance by segment later.

### Step 10 — Budget
- Daily budget: **$30**
- Delivery method: Standard (not Accelerated)

### Step 11 — Ad schedule
- Leave all day / all week for now. Adjust after 7 days based on data.

### Step 12 — Device adjustments
- Leave at 0% for all devices initially

---

## 📝 AD GROUPS — Paste-ready

You'll create 3 ad groups. Click **"+ New ad group"** for each.

---

### AD GROUP 1: GASF Brand Match

**Ad group name:**
```
GASF Brand Match
```

**Default bid:** $2.50

**Keywords** — paste this whole block into the keywords box:
```
[great american state fair]
"great american state fair"
[great american state fair dc]
"great american state fair dc"
[great american state fair washington]
[great american state fair 2026]
"great american state fair 2026"
[great american state fair tickets]
[great american state fair events]
"great american state fair events"
[great american state fair july 3]
[great american state fair july 4]
[great american state fair evening]
"great american state fair evening"
[great american state fair national mall]
[great american state fair after]
[great american state fair schedule]
[great american state fair july 2026]
```

**Negative keywords (add at campaign level too):**
```
-jobs
-vendor
-vendors
-exhibitor
-volunteer
-volunteers
-employment
-career
-careers
-hiring
-sponsor
-free
-parking
-kids
-children
-family
```

---

### AD GROUP 2: DC 250th Event Search

**Ad group name:**
```
DC 250th Event Search
```

**Default bid:** $2.00

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
"america 250 washington"
"250th anniversary dc"
"fourth of july dc 2026 events"
```

---

### AD GROUP 3: Black Tie DC Evening

**Ad group name:**
```
Black Tie DC Evening
```

**Default bid:** $2.00

**Keywords:**
```
"black tie gala dc 2026"
"formal event dc july 4"
"dc black tie event"
"dc gala july 4 weekend"
"washington hilton event july 3"
"dc evening events july 4 weekend"
"dc formal ball 2026"
"washington dc formal gala"
"dc gala 2026"
"black tie event washington dc"
```

---

## 📢 RESPONSIVE SEARCH ADS — Copy-paste blocks

For each ad group, create **ONE** responsive search ad. Paste headlines and descriptions as separate lines.

---

### AD FOR AD GROUP 1: GASF Brand Match

**Final URL:**
```
https://countdown250.allamericanball.com/great-american-state-fair-evening?utm_source=google&utm_medium=cpc&utm_campaign=gasf&utm_content=brand
```

**Display path (2 fields):**
```
state-fair
evening
```

**Positioning pillars (every ad must emphasize at least one):**
1. **Official Countdown 250** — legitimacy / the definitive event
2. **All-inclusive** — food, drinks, entertainment included
3. **6 ballrooms, 4 stages, 3,000 guests** — scale / spectacle
4. **A celebration of a lifetime** — emotional / once-in-a-generation

**Do NOT mention specific ticket prices in ad copy.** Prices scare off awareness-stage traffic and undercut premium positioning. Tier info lives on the landing page.

**Headlines (max 30 chars each — all verified under limit):**
```
Official Countdown 250 Ball
An All-Inclusive Gala
A Celebration of a Lifetime
6 Ballrooms, 4 Stages
3,000 Guests · 6 Ballrooms
July 3 Independence Eve Gala
Midnight Countdown to 250
Black Tie. All-Inclusive.
State Fair Evening Plans?
Premium Open Bars All Night
Live Entertainment All Night
The Ball of the Generation
After the State Fair, the Ball
America's Biggest 250th Gala
Washington Hilton, July 3
```

**Descriptions (max 90 chars each — all verified under limit):**
```
Official Countdown 250 Ball. All-inclusive black-tie gala. Washington Hilton, July 3.
6 ballrooms, 4 stages, 3,000 guests. A celebration of a lifetime on Independence Eve.
Formal evening finale of State Fair Week. All-inclusive. Washington Hilton, July 3.
Countdown with 3,000 Americans to the 250th year. Open bars. Live entertainment.
```

---

### AD FOR AD GROUP 2: DC 250th Event Search

**Final URL:**
```
https://countdown250.allamericanball.com/america-250-dc-events-guide?utm_source=google&utm_medium=cpc&utm_campaign=gasf&utm_content=dc250th
```

**Display path:**
```
america-250
dc-events
```

**Headlines (max 30 chars each — all verified under limit):**
```
Official Countdown 250 Ball
An All-Inclusive Gala
America 250 DC Events Guide
A Celebration of a Lifetime
6 Ballrooms, 4 Stages
3,000 Guests · 6 Ballrooms
Your July 4 Weekend Plan
Washington Hilton, July 3
July 3 Independence Eve Gala
Black Tie. All-Inclusive.
Midnight Countdown to 250
Premium Open Bars All Night
Live Entertainment All Night
The Ball of the Generation
America's Biggest 250th Gala
```

**Descriptions (max 90 chars each — all verified under limit):**
```
Official Countdown 250 Ball. All-inclusive black-tie gala. Washington Hilton, July 3.
6 ballrooms, 4 stages, 3,000 guests. A celebration of a lifetime on Independence Eve.
DC's premier 250th Independence Eve gala. Three blocks from the National Mall.
Countdown with 3,000 Americans to the 250th year. Open bars. Live entertainment.
```

---

### AD FOR AD GROUP 3: Black Tie DC Evening

**Final URL:**
```
https://countdown250.allamericanball.com/?utm_source=google&utm_medium=cpc&utm_campaign=gasf&utm_content=blacktie
```

**Display path:**
```
black-tie
july-3
```

**Headlines (max 30 chars each — all verified under limit):**
```
Official Countdown 250 Ball
An All-Inclusive Gala
A Celebration of a Lifetime
Black Tie Gala DC July 3
Washington Hilton July 3
6 Ballrooms, 4 Stages
3,000 Guests · 6 Ballrooms
Black Tie. All-Inclusive.
Midnight Countdown to 250
Premium Open Bars All Night
Live Entertainment All Night
Luxury Gala Washington DC
The Ball of the Generation
Independence Eve Black Tie
Reserve Your Table Now
```

**Descriptions (max 90 chars each — all verified under limit):**
```
Official Countdown 250 Ball. All-inclusive black-tie gala. Washington Hilton, July 3.
6 ballrooms, 4 stages, 3,000 guests. A celebration of a lifetime on Independence Eve.
DC's premier Independence Eve black-tie gala. Three blocks from the National Mall.
Countdown with 3,000 Americans to the 250th year. Open bars. Live entertainment.
```

---

## 🔗 CAMPAIGN-LEVEL ASSETS — Set once, apply to all ad groups

After ad groups are built, go to **Assets** (left sidebar) → click each type → add at **Campaign level**.

### Sitelinks (add 4-6)
```
State Fair Evening Guide
  Description line 1: Pair the Great American State Fair with Independence Eve's premier gala.
  Description line 2: Tickets from $225. Washington Hilton.
  URL: https://countdown250.allamericanball.com/great-american-state-fair-evening

Ticket Tiers
  Description line 1: Three tiers of all-inclusive access.
  Description line 2: Premium open bars included at every level.
  URL: https://countdown250.allamericanball.com/#tickets

Venue & Directions
  Description line 1: Washington Hilton, 1919 Connecticut Ave NW.
  Description line 2: Three blocks from the National Mall.
  URL: https://countdown250.allamericanball.com/#venue

About the Ball
  Description line 1: 3,000 guests, 6 ballrooms, 4 stages.
  Description line 2: Independence Eve, America's 250th year.
  URL: https://countdown250.allamericanball.com/#about

Statesman's Pass
  Description line 1: Premium reserved-seating concierge tier.
  Description line 2: Presidential stage, VIP reception, concierge.
  URL: https://countdown250.allamericanball.com/statesmans-pass

Press & Media
  Description line 1: Press releases and media information.
  Description line 2: For media inquiries.
  URL: https://countdown250.allamericanball.com/press
```

### Callouts (add 8)
```
Washington Hilton
July 3, 2026
7 PM to 1 AM
Black Tie Gala
3,000 Guests
Premium Open Bars
Midnight Countdown
Reserved Seating Available
```

### Structured snippet
```
Header: Services
Values:
  VIP Reception
  Reserved Seating
  Premium Open Bar
  Midnight Countdown
  Hero Awards Ceremony
  Live Entertainment
```

### Price assets — SKIP
Per Apr 20 decision: prices are NOT shown in Google Ads (scare off awareness-stage traffic, undercut premium positioning). Tier pricing lives only on the landing page. Skip this asset type entirely.

### Business name
```
Countdown 250 Ball
```

### Business logo
Upload from: `C:\Users\USER\countdown250\public\images\logo.png` (or similar — check the folder for the hi-res logo)

---

## ✅ FINAL REVIEW BEFORE PUBLISHING

Before hitting **Publish**:
- [ ] Campaign status set to **Enabled** (not Paused)
- [ ] Daily budget = $30
- [ ] All 3 ad groups active
- [ ] Each ad group has at least one responsive search ad with 10+ headlines
- [ ] Negative keywords applied at campaign level
- [ ] Sitelinks, callouts, structured snippets visible in preview
- [ ] Final URLs all use `countdown250.allamericanball.com` (NOT Eventbrite direct — we want them to hit our site first so pixel fires)

Click **Publish**.

---

## 📊 WHAT TO EXPECT / WHEN TO REVIEW

**First 24 hours:**
- Ads will be in "Under review" — normal
- First impressions usually within 2-4 hours of approval
- Don't touch anything

**Day 3:**
- You should see 50-150 clicks across the 3 ad groups
- Check which ad group has lowest CPC (that's your strongest intent match)
- Check landing page time-on-site in GA4 — under 30 sec = landing page not matching the ad promise

**Day 7 (decision day):**
- Pull clicks, impressions, CTR, conversions per ad group
- If conversions > 0 and CPA < $75: increase budget to $60/day
- If conversions = 0 but CTR > 3%: keep running, landing page is the bottleneck
- If CTR < 2%: kill that ad group, ad copy isn't working
- Send me the data, I'll analyze

---

## 🔄 WHAT HAPPENS AFTER THIS

Once GASF is live and running, next waves (in order):

1. **UFC Freedom 250 campaign** (June 14 White House South Lawn event) — same playbook, different keywords
2. **Freedom 250 Grand Prix keyword campaign** — capture Aug 22 race weekend research traffic (even though Pre-Prix 250 is paused, this drives awareness for Countdown 250 brand)
3. **Retargeting campaign on Meta** — 1,005+ pixel-tagged site visitors ready to retarget
4. **LinkedIn Statesman's campaign** — premium-tier targeting

But only after GASF proves the attribution loop works end-to-end.

---

## 🆘 IF SOMETHING BREAKS

**Ad disapproved:** 90% of the time it's a Trademark issue on "Great American State Fair." If Google flags it, reply to the disapproval with "We are an adjacent event, not claiming affiliation with the fair. Our landing page includes disclaimer. Request review."

**Conversion tracking still says "Needs attention" after 48 hours:**
Reach out to Eventbrite Ashley (Tues Apr 21 call) and ask her to verify the pixel is firing server-side. Separately, check `pagead/1p-conversion` in browser dev tools on Eventbrite confirmation page.

**Can't find "Account-level goals" in Step 3:**
You might be on a newer Google Ads UI. Look for "Conversion goals" section — same thing, different label.

**Getting impressions but no clicks:**
CTR problem. Your ad copy isn't winning the auction-to-click moment. Let me know; I'll rewrite headlines.

**Lots of clicks, no conversions:**
Either (a) landing page issue or (b) ticket prices too high for the search intent. We'll look at session recordings and Eventbrite funnel.

---

## FILE LOCATIONS

This playbook: `C:\Users\USER\countdown250\marketing\google-ads-gasf-campaign-spec.md`
Landing page code: `C:\Users\USER\countdown250\src\pages\great-american-state-fair-evening.astro`
Hub page code: `C:\Users\USER\countdown250\src\pages\america-250-dc-events-guide.astro`
