# Post-Purchase Social Share Flow

## Why this matters (data-backed)
On Apr 15, Marleen Beck bought a ticket, used the Eventbrite "I'm Going" share on Facebook, and Matthew Beck converted 9 hours later as a direct result. That is one confirmed referral sale in a single day — from ONE buyer's share. If we optimize this flow, even a 10% share rate on 72 current buyers = ~7 referral opportunities. At an average order of ~$500 that's ~$3,500 in referral revenue just from improved sharing.

## What to do (Mike, in Eventbrite)

### 1. Customize the order confirmation page
**Eventbrite → Manage Event → Order Options → Order Confirmation Page**

Replace the default confirmation message with:

```
Congratulations! You're officially part of history.

You'll be there the night America turns 250. One night only.
July 3, 2026 · Washington Hilton · Black tie.

🎉 SHARE THE NEWS:
Tell friends you're going — the best way to celebrate is together.
Post on Facebook, Instagram, or LinkedIn with the #Countdown250 hashtag,
or use the "I'm Going" button below to share directly.

Save this confirmation. Your ticket will arrive by email from Eventbrite.
```

### 2. Customize the confirmation email
**Eventbrite → Manage Event → Emails to Attendees → Order Confirmation Email**

Add a prominent share section after the ticket details:

**Subject:** Your Countdown 250 Ticket Is Confirmed — Share the News

**Share section:**
```
🇺🇸 LET FRIENDS KNOW YOU'LL BE THERE

On July 3, 2026, you'll be at the Washington Hilton celebrating America's
250th birthday. Your friends will want to know — some will want to join you.

Three quick ways to share:

FACEBOOK: "I just got my ticket to the Official Countdown 250 Ball — the
premier gala launching America's 250th birthday, July 3 at the Washington
Hilton. Who's coming with me? countdown250.allamericanball.com"

INSTAGRAM STORY: Use the "I'm Going" button or post:
"Countdown begins. July 3. DC. 🇺🇸 #Countdown250 #America250"

LINKEDIN: "Delighted to be attending The Official Countdown 250 Ball on
July 3, 2026 — the formal evening celebration of America's 250th
anniversary at the Washington Hilton. Looking forward to an
extraordinary evening." countdown250.allamericanball.com
```

### 3. Create a unique tracking link for referred purchases
**Eventbrite → Marketing → Tracking Links → Create**

- **Code name:** `socialShare` (alphanumeric only)
- Use this as the aff param in the shareable link given to buyers

Update the share copy so the link is:
`https://www.eventbrite.com/e/the-official-countdown-250-ball-washington-dc-tickets-1982528927390?aff=socialShare`

Any buyer who uses this link gets tagged as a "socialShare" source. Won't distinguish Marleen-vs-Matthew-level precision, but gives an aggregate referral count.

## Pre-written share assets (copy/paste into confirmation email)

### Facebook post (long form)
> I just got my ticket to **The Official Countdown 250 Ball** — the premier gala launching America's 250th birthday, July 3 at the historic Washington Hilton. 3,000 guests, live entertainment, midnight countdown to July 4.
>
> Who's in? Get yours: countdown250.allamericanball.com

### Facebook post (short form)
> July 3, Washington Hilton. Black tie. Midnight countdown to America's 250th birthday. I'm going. Who's with me? countdown250.allamericanball.com

### Instagram caption
> July 3, 2026.
> The Washington Hilton.
> 3,000 guests.
> Black tie.
> Midnight countdown to America's 250th.
>
> I'll be there. 🇺🇸
>
> countdown250.allamericanball.com
> #Countdown250 #America250 #JulyThird #WashingtonDC

### LinkedIn post
> Delighted to be attending **The Official Countdown 250 Ball** on July 3, 2026 — the formal evening celebration of America's 250th anniversary at the Washington Hilton in Washington, D.C.
>
> For a once-in-a-generation moment, looking forward to an extraordinary evening alongside leaders, dignitaries, and distinguished Americans from across the nation.
>
> countdown250.allamericanball.com

### Twitter/X
> July 3. Washington Hilton. Midnight countdown to America's 250th birthday. I'm going. 🇺🇸 countdown250.allamericanball.com #Countdown250

### SMS / text message template
> Hey — I got my ticket to the Countdown 250 Ball, July 3 at the Washington Hilton. It's the black-tie gala for America's 250th birthday. 3,000 guests, midnight countdown. You should come. Link: countdown250.allamericanball.com

## Branded social image

Use the existing Open Graph image at:
`/public/images/logos/countdown250-og-share.png` (1200×630, already optimized for social)

This image auto-shows when someone shares the site URL on Facebook / LinkedIn / Twitter. No extra work needed — Eventbrite's "I'm Going" share button automatically pulls the OG image from the linked page.

**IF you want a dedicated "I'm Going" graphic** for buyers to post on Instagram Stories / Facebook Stories (which don't auto-pull OG images), you'd need a designer to make:
- 1080×1920 vertical (Instagram Story / Facebook Story)
- "I'll Be There · July 3 · Countdown 250"
- Event logo + Washington Hilton silhouette + date
- Space for buyer to add their name/photo

Cost: ~$50-200 on Canva / Fiverr. Not urgent — the OG image works for horizontal posts.

## Referral incentive (optional but powerful)

**Phase 1 (immediate, no overhead):** Add to confirmation email:
"Refer a friend — if they attend the Ball, you'll both receive a complimentary commemorative gift at the event."

**Phase 2 (requires build):** Unique referral links per buyer + dashboard
- Each buyer gets a unique URL: `countdown250.allamericanball.com/ref/[code]`
- Code maps to a unique Eventbrite tracking link
- After 3 successful referrals → upgrade to next tier (Liberty → Patriot VIP)
- After 6 successful referrals → free Statesman's Concierge seat upgrade
- This is the "Ambassador Program" from the ticket sales strategy doc, now data-backed.

Phase 1 is a 10-minute email copy edit. Phase 2 requires site work + admin system — defer to after other priorities.

## Measurement

After 2 weeks of the above live, check Eventbrite tracking links:
- `websitemain` — direct site-driven sales (baseline)
- `socialShare` — shared-link-driven sales (this flow)

If `socialShare` hits 5%+ of total sales, this is a real channel. Double down with Phase 2.
