# The Hosted Tables Program — Program Spec & Recovery Doc

**Last updated:** 2026-04-29
**Purpose:** Single source of truth for the Hosted Tables Program design, operational mechanics, and pending deliverables. Hand this to any future Claude session to restore context.

---

## Strategic context

- **Goal:** Drive Statesman's Concierge Pass sales by giving people a structured, low-friction way to recruit their network into a "Party Inside the Party" at the event.
- **Mechanic:** Hosts get peacocking benefits (named in program/website, public toast, signage). Guests buy their own Statesman's Pass and join the host's table. Mike (the operator) handles all the logistics.
- **Why it works:** Aligns incentives — host gets credit, guest gets a curated experience, Mike gets the sales lift.
- **Cannibalization risk acknowledged:** Some "groups" may just be friends who would have bought anyway. Mitigated by the Featured threshold (6+ for full benefits) — drives genuine recruiting.

---

## Naming conventions (LOCKED)

| Term | Use |
|---|---|
| **The Hosted Tables Program** | The operational name. Page headers, FAQ, navbar links, anywhere clarity matters. |
| **"Party Inside the Party"** | The experience descriptor. Headlines, marketing taglines, social copy. Used inline ("Host your own Party Inside the Party"). |
| **Host** | The role — the person organizing a Hosted Table |
| **Guest** | The role — anyone joining a host's table |
| **Hosted Table** | Any group of 2+, full base benefits |
| **Featured Hosted Table** | Group of 6+ (host + 5 guests), gets toast + signage |
| **Open Affinity Table** | Internal name for the seeded affinity tables (alumni, healthcare, etc.) — these have no named host; visitors see them as regular Hosted Tables in the public roster |

---

## The 2-tier benefits ladder

Decided after Mike pushed back on the original "minimum 6" proposal. Logic: small groups still get marketing-relevant recognition (zero marginal cost to us). Production-cost benefits gate at 6+.

### Hosted Table — any size (2+)
- Reserved private table inside the Statesman's Concierge Area
- **Host named** in the official event program
- **Host named** on the event website
- We handle every detail — host enjoys their party

### Featured Hosted Table — 6+ guests (host + 5)
Everything in Hosted Table, **plus:**
- **Public "Toast to the Hosts"** ceremony at the event
- **Personalized table signage** with host name & group name
- Premium recognition during stage announcements

---

## Production deadlines

| Date | Event |
|---|---|
| **T-60 days** (~early May 2026) | Official event program goes to print. Hosts confirmed by this date are named in the printed program. |
| **T-30 days** | Personalized table signage cuts off (Featured Hosted Tables must finalize details by here). |
| **T-7 days** | Final seating chart locked. |

---

## The 9 seed tables (live roster at launch)

All seeded as **Open Affinity Tables** — no named organizer. The public roster shows them as standard Hosted Tables. Mike handles logistics for all of them.

| Table name | Seed count | Featured? |
|---|---|---|
| JMU Alumni | 12 | ★ Featured |
| Virginia Tech Alumni | 8 | ★ Featured |
| University of Maryland Alumni | 6 | ★ Featured |
| UVA Alumni | 4 | — |
| Georgetown Alumni | 4 | — |
| Healthcare Professionals | 6 | ★ Featured |
| H Tragle 50th Bday | 10 | ★ Featured |
| Lansdowne Crew | 8 | ★ Featured |
| Walter Family Reunion | 8 | ★ Featured |

**Total seeded membership:** 66 across 9 tables. Provides immediate social-proof gravity at launch.

**Display rule (Option A):** Public roster shows the count only. Individual member names appear only as real people sign up via the form (with consent). This avoids any name/count mismatch.

**Live in code at:** `src/data/hosted-groups.ts` (canonical source). Update counts here weekly as real signups roll in (master Sheet → reflect changes here).

---

## The "no wrong way" reassurance — three required messages

Mike emphasized these MUST be conveyed clearly, multiple places, to avoid dissuading buyers:

1. **Buy together = seated together.** Even without joining a formal group, guests who buy at the same time are seated together automatically.
2. **Hosting and joining are completely optional.** A Statesman's Pass works perfectly as a solo ticket.
3. **Don't want to host?** Either join an existing affinity/hosted table OR be seated with other distinguished guests in the Statesman's Concierge Area.

These are unified into **"Three Ways to Enjoy Your Statesman's Pass"** on `/hosted-group-tables`:

| Option | What it is |
|---|---|
| **Option 1: Host your own Hosted Table** | Bring your group, get the spotlight |
| **Option 2: Join an existing Hosted Table** | Sit with your tribe (alumni, professional, family) |
| **Option 3: Sit independently** | Buy solo — seated with other distinguished/honored guests. Buy with friends — seated together automatically, no formal group needed. |

---

## Operational architecture

### Where the program lives
1. **`/hosted-group-tables`** page on countdown250.allamericanball.com — pre-purchase pitch + roster + Create/Join forms (rewritten 2026-04-29)
2. **Eventbrite Statesman thank-you message** — post-purchase explainer that points buyers back to the page

### How it works end-to-end (NO BACKEND, MVP-grade)

```
1. Visitor reads /hosted-group-tables (or links to it from homepage Hosted Tables section)
2. Decides to host OR join OR sit independently
3a. (Host) Buys Statesman's Pass on Eventbrite → returns to page → fills Create form
3b. (Guest) Buys Statesman's Pass on Eventbrite → returns to page → fills Join form (dropdown of existing tables)
3c. (Independent) Just buys Statesman's Pass → no further action needed
4. Eventbrite confirmation email (Statesman tier) explains the program & links back to /hosted-group-tables for anyone who didn't notice the program at purchase time
5. Mike checks the Google Form responses weekly — emails hosts confirmation, updates the public roster (count updates), assigns seating at the event
```

### Why we DON'T use Eventbrite custom questions
Considered, rejected. Reasons:
- Many buyers don't know about the program at purchase time — adding a checkout question they can't answer slows them down
- Eventbrite per-ticket-type custom questions are clunky/limited on Mike's plan
- The Google Form approach works whether someone decides to host BEFORE or AFTER buying

---

## The two Google Forms (Mike still needs to build)

### Form #1 — "Create a Hosted Table" (Host signup)

| # | Field | Required |
|---|---|---|
| 1 | Your name (full) | ✅ |
| 2 | Email | ✅ |
| 3 | Phone | optional |
| 4 | Eventbrite order # *(verifies Statesman's Pass)* | ✅ |
| 5 | Group name *(e.g., "Smith Family Reunion")* | ✅ |
| 6 | Group theme/description *(1 line)* | optional |
| 7 | Expected number of guests | optional |
| 8 | May we list you publicly on the website roster? *(Yes/No)* | ✅ |
| 9 | Anything specific for your stage announcement or table signage? | optional |
| 10 | Anything else we should know? | optional |

### Form #2 — "Join a Hosted Table" (Guest signup)

| # | Field | Required |
|---|---|---|
| 1 | Your name (full) | ✅ |
| 2 | Email | ✅ |
| 3 | Phone | optional |
| 4 | Eventbrite order # *(verifies Statesman's Pass)* | ✅ |
| 5 | Which group are you joining? *(dropdown of all hosted tables + "Other / write-in")* | ✅ |
| 6 | May we list your name publicly in the group's roster? *(Yes/No)* | ✅ |

**Operational note on the dropdown:** Mike updates the dropdown options manually as new tables are created (~30 sec per addition). For 10–50 hosts over the year, this is ≤5 min/week. Free `formRanger` add-on can auto-sync from Sheet later if volume justifies.

### Both forms feed into one master Google Sheet
- "Hosted Tables — Master" sheet
- Columns: Host/Guest name, Email, Phone, Order #, Group, Public-display Y/N, etc.
- Public-facing data (Group + Names with consent + count) is what shows on the website
- Private data (Email, Order #, Phone) only Mike sees

---

## Status of the 5 deliverables

| # | Deliverable | Status | Location |
|---|---|---|---|
| 1 | Full `/hosted-group-tables` page rewrite | ✅ DONE 2026-04-29 | `src/pages/hosted-group-tables.astro` |
| 2 | Eventbrite Statesman thank-you message text | ⏳ Drafted in chat — pending paste into Eventbrite admin (see chat history) |
| 3 | Host confirmation email | ⏳ Pending — Mike to OK schedule, then Claude drafts |
| 4 | Sample host-to-guest invitation email | ⏳ Pending |
| 5 | Both Google Form question sets (paste-ready text) | ⏳ Pending — list above is the spec |

### Mike's TODO before the program goes live
1. **Create the two Google Forms** in Google Forms (use the field specs above)
2. **Replace the placeholder URLs** in `src/pages/hosted-group-tables.astro`:
   ```js
   const CREATE_FORM_URL = "mailto:CountdownAmerica250@gmail.com?subject=...";  // ← replace
   const JOIN_FORM_URL   = "mailto:CountdownAmerica250@gmail.com?subject=...";  // ← replace
   ```
   Until replaced, both buttons fall back to a prefilled `mailto:` so visitors can still reach Mike.
3. **Edit the Eventbrite Statesman tier** "additional info / thank you" field to include the program description (text drafted in chat history; will be re-delivered as a formal copy doc soon).
4. **Build out the public-display Sheet view** (filter master sheet to show only public columns).

---

## Visual / design conventions established for this program

- **Section bg:** navy (`bg-navy`, `#002868`) — primary brand blue, the official "Old Glory Blue" / America 250 color
- **Feature accent:** gold (`text-gold`, `bg-gold`)
- **Body text on navy:** white/85 or white/90
- **Bold value-words on navy:** gold (instead of navy)
- **Headlines on navy:** gold or white
- **CTAs:** gold gradient (`bg-gradient-to-b from-gold to-[#B8954A]`) with navy-dark text — same pattern as the Statesman ticket card's "Host your Own" CTA
- **Cream cards on navy** for content panels (high contrast, easy to read)
- **Header bar over benefits cards:** solid gold bg + navy-dark text (gold-ribbon look)

---

## Decisions made and rejected (for completeness)

| Topic | Considered | Decision |
|---|---|---|
| Program name | "Hosted Tables Program" / "Party Inside the Party" / "PIP (Party Inside the Party)" | Use **both**: "Hosted Tables" operationally, "Party Inside the Party" experientially. Drop "PIP." |
| Minimum group size | 6 mandatory cliff vs no minimum | **No minimum.** 2-tier ladder: any size = Hosted Table; 6+ = Featured. Avoids "I might not qualify, so I won't try" friction. |
| Anchor / seed tables | None vs a few real-host vs many seeded affinity | **9 seeded affinity tables**, no named organizer (all "Open"). Mike handles logistics for all of them. |
| Public group display | Hide all info / show counts only / show counts + names | **Counts visible from launch.** Names visible only when real signups occur (consent gated). |
| Guest→host association | Eventbrite custom question / Google Form on the page / mailto: | **Google Form on the page.** Eventbrite limitations + risk of confusing buyers killed option 1. |
| AI Fanatics seed table | Include / exclude | Excluded — lower obvious affinity for this event's positioning. |

---

## Audit guardrails (for any future Claude session)

Run before every push:
```
python scripts/audit_assets.py
```

Six checks: (1) image existence, (2) internal route resolution, (3) in-page anchor resolution, (4) duplicate IDs, (5) carousel dot/slide match, (6) **dead/missing named imports** *(added 2026-04-29 after a deploy break caused by a renamed export)*.

All 6 must pass before push. Both `hostedTables` array updates and any export renames are covered by Check #6.
