# Eventbrite vs. Site — Gap Analysis (Phase 1 Recon)

**Date:** 2026-04-26
**Eventbrite event URL:** https://www.eventbrite.com/e/the-official-countdown-250-ball-washington-dc-tickets-1982528927390
**Site canonical pages compared:**
- `src/pages/hosted-group-tables.astro` (full Hosted Group Tables spec)
- `src/pages/index.astro` — Hosted Tables panel (Host + Guest) at lines ~485–550
- `src/pages/statesmans-pass.astro` (Statesman's Concierge Pass overview)

---

## TL;DR

**The biggest gap by far:** The site has a fully built **Hosted Group Tables** program — Founding Hosts, Toast to the Hosts, a public list of forming groups, a 10+ paid members threshold for signage, a June 20 cutoff, an in-checkout group dropdown — and **none of it appears on the Eventbrite event page**. A guest who clicks "Get Tickets" from the home page (where we just locked in "WE do the work… YOU get the credit!") lands on an Eventbrite page that doesn't mention Hosted Tables, Hosted Groups, Founding Hosts, or any of it. The funnel is broken at the handoff.

Everything else is secondary.

---

## A. CRITICAL GAPS — Hosted Group Tables program is invisible on Eventbrite

### A1. Eventbrite event description has zero mention of:
- Hosted Group Tables / Hosted Groups
- Founding Hosts
- "Toast to the Hosts" signature moment
- The list of groups currently forming (universities, neighborhoods, industries)
- The June 20, 2026 cutoff for Founding Host table signage
- The Statesman's Concierge Area being where Hosted Groups are seated

### A2. Statesman's Concierge Pass description on Eventbrite does NOT mention Hosted Group Tables as a benefit
The site's `statesmans-pass.astro` page positions Hosted Group Tables as the headline benefit. Eventbrite's $1,700 ticket description lists concierge, expedited entry, Presidential Stage seating, backstage access, etc. — but not "be part of a Hosted Group with your alumni / neighbors / industry circle."

### A3. Unverified — does the order form actually have the group-selection question?
The site's "How It Works" promises:
> "A short question in the Eventbrite checkout asks whether you're joining an existing Hosted Group, proposing a new one, or attending solo."

**I cannot verify this from the public page** — it only appears after starting checkout. **This is the single most important thing to verify.** If that question doesn't exist, the program literally has no intake mechanism.

→ **Action for Mike:** Either (a) walk through the checkout yourself and screenshot the order form questions, OR (b) let me drive Chrome to start a checkout and capture it.

### A4. No public list of Hosted Groups inside Eventbrite
The site shows "Hosted Groups Currently Forming" — buyers need this list visible at the point of purchase so they know which exact name to enter. If they have to leave Eventbrite to look it up on the site, conversion friction goes way up.

### A5. No CTA / link from Eventbrite back to the Hosted Group Tables page
At minimum, the description should link out to `https://countdown250.allamericanball.com/hosted-group-tables` so Eventbrite-first buyers can read the full program before committing.

---

## B. SECONDARY ISSUES on the Eventbrite page

### B1. Date wording confusion
Title shows "Friday, July 3–Saturday, July 4, 2026" but description treats it as a July 3 event. Event time is 7 PM–1 AM. Both are technically correct (the ball runs past midnight) but a casual reader sees "two days" and gets confused. Recommend: "Friday, July 3, 2026 — 7 PM through midnight (ends ~1 AM Saturday)."

### B2. "Black-Tie Opt." is ambiguous
Reads as "Black-Tie Optimal" or "Black-Tie Optional"? In the tagline string. Spell out: "Black-Tie Optional" (or whichever it actually is — I'm assuming optional).

### B3. No FAQ section on Eventbrite
The site has FAQ content. The Eventbrite page has none. This is the #1 thing buyers re-read before pulling the trigger on a $1,700 purchase.

### B4. No "How did you hear about us?" question
Per `master_checklist.md` P1 item #13 — flagged 10+ days ago, still not done. Critical because Google Ads conversion tracking has been broken for weeks. Without this you have no attribution at all.

### B5. Refund policy is one word: "No refunds"
For a $1,700 ticket, this is harsh. Recommend a one-line softener: "All sales final. Tickets are transferable up to [date] — contact [email] to transfer."

### B6. Missing hotel block details
Description references discounted hotel rooms but no rate, code, or booking link visible. Wealthy out-of-towners will book a hotel before they commit to the ticket; if the hotel block isn't easy, they pick a different gala.

### B7. Webcast mentioned but no detail
"Live webcast" is a feature in the description but no info on how to watch, who can watch, or whether it's a separate purchase. Either flesh it out or remove the mention.

### B8. No mention of the Statesman's VIP Dinner image / specific food experience
The Statesman's Concierge Pass description on Eventbrite is text-only with no visual cue of the upgrade. People buy luxury with their eyes.

### B9. Tags are minimal: just "Community, Gala"
Add: "America 250," "July 4," "Independence Day," "Washington DC events 2026," "Black tie gala," "New Year's Eve style ball" — every tag is a search hit.

### B10. Eventbrite Ads / paid promotion alignment
Eventbrite Ads campaign is running at $15/day per the Apr 19 overnight notes. If the Hosted Tables story isn't on the page, the ad spend is selling against an incomplete pitch.

---

## C. WHAT'S WORKING WELL on Eventbrite

- Three clear ticket tiers with prices and "(Price will go up very soon)" urgency
- "Extremely limited. Expected to sell out early." on the Statesman's Pass — good scarcity copy
- Visual carousel present (5 slides)
- Venue name and address are correct and clear
- Time block is correct
- Existing pricing matches what's on the site

---

## D. WHAT I COULD NOT SEE (need backend access)

These require either Mike screenshotting Eventbrite Manager, or me driving Chrome through a logged-in session:

1. Custom order form questions (does the Hosted Group selection question exist? what dropdown values? required vs. optional?)
2. Confirmation email content (is the share-to-friends flow live?)
3. Post-purchase landing page (does it surface Hosted Groups again?)
4. Any hidden / promo-code-gated ticket types
5. Affiliate tracking link reports (websitemain, etc.)
6. Eventbrite Ads campaign current settings
7. "How did you hear" question — confirmed not in public view, but might be in checkout

---

## E. PROPOSED NEXT STEPS (deliberately small to avoid context blowout)

**Phase 2 (next):** Reserved Table program review from a guest's POV — friction analysis + recommendation to keep, simplify, or restructure. ~5 min, no Chrome needed.

**Phase 3 (after Phase 2):** Detailed Eventbrite implementation playbook — exact copy + click paths. Requires either screenshots from Mike OR a quick Chrome session to verify the current order form state.
