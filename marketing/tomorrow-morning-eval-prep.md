# Tomorrow Morning — Countdown 250 Acceleration Eval

**Goal:** Evaluate current state of all paid media + Eventbrite, identify what's working, kill what's not, scale what is. In under 90 minutes.

**Sequence:** You gather data (15 min), we analyze together (45 min), we execute changes (30+ min).

---

## PLATFORM 1 — Meta (Facebook + Instagram) Ads

**Open:** Meta Ads Manager (business.facebook.com/adsmanager/)

**Paste these into chat:**

### 1.1 Campaign overview — LAST 7 DAYS
Go to the **Campaigns** tab, set date range to **Last 7 days**, select these columns:
- Campaign name
- Delivery status (Active / Paused / Completed / Rejected)
- Amount spent
- Impressions
- Link clicks (or Reach)
- CPC
- CTR
- Results / conversions (whatever metric is the optimization goal)

Copy the summary table. Format doesn't matter — I'll parse whatever format paste gives.

### 1.2 Same columns but LAST 30 DAYS
Same view, just toggle date to **Last 30 days**. Paste separately.

### 1.3 Individual ad performance for "ImGoing"
You mentioned ImGoing has had activity. Click into that campaign/ad set/ad (whatever level it exists at) and paste:
- Ad name
- Creative/copy
- Targeting summary (audiences, locations, ages, interests)
- Performance: impressions, clicks, CTR, cost per result, results type
- When it started / current status

### 1.4 Meta Pixel events
Go to **business.facebook.com/events_manager** → select your pixel (ID `940860418659873`) → **Overview** tab → Last 7 days.

Tell me:
- Events firing (PageView, ViewContent, InitiateCheckout, Purchase, Lead, etc.)
- Total event count per event in last 7 days
- Whether events from **Eventbrite domain** are firing (this tells us if your pixel setup from the Apr 17 call is actually working)

### 1.5 Custom Audiences
Go to **Audiences** → tell me:
- What Custom Audiences exist (Inaugural Guest List, Website Visitors, etc.)
- Size of each (Meta shows audience size)
- Which ads are targeting which audiences

---

## PLATFORM 2 — Google Ads

**Open:** ads.google.com

**Paste these into chat:**

### 2.1 Campaign overview — last 7 days
Campaigns tab → Date range: **Last 7 days**. Columns: Campaign, Status, Budget, Cost, Impressions, Clicks, CTR, Avg CPC, Conversions, Conv. rate, Cost/conv.

Paste the table.

### 2.2 Same thing — last 30 days
Toggle date, paste.

### 2.3 Conversion tracking status
This is the one that was broken. Go to **Goals** (left sidebar) → **Conversions** → **Summary**.
Tell me:
- Purchase conversion status (Recording / Needs attention / No recent conversions / etc.)
- How many purchase conversions in last 7 days
- How many in last 30 days
- Any warnings or errors shown

### 2.4 NYC Ball Drop campaign detail
Click into the NYC Ball Drop campaign → paste:
- Current daily budget
- Top 10 keywords by spend + their conversion counts
- Any keywords flagged as low quality score
- Whether the campaign has run into any daily budget caps

### 2.5 Has the GASF campaign launched?
I spec'd out a full Great American State Fair Google Ads campaign on Apr 17 (see `google-ads-gasf-campaign-spec.md`). Tell me:
- Did you launch it? (Y/N)
- If yes: name + performance
- If no: no problem, we launch it tomorrow

---

## PLATFORM 3 — Eventbrite

**Open:** eventbrite.com/organizations

### 3.1 Sales snapshot — total as of this morning
Go to your event dashboard. Tell me:
- **Total tickets sold** (was 72 on Apr 17)
- **Total revenue** (was $31,740 face value on Apr 17)
- **Sales by tier** (Liberty / Patriot VIP / Statesman's) — quantities + revenue

### 3.2 Daily sales breakdown since Apr 15
Go to **Reporting → Orders** or **Sales → Revenue Report**. Change view to **Daily** or export orders to CSV.

For each day Apr 15 through today, tell me:
- Number of orders
- Revenue
- Any standout single orders (e.g., the $3,890 Elizabeth McCormick type)

### 3.3 Tracking links report
Go to **Marketing → Tracking Links** and paste the full table (every link, page views, tickets sold, sales).

This is where we'll see if `websitemain` is now showing traffic (since we installed it Apr 17) and what the **FacebookPromoImGoing0404** has done.

### 3.4 Promo codes report
Go to **Marketing → Promo Codes** and paste the table showing each code's name, uses count, revenue generated.

Specifically watching: how many **IMGOING** redemptions total now (was 3 on Apr 17).

### 3.5 Eventbrite Ads campaign results
You relaunched two Eventbrite Ads campaigns on Apr 17:
- "Increase Awareness" — $15/day
- "Drive Traffic" — $15/day
Both running through Apr 24.

Go to **Marketing → Eventbrite Ads** and paste:
- Status of each campaign (Active / Paused / Out of budget)
- Impressions, clicks, CPC, tickets sold per campaign
- Total spent so far

### 3.6 Pixel status (post-April-17 rep call)
Did you finish pasting the pixel IDs the rep showed you?
- **Meta Pixel** added? (ID should be `940860418659873`)
- **Google Ads pixel** added? (ID `AW-1018113532`)
- **Meta Conversions API token** generated and added? (this is the one I walked you through — generating in Meta Events Manager)

If not yet, we'll do it tomorrow morning as step 1 (takes 10 min).

### 3.7 Order form
Did you add the **"How did you hear about this event?"** dropdown question to the order form?
If not, we add it tomorrow (5 min).

### 3.8 Confirmation page / email
Did you update with the pre-written share copy from `social-share-flow.md`?
If not, we update tomorrow (15 min).

---

## PLATFORM 4 — Website traffic (bonus — free and public)

**Open:** Any of these you have set up:
- Google Search Console (search.google.com/search-console) — if you completed setup from my `google-search-console-setup.md` guide
- Google Analytics — if connected
- Any site analytics tool

**Tell me:**
- Total site sessions last 7 days
- Top landing pages (home, GASF, Statesman's, etc.)
- Top search queries bringing traffic (if GSC is set up)
- Traffic source breakdown (organic, direct, social, referral, paid)

---

## MY HYPOTHESES GOING IN

Based on what we know from Apr 17:

### The ImGoing question — three possibilities
Mike says ImGoing had "a lot of activity." Possibilities ranked:

1. **Someone reshared the Marleen Beck-style social post.** If a buyer posted "I'm going" on Facebook and it got reshared, every click goes to `FacebookPromoImGoing0404` tracking link. Would show as tracking link views spike without promo code redemption spike.

2. **A new Facebook ad running ImGoing creative.** If there's a paid campaign using ImGoing copy, we'd see spend + impressions in Meta Ads Manager.

3. **Organic Facebook page activity.** If the Facebook page post got algorithmic push, organic reach could explain it without any paid spend.

**How we tell them apart:** Cross-reference tracking link views (Eventbrite) vs. ad spend (Meta) vs. IMGOING promo redemptions (Eventbrite). The pattern will tell the story.

### Expected state of other channels
- **Google Ads NYC Ball Drop:** likely still burning $52/day with 0 attributed conversions (conversion tracking was broken Apr 17)
- **Eventbrite Ads (the 2 new ones):** ~$210 spent total, probably 20–60 clicks, likely 0–2 tickets sold. Small data, but informative.
- **Tracking links:** `websitemain` should now show 20–100 views depending on site traffic. Still probably 0 tickets attributed because most buyers came via news-cycle organic.
- **Total sales:** 72 + some number of new sales. I'd expect 3–10 more tickets in the 4 days since Apr 15, driven by organic traffic continuing.

### What I want to kill vs. scale
- **Kill candidate:** NYC Ball Drop Google Ads if conversion tracking is still broken and/or if the keywords aren't aligned with news-cycle search. Redirect to GASF campaign.
- **Scale candidate:** Whatever created the ImGoing activity bump. If it's organic social from buyers, we productize it (see `social-share-flow.md`). If it's a lucky ad, we clone it.

---

## TOMORROW'S EXECUTION AGENDA (after data review)

Depending on what we find, here's the priority order for action:

1. **Pixel setup completion** (10 min) — if not done, do it first. Everything else is wasted money without tracking.
2. **Kill underperformers** (15 min) — pause anything burning cash with zero attribution.
3. **Launch GASF Google Ads campaign** (25 min) — paste the spec from `google-ads-gasf-campaign-spec.md` into Google Ads.
4. **Clone whatever drove ImGoing activity** (15 min) — if it's organic, amplify with spend. If it's paid, expand targeting.
5. **Submit outstanding 3 emails** — Destination DC, Freedom 250 umbrella, Freedom 250 Grand Prix (all already drafted, ~10 min to send each).
6. **Update Eventbrite order form + confirmation flow** — if not done Apr 17/18 (20 min).
7. **Optional: LinkedIn Statesman's campaign launch** — if we have budget headroom (30 min, uses spec from `linkedin-statesmans-campaign-spec.md`).

---

## WHAT TIME TOMORROW?

When you wake up, message me with:
- **"Ready"** — then I'll ping you the prompt to paste the Platform 1 data
- Or just paste your Meta Ads Manager screenshot-as-text and we start immediately

I can start as early as you want. Let me know what "early" means — 6 AM? 7 AM? Otherwise I assume 8ish.
