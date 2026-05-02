# Asset Library

A storage shelf for **content that's not currently on the live site but might be added (or restored) later**. Anything saved here is intentionally NOT in the deploy pipeline (`docs/` is not built into the site).

When in doubt, **save before deleting** — it's cheap to keep around, expensive to recreate.

---

## How it's organized

| Folder | What goes in it |
|---|---|
| **`copy/`** | Plain text or short markdown snippets — taglines, paragraphs, headlines we removed from a page or are considering for a future page |
| **`pages/`** | Whole `.astro` page files that were removed from `src/pages/` (so the route no longer exists). If we ever want the page back, copy it back into `src/pages/` |
| **`sections/`** | Larger `.astro` snippets — entire sections (a hero, a marquee, a CTA block) that we pulled off a page but don't want to lose |
| **`images/`** | Images we removed from `public/images/` or considered for the site but didn't use. Either copy the file here OR add a `.md` note pointing to where the file lives in Downloads/Dropbox/etc. |

---

## Index of saved assets

### Copy
- `copy/home-tickets-section-headline-tagline.md` — *"Ticket sales are deliberately limited to ensure optimal comfort and an exceptional experience for every guest."* — REMOVED from the home page Tickets section 2026-05-02. Restore by pasting back into `src/pages/index.astro` just below the red divider in the "Three Ticket Options" header block.

### Pages
- `pages/schedule.astro` — the full event-evening schedule page (was at `/schedule/`). Removed from the live site 2026-05-02 because the actual evening run-of-show isn't finalized yet. Restore by copying back to `src/pages/schedule.astro` AND re-adding `{ label: "Schedule", href: "/schedule/" }` to the `moreLinks` array in `src/components/Navbar.astro`.

### Sections
- *(none yet)*

### Images
- *(none yet)*

---

## How to restore something

**A page** (e.g. schedule):
1. Copy file back: `cp docs/asset-library/pages/schedule.astro src/pages/schedule.astro`
2. Re-add the nav link in `src/components/Navbar.astro` (under `moreLinks`)
3. Run `python scripts/audit_assets.py` to confirm
4. Commit + push

**A copy snippet:**
1. Open the markdown file in `copy/` to see the exact text
2. Paste back into the relevant page where it belongs
3. Commit + push

**A section:**
1. Open the `.astro` snippet in `sections/`
2. Paste into the page at the correct location
3. Adjust class names / IDs to match destination page
4. Commit + push

---

## How to add something to the library

**Removing a piece of copy from a page?**
1. Save it to a new file in `copy/` with a descriptive filename (e.g. `homepage-trust-band-old-version.md`)
2. Add a one-line entry to the index above
3. Then remove from the page

**Removing a whole page?**
1. Move the `.astro` file: `mv src/pages/somepage.astro docs/asset-library/pages/somepage.astro`
2. Remove any nav links pointing to it
3. Add an entry to the index above with restoration instructions

**Removing a section?**
1. Cut the section block out of the page
2. Save to `sections/page-section-description.astro`
3. Add an entry to the index above
