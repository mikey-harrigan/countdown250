# LinkedIn Campaign Spec — Statesman's Concierge Pass

## Why LinkedIn
The $1,700 Statesman's Pass buyer doesn't click a Facebook ad. They live on LinkedIn. Confirmed by the Apr 15 Elizabeth McCormick purchase — a cold stranger converted on the premium tier, which means the audience exists and is reachable. LinkedIn lets us target with job-title + firmographic precision Facebook can't match.

## Landing page
`https://countdown250.allamericanball.com/statesmans-pass` (recently enhanced with premium SEO, direct Eventbrite CTA, hour-by-hour evening timeline, FAQ).

**Tracking URL for all LinkedIn ads:**
```
https://countdown250.allamericanball.com/statesmans-pass?utm_source=linkedin&utm_medium=paid&utm_campaign=statesmans&utm_content={ad-variant}
```

**Eventbrite tracking link to create separately:** `liStatesmans`

## Campaign type
**Sponsored Content** (feed ads) — standard for premium B2B reach. Optional later addition: **Message Ads** (InMail) for the top-200 target list, but start with Sponsored Content for volume.

## Campaign structure
Create ONE campaign with FIVE audiences (ad sets) so you can measure which audience converts best:

### Audience 1 — DC C-suite
- **Locations:** Washington D.C., Maryland, Northern Virginia
- **Job titles:** CEO, CFO, COO, President, Chief [any], Managing Director, Managing Partner, Senior Partner, Executive Director, General Counsel
- **Company size:** 201+ employees
- **Seniority:** CXO, VP, Director, Partner
- **Optional interest:** galas, philanthropy, events

### Audience 2 — Political & government class
- **Locations:** D.C., MD, VA
- **Job titles:** Political Consultant, Government Relations, Senior Advisor, Chief of Staff, Legislative Director, Policy Director, Principal, Lobbyist
- **Industries:** Public Policy, Government Administration, Political Organizations, Public Affairs
- **Seniority:** Director+

### Audience 3 — Senior military & defense
- **Locations:** D.C., MD, VA + Pentagon, Fort Belvoir, Quantico-area zips
- **Job titles:** Colonel, Captain (Navy), General, Admiral, Flag Officer, Senior Executive Service, Defense Executive
- **Industries:** Defense & Space, Government Administration, Military
- **Companies (optional seed):** Lockheed Martin, Raytheon, Northrop Grumman, Boeing Defense, L3Harris, General Dynamics, BAE Systems

### Audience 4 — Law & consulting partners
- **Locations:** D.C., MD, VA
- **Job titles:** Partner, Senior Partner, Principal, Managing Director
- **Industries:** Law Practice, Legal Services, Management Consulting, Government Relations
- **Companies (seed list for lookalike):** Covington & Burling, Arnold & Porter, Akin Gump, Hogan Lovells, Kirkland & Ellis DC, McKinsey DC, Deloitte Federal, Booz Allen Hamilton, Bain DC, BCG DC
- **Seniority:** Partner, Director+

### Audience 5 — Event & hospitality industry
- **Locations:** D.C., MD, VA + DC metro plus travel-in markets (Philadelphia, Richmond)
- **Job titles:** Event Director, VP Marketing, VP Events, Corporate Events Manager, Event Production, Chief Marketing Officer
- **Industries:** Events Services, Hospitality, Marketing & Advertising
- **Optional:** Gala planners, Non-profit development, Philanthropy

## Budget
**Start:** $40/day × 5 ad sets = **$200/day total** for 7 days to calibrate
**Reasoning:** LinkedIn CPCs are $7–15 typically. At $40/ad set, each audience gets 3–6 clicks/day = 20+ data points over a week. Enough to spot the top-converting audience.
**Escalation rule:** After 7 days, reallocate 70% of budget to top 2 audiences by conversion rate. Pause bottom 2.

## Bid strategy
Start with **Maximum Delivery** (LinkedIn auto-optimizes). After 100 clicks, if CPC is > $15, switch to **Target Cost Bidding** with a $12 cap.

## Creative — 4 ads per audience (16 total)

### Ad format: Single image sponsored content
**Image specs:** 1200×628 or 1200×1200 (LinkedIn accepts both). Use the `/images/event/statesman-vip-dinner.png` or a ballroom establishing shot. Text overlay: "THE STATESMAN'S PASS · JULY 3, 2026 · WASHINGTON HILTON"

### Ad variant 1 — The Room Where It Happens
**Headline:** The Room Where It Happens. July 3, 2026.
**Intro text:**
> Two hundred seats. Reserved Presidential Stage seating. Dedicated concierge. The Official Countdown 250 Ball — Washington D.C.'s black-tie gala on the eve of America's 250th birthday. The Statesman's Pass is built for the guests whose evening demands more than a seat.
>
> Washington Hilton. July 3, 2026. $1,700.
**CTA button:** Learn More

### Ad variant 2 — Built For Your Evening
**Headline:** Your Clients Will Remember Where You Took Them the Night America Turned 250.
**Intro text:**
> On the eve of America's 250th birthday, 3,000 guests will gather at the Washington Hilton. Two hundred of them will do so in the Statesman's tier — private VIP entrance, reserved Presidential Stage seating, premium fine dining, dedicated concierge, backstage access.
>
> Corporate and group packages available. Independence Eve, 2026.
**CTA button:** Request Details

### Ad variant 3 — The Pairing
**Headline:** Great American State Fair by Day. The Countdown 250 Ball by Night.
**Intro text:**
> July 3, 2026. The Great American State Fair runs on the National Mall through Independence Eve. The Official Countdown 250 Ball delivers the formal evening three blocks away at the Washington Hilton.
>
> The Statesman's Pass ($1,700) reserves your seat on the Presidential Stage for the midnight countdown to America's 250th year.
**CTA button:** View Details

### Ad variant 4 — Scarcity / Price
**Headline:** 200 Seats. One Night. The 250th.
**Intro text:**
> The Statesman's Concierge Pass to The Official Countdown 250 Ball is limited to 200 guests across the entire event. Early-release pricing is $1,700 per guest. Prices increase as the event approaches.
>
> July 3, 2026. Washington Hilton. Reserved Presidential Stage seating.
**CTA button:** Get Tickets

## Conversion tracking

Create a **LinkedIn Insight Tag** (ask the Eventbrite rep to add it to the checkout page) and register two conversion events:
- **Purchase** — fires on Eventbrite order complete (primary)
- **Inquiry form submit** — fires on `/statesmans-pass` inquiry form submit (secondary, since some premium buyers prefer inquiry over direct purchase)

If LinkedIn Insight Tag setup isn't possible yet, track via UTM params and Eventbrite tracking link `liStatesmans` as a proxy.

## Weekly review ritual

Every Monday, check:
1. **Clicks / CPC per audience** — is one ad set consistently cheaper?
2. **Conversion rate per audience** — clicks are meaningless if no tickets sell
3. **Cost per Statesman's Pass sold** — the north-star metric. If < $200, scale hard. If > $500, rethink.
4. **Best-performing ad variant** — pause bottom 2, produce variants of top 2

## Long-term: InMail for the top 50

Once Sponsored Content proves the audience converts, run a **Message Ads (InMail)** campaign to a hand-picked list of 50 top DC prospects. Personalized. Subject line: *"An invitation to the Statesman's experience — July 3, 2026"*. CPC is high but conversion on warm 1-to-1 outreach is 3–5x Sponsored Content.

## Launch checklist

- [ ] LinkedIn Campaign Manager account created + billing attached
- [ ] LinkedIn Insight Tag installed (on site + Eventbrite checkout if possible)
- [ ] Two conversion events registered
- [ ] 5 audiences created
- [ ] 16 ads created (4 variants × 4 image-matched campaigns, or simpler: 4 variants per ad set rotating)
- [ ] UTMs on all final URLs
- [ ] Eventbrite `liStatesmans` tracking link created
- [ ] $200/day budget set, 7-day calibration window
- [ ] Calendar reminder set for day-7 review

## Budget reality check

$200/day × 7 days = $1,400 calibration. If zero Statesman's passes sell from LinkedIn after $1,400 spent, we've learned something expensive but definitive (either the copy, the landing page, or the audience targeting is wrong — we'd iterate). If **even one Statesman's sells** from LinkedIn, you recoup $300 of the spend. Two sales = profit. The math is asymmetric in your favor given the tier price.
