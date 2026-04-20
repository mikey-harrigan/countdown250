# Morning Briefing — 2026-04-20 (Monday, 74 days to event)

Fresh data pulled from Eventbrite, Meta Ads Manager, and Google Ads just now.

---

## 📊 TOP-LINE NUMBERS

| Metric | Value | Change |
|---|---:|---|
| Net Sales | $37,131.52 | +$1,066 overnight |
| Tickets Sold | 83/2600 | +5 overnight |
| Tracked Revenue (`websitemain`) | $4,167.68 | +$1,189 overnight |
| Total Ad Spend (30 days, Google only) | $5,084.09 | — |
| Tracked ROAS (ad-dollars-to-tracked-sales) | **0.0x** | 💀 |

**The critical take:** you've spent $5,000+ on Google Ads in 30 days with 0 attributed conversions. Meanwhile 10 tickets / $4,167 came from free organic `websitemain` site traffic. This is a signal problem (pixel only just installed), but it's also a *strategy* problem worth addressing.

---

## 1️⃣ EVENTBRITE — The good news

### Tracking links (live attribution)
| Link | Views | Tickets | Sales | Note |
|---|---:|---:|---:|---|
| **websitemain** | **84** | **10** | **$4,167.68** | 🟢 All 5 overnight sales came from here |
| ImGoing FB tracking | 1 | 0 | $0.00 | Still flat |
| Email Blast (Mar 31) | 13 | 0 | $0.00 | Zero conversions, ever |
| FB Page | 0 | 0 | $0.00 | Dead |

### Eventbrite Ads
- Live at $15/day, runs through Apr 24
- 15 clicks, 1,501 impressions, $43 spent, conversion data not yet visible

### Pixels installed last night ✅
- **Meta Pixel** (940860418659873) — live, fires on Order Confirmation
- **Google Ads** (AW-1018113532 + label SPVpCIiW2pgcEP2bvOUD) — live, fires on Event Order Confirmation

Conversion data from here forward will be real. Everything pre-last-night is permanently uncountable.

---

## 2️⃣ META ADS MANAGER — The ImGoing mystery solved

You have exactly **one (1) Meta ad** in this account. Here's the full picture:

### The only campaign
- **Name:** "Post: 🚨 HURRY! Comment IMGOING below and we'll send you..."
- **Objective:** Post Engagement (optimizes for comments/reactions, NOT traffic or sales)
- **Budget:** $20/day
- **Schedule:** Apr 5, 2026 – Ongoing (14 days)
- **Toggle:** ON
- **Actual delivery status:** 🔴 **PAYMENT ERROR — NOT DELIVERING**

### Results over 14 days
| Metric | Value |
|---|---:|
| Impressions | 2,556 |
| Reach | 2,364 |
| Post engagements | 553 |
| Cost per engagement | $0.07 |
| **Total spent** | **$40.00** |
| **Should have spent** | $280 ($20 × 14) |
| **% of budget delivered** | ~14% |

### What this means

1. **The "ImGoing activity" you noticed = 553 Facebook comments/reactions.** Real people, on your existing Facebook page, engaging with the boosted post. Good social proof. Zero direct ticket sales.

2. **Your credit card has been declining Meta charges since ~Apr 5.** $40 spent instead of $280. Same payment problem that killed the earlier Eventbrite Ads campaign. Fix the card.

3. **Even fully funded, this ad would never drive sales.** Post Engagement objective = Meta optimizes for people who like/comment, NOT people who click through and buy. It's the wrong ad type for your goal.

4. **You have zero retargeting, prospecting, or Statesman's-targeted Meta ads.** Despite having Meta Pixel installed on the site since Apr 10 (with a 30-day retargeting audience now ready), none of it is being used.

---

## 3️⃣ GOOGLE ADS — The big spender

### 30-day account performance (Mar 21 – Apr 19)
| Metric | Value |
|---|---:|
| Clicks | 5,118 |
| Impressions | 80,558 |
| Cost | **$5,084.09** |
| CTR | 6.35% |
| **Conversions** | **0** ⚠️ |

### Campaigns (5 total, 1 active)

| # | Campaign | Budget | Status | Clicks | Cost | CTR | Conversions |
|---|---|---:|---|---:|---:|---:|---:|
| 1 | Website Traffic - Search - General | $59/day | **Paused** | 3,133 | $2,230.61 | 5.68% | 0 |
| 2 | **Countdown 250 - NYC Ball Drop** | **$200/day** | 🟢 Limited by budget | 1,985 | $2,853.49 | 7.81% | 0 |
| 3 | All American Ball 2013 | $1/day | Paused (no ads) | 0 | $0 | — | 0 |
| 4 | All American Ball - 2017 | $250/day | Paused (all groups paused) | 0 | $0 | — | 0 |
| 5 | All American Ball '25 | $100/day | Paused | 0 | $0 | — | 0 |

### Critical observations

- 🚨 **NYC Ball Drop campaign is now at $200/day — up from $52.70 a week ago.** That's nearly 4x. Spending pace $1,400/week. If you didn't authorize that increase, something's wrong.
- 🟢 **"Limited by budget" status** = Google thinks you're leaving clicks on the table at this budget. At $1.44 CPC, you're getting cheap clicks. CTR 7.81% is strong.
- 🔴 **Zero tracked conversions on $5,084 of spend.** This is 100% a pixel timing issue — the Eventbrite pixel just fired last night for the first time, and only fires on NEW Eventbrite purchases after install.
- 📢 **Account has a security alert:** "Protect your account from unauthorized activity" — still showing. Worth checking to make sure no one else is in your Google Ads account.
- 📢 **"Set up conversion tracking" alert still showing** — will clear once a real purchase comes through the Eventbrite pixel and Google verifies it.

---

## 🎯 STRATEGIC VIEW — Where you are right now

### The math problem

**Tracked revenue:** $4,167.68 from `websitemain` (free organic)
**Ad spend last 30 days:** $5,084.09 (all Google) + $40 (Meta) = **$5,124.09**
**Ad-attributed revenue:** $0 (because of broken pixel — but now fixed going forward)

Even if we generously assume 25-50% of the $36,000+ in historical sales came from Google Ads *somehow* (impossible to verify), the ROAS is still weak because your highest-value tier (Statesman's $1,700) conversions came from news-cycle-driven organic search, not paid ads.

### The actionable problem

1. **Your real channel is organic search.** The Apr 15 pattern holds. Every news cycle = sales spike. The GASF landing page, America 250 hub, and Statesman's page are doing their job.
2. **Paid ads are currently a money furnace** with broken payment processing (Meta) and unmeasurable outcomes (Google — though this fixes tomorrow as pixel starts firing).
3. **None of your channels are retargeting.** Meta Pixel has been collecting audience data since Apr 10. You have 1,005+ site visitors ready to retarget. Nobody is doing it.

---

## 🔴 P0 — WHAT TO DO FIRST (30 minutes)

1. **Fix the Meta payment method.** Go to `business.facebook.com/settings/payments` → check the card on file → update or add a new one. Your ad has been throttled to 14% delivery since Apr 5.
2. **Verify Google Ads security alert.** Click the "Protect your account from unauthorized activity" link. Make sure no unknown users, admins, or linked accounts exist.
3. **Verify the $200/day NYC Ball Drop budget was intentional.** If not, dial it back to $52.70 or even lower until we see conversions fire.

## 🟠 P1 — THIS MORNING (60-90 minutes)

4. **Test a fake checkout** to verify pixels are firing. Use Meta Events Manager Test Events + Google Ads real-time conversion view. Walk through clicking Buy Tickets → Initiate Checkout (don't complete). If events show up, pixels are working.
5. **Send the 3 calendar submission emails** from `C:\Users\USER\countdown250\marketing\` (`calendar-submission-destinationdc.md`, `-freedom250.md`, `-freedom250gp.md`).
6. **Kill or pivot the Meta ImGoing ad.** Either fix payment AND change objective to Traffic/Conversions (not Engagement), or pause it entirely. It's generating engagement, not tickets.

## 🟡 P2 — THIS WEEK

7. **Build a Meta retargeting campaign** using the 30-day audience Meta Pixel has been collecting. Point it at the `websitemain` page with a "come back and buy" angle.
8. **Audit Google Ads keywords in NYC Ball Drop campaign.** At $200/day, we need to know which keywords are eating budget without converting.
9. **Launch GASF-specific Google Ads campaign** (spec already drafted in `google-ads-gasf-campaign-spec.md`). Cheaper, more targeted, better intent match.
10. **Decide on Google Ads conversion tracking Apr 21 call with Ashley.** Push her hard on the retargeting export question.

---

## 🤔 OPEN QUESTIONS FOR YOU

1. **Did you authorize the NYC Ball Drop budget increase to $200/day?** If yes, why? If no, we need to roll it back.
2. **Is there a payment method issue on your Visa ****4884?** Both Meta AND Google Ads have had payment-related throttling. The card might be at its limit or flagged.
3. **What's the source of that "a lot of activity" you noticed on ImGoing?** Now you know it's the 553 Facebook post engagements. Does that change your mental model?

---

## 🏁 BOTTOM LINE (one paragraph)

You have $37,131 in sales, 83 tickets, and your REAL engine is organic site traffic (10 tickets / $4,167 tracked in 2 days via `websitemain`). Your paid channels are broken: Meta ad has a payment error and wrong objective ($40 of $280 intended), Google Ads is spending $200/day on an unconverting campaign that jumped 4x in budget recently. Pixels finally fire from last night forward, so today's conversion data will be real. Priority 1: fix Meta card, verify Google Ads is legit (not hacked), verify $200/day was intentional. Priority 2: send 3 pending calendar emails that leverage the organic channel that's actually working. Priority 3: build Meta retargeting off the pixel audience that's been sitting idle since Apr 10.
