# Hosted Group Tables — Program Manager Guide

**Event:** The Official Countdown 250 Ball
**Date:** July 3, 2026
**Venue:** Washington Hilton, 1919 Connecticut Ave NW, Washington, D.C.
**Program owner:** Mike Harrigan
**Website:** countdown250.allamericanball.com

---

## 1. Program name and purpose

**Hosted Group Tables** is a new benefit exclusive to the **Statesman Pass** (the $1,700 premium tier) for the Countdown 250 Ball.

The program lets any Statesman Pass guest create or join a **named group of any size** — university alumni network, neighborhood circle, industry crew, a group of friends — and be seated together in the premium Statesman area alongside special guests and All-American Hero Awardees.

**Strategic purpose:** to drive Statesman Pass sales by turning network connectors into volunteer organizers. One organizer recruiting 10 friends = 10 Statesman Pass sales. Fifty organizers = 500 Statesman sales = ~$850,000 in premium revenue. The program gives organizers a compelling, prestige-based reason to do the work of rallying their people.

**Key principle:** No discounts. No held pricing. No financial incentives. The program succeeds on recognition and peer status, not discounts.

---

## 2. How the program works for buyers

1. A buyer purchases a Statesman Pass on Eventbrite.
2. At checkout, a required question asks: *"Are you joining an existing Hosted Group, interested in starting a new one, or not part of a specific Hosted Group?"*
3. Depending on their answer:
   - **Joining existing** → dropdown of current official Hosted Groups. They select one.
   - **Starting new** → text field for the group name they're proposing, and a yes/no on whether they are the main organizer/contact.
   - **Not part of a group** → nothing more captured.
4. Purchase completes immediately. No waiting for approval.
5. The Program Manager reviews new-group proposals after purchase. Approved groups are added to the website and the Eventbrite dropdown for future buyers.
6. Website is the **official public list** of Hosted Groups: countdown250.allamericanball.com/hosted-group-tables

---

## 3. Group size and seating rules

- **Any size is welcome.** A group of 2 still participates and will be seated together.
- **Groups under 10 paid Statesman members** may be placed at a shared table with another compatible group.
- **Groups of 10 or more paid Statesman members** trigger two things:
  - Their group gets its own table or adjacent tables in the Statesman area.
  - Custom table signage is prepared (8.5 × 11 card in a table-top holder, text-only at launch).
  - The organizer becomes a **Founding Host** with the full recognition package (see Section 5).
- **Signage cutoff: June 20, 2026.** After that date, group membership is locked for signage and program printing. Ticket sales continue, but late additions to a group won't affect signage, the program, or Founding Host eligibility.

---

## 4. Member benefits (any Hosted Group member)

Every member of a Hosted Group, regardless of group size, gets:
- Seated with their group in the premium Statesman area
- Opportunities to mingle with special guests and Hero Awardees throughout the evening
- Everything that comes standard with their Statesman Pass (reserved Presidential Stage seating, private entrance, dedicated Ambassador/concierge, premium dining, etc.)

---

## 5. Founding Host benefits (organizer, at 10+ paid group members)

When a group reaches 10 or more paid Statesman guests by the June 20 cutoff, the organizer earns Founding Host status and receives:

1. **Table signage credit** — the physical 8.5×11 card on their group's table reads "[Group Name] — Hosted by [Their Name]."
2. **Dedicated Founding Hosts section** in the official event program, distinct from the general Statesman roster.
3. **Named stage callout** during the evening's announcements — specifically as Founding Host of their group.
4. **Public listing** on the Hosted Group Tables page of the website as Founding Host.
5. **Founding Host commemorative pin** — limited-edition keepsake of the role.
6. **Toast to the Hosts** — a signature moment during the evening where all Founding Hosts are called to stand (or invited onstage) for a public toast in front of the full ballroom.

**Cost of the benefits package:** negligible (~$25-50/pin × 50 Hosts = $1,250-$2,500 total). The value to the organizer is social capital, not savings.

---

## 6. Founding Host responsibilities

Becoming a Founding Host is earned, not granted. Responsibilities:
- Personally rally 10 or more people to purchase Statesman Passes and join their named group
- Communicate the exact official group name to their recruits (so each buyer selects the correct name from the Eventbrite dropdown)
- Respond to the Program Manager's confirmation requests leading up to the event
- If they cannot attend, the Founding Host designation does not transfer; someone else in the group can be proposed as the new Host if they had a significant recruitment role

---

## 7. Key dates and deadlines

| Date | What happens |
|---|---|
| Ongoing | Buyers purchase Statesman Pass and select or propose Hosted Group at checkout |
| Weekly | Program Manager reviews new proposals, approves and adds to website + Eventbrite |
| **June 20, 2026** | Signage cutoff. Group membership locked for signage printing and Founding Host eligibility |
| June 20-25 | Signage printed, pins confirmed, program sent to printer |
| June 25-July 2 | Final seating coordination with venue |
| July 3, 2026 | Event day. Toast to the Hosts happens during the evening |
| July 5-10 | Post-event thank-you and feedback |

---

## 8. Program Manager responsibilities — by phase

### A. Ongoing (from now until June 20)

**Weekly (~30 minutes per week at launch, scaling with volume):**
- Export new Eventbrite orders; filter for Statesman Pass purchases
- Identify buyers who selected "joining an existing group" — verify they chose a valid name matching the website list. If they typed something close but not matching (e.g., "JMU Alums" instead of "JMU Alumni"), contact them to confirm intent.
- Identify buyers who selected "starting a new group" — evaluate their proposed name:
  - Is it clear? Not vulgar? Not duplicating an existing group?
  - If yes: approve, add to website data file (`src/data/hosted-groups.ts`) and to Eventbrite dropdown. Email the proposer to confirm.
  - If duplicate/near-duplicate of an existing group: merge, contact both buyers, standardize on one name.
  - If unclear: contact proposer to clarify before adding.
- Maintain an internal tracking spreadsheet: each Statesman buyer, their group, their order number, Founding Host yes/no status, any special notes.
- Watch for groups approaching 10 paid members — these are your future Founding Hosts. Reach out to the organizer proactively to celebrate progress and encourage final recruitment.

**Anytime a group list changes:**
- **Website and Eventbrite must stay perfectly synchronized.** Any group name on one must exist on the other.
- To update the website: edit `src/data/hosted-groups.ts` in the GitHub repo (or request the change from whoever manages code commits). The change deploys automatically within ~2 minutes.
- To update Eventbrite: edit the Hosted Group dropdown in the event checkout question.

**Communication:**
- Respond to buyer questions within 24-48 hours (via CountdownAmerica250@gmail.com or designated contact)
- Respond to organizers with progress reports on their group counts when asked

### B. 4-8 weeks before event (late May – early June)

- Begin compiling a provisional Founding Hosts list — every group on track to reach 10 members
- Source and price the Founding Host commemorative pins. Allow lead time for custom engraving if applicable. Order a slight surplus (10-15% extra) to cover last-minute qualifiers.
- Draft the Founding Hosts section for the official event program — send to Mike for approval
- Provide the print-program designer with the Founding Hosts list (names + group names)
- Begin weekly check-ins with each active Hosted Group's organizer

### C. 2 weeks before event (mid-to-late June)

- **June 20 signage cutoff**: freeze group membership lists. Any Statesman Pass bought after June 20 can still select any group from the dropdown, but will NOT count toward Founding Host status or affect signage.
- Finalize the Founding Hosts list
- Produce custom table signage (one card per 10+ group): "[Group Name] — Hosted by [Organizer Name]." Signage is 8.5 × 11, text-only at launch.
- Confirm pins are received and counted
- Finalize the official program's Founding Hosts section; program goes to printer
- Update the website's Founding Hosts public listing (will likely live on /hosted-group-tables page)
- Work with the venue's event coordinator on the Statesman area seating plan:
  - Ensure every Hosted Group is seated together
  - Groups with 10+ members get their own table or adjacent tables
  - Place Founding Host at a prominent seat in their group's seating
- Prepare usher/check-in briefing document listing each Founding Host and their group

### D. 1 week before event

- Coordinate with **stage manager** on the Toast to the Hosts execution:
  - **When** in the evening does it happen? Recommended: during dinner or just before the midnight countdown for maximum drama.
  - **Who announces it** — Mike? the MC? a special guest?
  - **What's said** — write the exact words. Founding Host names should be read aloud or displayed on screen. Confirm pronunciation of each name with the organizer in advance.
  - **How are Hosts identified** — asked to stand at their table, invited onstage, or both?
  - **What's the visual** — spotlight? raised glass? photo moment?
- Coordinate with **program printer** to confirm Founding Hosts section is correct and printed on time
- Prepare a printed roster for the stage manager: every Founding Host's name + phonetic spelling + group name
- Send a pre-event email to all Founding Hosts:
  - Confirm their status and benefits
  - Preview the Toast to the Hosts ceremony so they know to expect it
  - Confirm their group's table location
  - Thank them for their recruitment work

### E. Day of event

- Arrive early. Coordinate with the setup team on table signage placement in the Statesman area.
- Brief the check-in team: when a Founding Host arrives, they receive their commemorative pin immediately and are directed to their group's table.
- Brief ushers: Hosted Group members may ask where their group is seated. Ushers should have the seating chart.
- Check in with the stage manager throughout the evening to confirm Toast to the Hosts timing and execution
- Oversee the Toast to the Hosts moment: make sure every Founding Host is in the room when it happens, on their feet, and visible
- Be available for last-minute Hosted Group questions from buyers

### F. Post-event (within 2 weeks)

- Send personalized thank-you notes to every Founding Host
- Gather feedback (brief survey or call): what worked, what didn't, would they do it again for Year 2, any names to refer for future programs
- Collect photos from the evening showing Hosted Groups and the Toast to the Hosts ceremony — useful for next year's marketing
- Document lessons learned and process improvements in a wrap-up doc
- Work with Mike to determine if any Founding Hosts should be cultivated for sponsorship, ambassadorship, or future-event roles

---

## 9. Resources and system access

| Resource | Location | Access needed |
|---|---|---|
| Public program page | countdown250.allamericanball.com/hosted-group-tables | Public |
| Statesman Pass page | countdown250.allamericanball.com/statesmans-pass | Public |
| Official group list (website source of truth) | GitHub: `src/data/hosted-groups.ts` | Repo write access via Threshold Media |
| Eventbrite event | eventbrite.com — The Official Countdown 250 Ball - Washington DC | Admin access via CountdownAmerica250@gmail.com |
| Eventbrite orders export | Eventbrite → Manage event → Orders → Export | Admin access |
| Eventbrite Hosted Group checkout question | Eventbrite → Manage event → Order Options → Order Form | Admin access |
| Event ID | `1982528927390` | — |
| Master program doc | `/marketing/Hosted_Group_Tables_Addendum.docx` | Local files |

---

## 10. Coordination contacts (fill in with actual names when known)

- **Event owner:** Mike Harrigan — 703-930-0400 — mike@headstrong1.com
- **Marketing/website lead:** Anna Rice — arice@thresholdmedia.com (Threshold Media)
- **Website code:** Alex Plisov — aplisov@thresholdmedia.com — GitHub user `thresholdmedia`
- **Meta Pixel / Ad tracking:** Brenda Stromberg — bstromberg@thresholdmedia.com
- **Stage manager:** TBD
- **Event coordinator (Washington Hilton):** TBD
- **Program printer:** TBD
- **Table signage printer:** TBD
- **Pin/commemorative supplier:** TBD
- **Seating coordinator:** TBD

---

## 11. Critical rules and policies (do not violate)

- **Statesman Pass required.** Hosted Group Tables is not available to Liberty or Patriot VIP tier buyers. Do not make exceptions.
- **No discounts.** Standard Statesman rates apply to every member of every group. No group rate, no early-bird locked price, no comp tickets to organizers. The program's credibility depends on this.
- **Website and Eventbrite must match exactly.** A buyer typing "UVA Alumni" must see that exact name in both places. Mismatches cause matching failures.
- **Founding Host status is earned, not granted.** Do not pre-award the status. A group must reach 10 paid members by June 20 to qualify. An organizer who falls short gets sincere thanks and the standard Hosted Group benefits, but not Founding Host recognition.
- **Review decisions stay with the Program Manager.** New group proposals, merges, name standardization, and Founding Host confirmations are the Program Manager's call, in consultation with Mike when needed. Don't let buyers dictate.
- **Never slow down ticket buying to gate group approvals.** Purchase happens first, review happens after.

---

## 12. Common situations and how to handle them

**Two buyers propose near-duplicate names (e.g., "JMU Alumni" and "JMU Alums")**
→ Contact both. Standardize on one official name. Update both orders to the standard. Add only the standard name to the dropdown.

**A Founding Host cannot attend at the last minute**
→ The Founding Host designation does not transfer automatically. If the group identifies a credible co-organizer who contributed substantially to recruitment, they may be recognized as Founding Host in absentia. Consult Mike on edge cases.

**Group size drops below 10 after the June 20 cutoff due to cancellation**
→ Founding Host status is retained. Signage and program are already printed. Group members already placed. No change.

**Buyer insists they want to join a group they typed that doesn't exist on the website**
→ Contact them. Offer options: join an existing similar group, or propose a new one (which will be reviewed).

**A Hosted Group becomes politically controversial or a PR risk**
→ Escalate to Mike immediately. Program Manager has authority to decline or rename in consultation with Mike.

**An organizer asks for a discount or comp ticket**
→ Firmly and warmly decline. The program is recognition-based by design. Explain the Founding Host benefits package as the reward for their work.

**A buyer asks whether the Program Manager can tell them exactly who else is in their group**
→ At launch, no member rosters are shared. Privacy practice. The organizer may separately choose to share their recruitment list. Future phases may include an opt-in roster sheet; not at launch.

---

## 13. Success metrics

- Total number of active Hosted Groups
- Total Statesman Pass sales attributable to Hosted Groups (trackable via Eventbrite's "Select your Hosted Group" question)
- Number of Founding Hosts (groups reaching 10+)
- Average group size across all groups
- Percentage of Statesman Pass buyers who are in a Hosted Group vs. attending solo
- Qualitative: organizer satisfaction, Toast to the Hosts reception, post-event NPS

**Rough targets for Year 1 (discussed with Mike):**
- 25-50 active Hosted Groups
- 10-20 groups reaching Founding Host status (10+ members)
- 300-500 Statesman Pass sales driven through the program
- >80% organizer satisfaction post-event

---

## Questions for Mike

For the new Program Manager to review with Mike at handoff:
1. Who is the stage manager, and when should the Toast to the Hosts happen in the program?
2. Who is the program printer, and what's the deadline for the Founding Hosts section?
3. Who is sourcing and paying for the commemorative pins?
4. Are there special guests, celebrities, or dignitaries whose presence should be coordinated with the Founding Host recognition moment?
5. Is there a budget ceiling for operational expenses (pins, signage, printing)?
6. Who has final approval authority on ambiguous new-group proposals?
7. Are there any specific groups Mike wants personally cultivated (e.g., for existing relationships)?
