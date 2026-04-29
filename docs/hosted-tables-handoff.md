# Hosted Tables Program — Manager Handoff

**For:** Whoever takes over day-to-day management of the Hosted Tables Program from Mike Harrigan.
**Last updated:** 2026-04-29

> Read this first. For deeper detail, see `docs/hosted-tables-program.md` (full spec) and `docs/website-design-conventions.md` (visual / design language).

---

## 1. What the program is

A **named-group dining experience** for **Statesman's Concierge Pass** holders at the Countdown 250 Ball (Washington Hilton, July 3, 2026).

Statesman's Pass holders can either **host** a group ("Hosted Table") or **join** an existing one. Each table is a "Party Inside the Party" inside the Statesman's Concierge Area. We do all the logistics. The host gets public recognition.

Two tiers:

| Tier | Threshold | Benefits |
|---|---|---|
| **Hosted Table** | Any size (2+) | Reserved table together · Host named in event program · Host named on website |
| **Featured Hosted Table** | 6+ guests | Above + Public "Toast to the Hosts" + Personalized table signage |

There is **no extra cost** to host or to join — every member just buys their own Statesman's Pass.

---

## 2. Program goals

**Primary:** Drive Statesman's Pass sales by giving people a structured way to recruit their network. Each host is essentially a recruiting agent.

**Secondary:**
- **Web traffic / SEO** — every host shares the `/hosted-group-tables` URL with their guests, driving organic visits to our site
- **Social proof** — public roster shows the program is alive and growing; helps fence-sitters convert
- **Affinity targeting** — anchor tables (alumni, professional groups, family reunions) attract buyers who don't know anyone but want to join their tribe

---

## 3. Critical success factors

### A. The "don't dissuade" rule (most important)

Mike was clear: the program must NEVER feel like pressure. Three messages must always come through:

1. **Buying tickets together = seated together automatically.** No formal group needed.
2. **Hosting and joining are completely optional.** A solo Statesman's Pass works perfectly.
3. **Don't want to host?** Either join an affinity table OR be seated with other distinguished guests in the Statesman's Concierge Area.

The page handles this with a "Three Ways to Enjoy Your Statesman's Pass" triptych. **Do not let copy edits accidentally erode this messaging.** Future ad campaigns, emails, and FAQ revisions should always reinforce these three points.

### B. Common pitfalls to actively avoid

| Pitfall | Symptom | Mitigation |
|---|---|---|
| "I have to bring a big group" | People hesitant to host | Lead with "any size 2+ qualifies." 6+ is the *bonus* tier, not the entry. |
| "There's an extra charge" | Buyers question the value | "No cost to you or your guests" is on the homepage CTA, the page, the FAQ. Don't bury it. |
| "I have to commit before knowing my guest count" | Hosts won't even start | Form takes 30 seconds. No financial commitment. Drop out anytime. |
| "I'm alone, I can't go to this event" | Solo buyers feel awkward | Option 3 in the Three Ways triptych must always read first-class, not consolation prize. |
| Slowing down checkout with group questions | Cart abandonment | We deliberately do NOT use Eventbrite custom questions. People learn about the program post-purchase. |

### C. Other success factors

- **Speed of host onboarding.** The form must stay short and approval should be same-day where possible. Friction here = dropouts.
- **Honesty on the public roster.** Counts shown are the truth (seeds + real signups). Never inflate visible names beyond what was actually submitted with consent.
- **Communication to hosts.** A host who fills the form and hears nothing for a week loses momentum. Confirmation should go out within 24 hours.
- **Deadline visibility.** T-60 / T-30 / T-7 dates are on the page. They drive urgency. Don't soften them.

---

## 4. What's already done

| Item | Where |
|---|---|
| `/hosted-group-tables` page rewrite (full design + copy) | `src/pages/hosted-group-tables.astro` |
| Live roster of 9 seed tables (66 seeded members total) | `src/data/hosted-groups.ts` |
| Homepage Hosted Tables section with gold-on-navy treatment | `src/pages/index.astro` |
| Statesman ticket card with "Host your Own Party Inside the Party" gold CTA | `src/pages/index.astro` |
| Audit script with 6 guardrails (image existence, routes, anchors, IDs, carousels, dead imports) | `scripts/audit_assets.py` |
| Production deadline framing (T-60 / T-30 / T-7) | Embedded in page copy |
| "Three Ways to Enjoy Your Statesman's Pass" reassurance section | Embedded in page |
| FAQ block on the page (6 questions, including the don't-dissuade ones) | Embedded in page |

---

## 5. What's left to do before launch

| # | Item | Owner | Notes |
|---|---|---|---|
| 1 | **Create two Google Forms** (Create-Hosted-Table + Join-Hosted-Table) | Manager | Field specs in `docs/hosted-tables-program.md` §"The two Google Forms" |
| 2 | **Replace placeholder URLs** in `src/pages/hosted-group-tables.astro` with real Form URLs | Manager | Constants `CREATE_FORM_URL` and `JOIN_FORM_URL` at top of file. Both currently fall back to `mailto:CountdownAmerica250@gmail.com`. |
| 3 | **Edit Eventbrite Statesman tier "additional info / thank you"** to include program description | Manager | Draft text exists in chat history; available on request |
| 4 | **Build "Hosted Tables Master" Sheet** (the Form-receiving spreadsheet) with two views: (a) full-data, Mike-only and (b) public-display-only filter | Manager | All Form responses → master Sheet → public columns surface to roster |
| 5 | **Draft host confirmation email** + sample host-to-guest invitation email | Pending | Templates pending — Claude can draft on request |
| 6 | **Update the Join Form's group dropdown** to mirror the live roster (initial: 9 seed tables; add real groups as they're created) | Manager | ~30 sec per addition. Optional: install free `formRanger` Google Forms add-on for auto-sync from Sheet |

---

## 6. Ongoing operations (regular cadence)

| Cadence | Task |
|---|---|
| **Daily (5 min)** | Check Eventbrite for new Statesman's Pass purchases. Watch for incoming Forms. Reply to host inquiries within 24 hours. |
| **Weekly (15 min)** | Sync Form submissions → public roster. Update `src/data/hosted-groups.ts` counts (or names if any new ones consented to public listing). Push the change. New table created? Add it to the Join Form dropdown. |
| **Weekly (10 min)** | Brief check-in with each host whose group is filling — quick "you've got X confirmed, Y to reach Featured" email. Keeps momentum. |
| **Monthly** | Brainstorm 1–2 new affinity table themes that could attract buyers (e.g., professional networks, civic associations). Add them as seeded tables if they fit. |
| **Monthly** | Review FAQ + page copy against actual buyer questions received. If 3+ people ask the same thing, add it to the FAQ. |
| **Monthly** | Sales-channel brainstorm: which host or affinity table can be amplified via partner outreach, social, email blast, etc.? |
| **At deadlines (T-60 / T-30 / T-7)** | Hard cutoffs for program-print, signage, seating. Email all uncommitted hosts a week before each deadline. |

---

## 7. The technical touchpoints

| Asset | Path | Who edits |
|---|---|---|
| Live roster data | `src/data/hosted-groups.ts` | Manager (weekly) |
| Page copy | `src/pages/hosted-group-tables.astro` | Manager (when copy changes are needed) |
| Homepage Hosted Tables section | `src/pages/index.astro` *(search "hosted-tables" for section start)* | Manager (rare) |
| Pre-deploy audit | `scripts/audit_assets.py` — run with `python scripts/audit_assets.py` | Manager (every push) |
| Deployment | GitHub Actions auto-deploys on push to `main`. ~60–90 sec to live. | Automatic |
| Repo URL | https://github.com/mikey-harrigan/countdown250 | — |

**Standing rules:**
- Run `python scripts/audit_assets.py` before every push. All 6 guardrails must pass.
- Never strip `class="eventbrite-checkout"` or `?aff=websitemain` query param from any ticket-purchase link — they're required for the checkout integration and affiliate tracking.
- Never expose private Form data (emails, order #s, phone) on the public roster.
- The `/statesmans-pass` page exists at the URL but is currently unlinked from the homepage — preserved for future per-tier detail pages.

---

## 8. Where to dig deeper

- **`docs/hosted-tables-program.md`** — Full program spec. Every decision and the reasoning behind it. The 9 seed tables. Both Google Form specs. Mike's full TODO list.
- **`docs/website-design-conventions.md`** — Color terminology (Mike's specific usage of "navy blue" / "white" / etc.), section bg map, recurring patterns, what's been removed and shouldn't come back.
- **`C:\Users\USER\claude-backups\2026-04-29\`** — Mirror of the docs above, plus a session-summary recapping the design session that produced this program.

---

## TL;DR for a busy manager

1. **Read the page at `/hosted-group-tables`.** That tells you what the program is and how it's marketed.
2. **Build the two Google Forms** and replace the two URLs in `src/pages/hosted-group-tables.astro`. That's the main launch blocker.
3. **Watch the Forms inbox + Eventbrite.** Update the roster weekly.
4. **Protect the don't-dissuade messaging** in any future copy edits.
5. **When in doubt, run the audit** before pushing.
