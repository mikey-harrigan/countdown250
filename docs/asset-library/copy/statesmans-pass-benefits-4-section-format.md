# Statesman's Pass — original 4-section benefits format

**Removed from `src/pages/index.astro` Statesman's Pass card on 2026-05-05** to make room for a flatter single-list version.

Mike wants this preserved for a future **Tickets sub-page** where the deeper structure makes more sense (more vertical real estate, more room to breathe).

## Heading

**The Pinnacle Experience at the VIP Reception and the Ball (6:30 PM – 1 AM)**

Sub-heading (2-line stack):
- Everything in the Patriot VIP Ticket
- Plus These Elite Upgrades:

## Sections

### Private Service – All Night
- Personal ambassador/concierge
- Top-shelf open bars & premium cuisine

### Exclusive Access to:
- Reserved VIP seating with special guests
- 3 additional hospitality/entertainment areas
- Backstage areas and historic spaces reserved for POTUS & dignitaries

### Personal Recognition:
- Stage announcements & name in event program

### Gifts & Keepsakes:
- Limited-edition gift, Statesman's Pass lanyard, Official Program

---

## How to restore (for the Tickets sub-page)

Drop this back into the JS data array on the future tickets page using the same `sections: [{ heading, items }]` shape that `src/pages/index.astro` uses today:

```js
description: "The Pinnacle Experience at the VIP Reception and the Ball (6:30 PM – 1 AM)",
sectionIntro: "<span class='block'>Everything in the Patriot VIP Ticket</span><span class='block mt-1'>Plus These Elite Upgrades:</span>",
sections: [
  {
    heading: "Private Service – All Night",
    items: [
      "Personal ambassador/concierge",
      "Top-shelf open bars & premium cuisine",
    ],
  },
  {
    heading: "Exclusive Access to:",
    items: [
      "Reserved VIP seating with special guests",
      "3 additional hospitality/entertainment areas",
      "Backstage areas and historic spaces reserved for POTUS & dignitaries",
    ],
  },
  {
    heading: "Personal Recognition:",
    items: [
      "Stage announcements & name in event program",
    ],
  },
  {
    heading: "Gifts & Keepsakes:",
    items: [
      "Limited-edition gift, Statesman's Pass lanyard, Official Program",
    ],
  },
],
```
