"""Guardrail audit:
  1. Every <img src="/...">, <source srcset="/...">, ogImage="..." resolves to an existing file under public/.
  2. Every internal <a href="/..."> (relative) maps to a known route.
  3. Every <a href="#..."> in-page anchor matches an id="..." on the same page.
  4. No duplicate id attributes within a single .astro file.
  5. Each .carousel block's .carousel-dot count matches its .carousel-slide count.
  6. Every named import from a local file resolves to an actual export of that file.

Prints PASS / FAIL per check. Exit 1 if any failure.
"""
import re
import sys
from pathlib import Path
from collections import Counter

ROOT   = Path(r"C:/Users/USER/countdown250")
PAGES  = ROOT / "src" / "pages"
COMPS  = ROOT / "src" / "components"
PUBLIC = ROOT / "public"

# Source files to scan
ASTRO_FILES = list(PAGES.rglob("*.astro")) + list(COMPS.rglob("*.astro"))

failures = []


# ---------- 1. Image existence ----------
img_src_re   = re.compile(r'(?:src|srcset|ogImage)\s*=\s*"(/images/[^"]+?)"')
print("\n=== [1] Image-existence audit ===")
missing_images = set()
for f in ASTRO_FILES:
    txt = f.read_text(encoding="utf-8", errors="ignore")
    for m in img_src_re.finditer(txt):
        ref = m.group(1)
        # ignore querystrings/fragments
        ref = ref.split("?")[0].split("#")[0]
        path = PUBLIC / ref.lstrip("/")
        if not path.exists():
            missing_images.add((f.name, ref))
if missing_images:
    failures.append(f"{len(missing_images)} missing image refs")
    for src, ref in sorted(missing_images):
        print(f"  MISSING  {src}: {ref}")
else:
    print("  PASS — every /images/... ref resolves")


# ---------- 2. Internal route audit ----------
# Known routes = .astro files in src/pages (minus dynamic [..] etc.)
known_routes = set(["/"])
for f in PAGES.rglob("*.astro"):
    rel = f.relative_to(PAGES).with_suffix("")
    parts = rel.parts
    if parts == ("index",):
        known_routes.add("/")
    else:
        path = "/" + "/".join(parts).replace("\\", "/")
        if path.endswith("/index"):
            path = path[:-len("/index")]
        known_routes.add(path)
        known_routes.add(path + "/")

href_re = re.compile(r'href\s*=\s*"(/[^"#?]+?)(?:[?#][^"]*)?"')
print("\n=== [2] Internal route audit ===")
unknown_routes = set()
for f in ASTRO_FILES:
    txt = f.read_text(encoding="utf-8", errors="ignore")
    for m in href_re.finditer(txt):
        href = m.group(1)
        # ignore static-asset hrefs
        if href.startswith(("/images/", "/fonts/", "/favicon", "/robots", "/sitemap", "/.well-known/")):
            continue
        # normalize trailing slash
        if href not in known_routes and (href + "/") not in known_routes and href.rstrip("/") not in known_routes:
            unknown_routes.add((f.name, href))
if unknown_routes:
    failures.append(f"{len(unknown_routes)} hrefs to unknown routes")
    for src, href in sorted(unknown_routes):
        print(f"  UNKNOWN  {src}: {href}")
else:
    print(f"  PASS — every internal href maps to one of {len(known_routes)} known routes")


# ---------- 3. In-page anchor audit ----------
# Only check pages — components may have anchors that resolve in their parent.
print("\n=== [3] In-page anchor (#fragment) audit (pages only) ===")
anchor_re = re.compile(r'href\s*=\s*"#([A-Za-z][\w\-]*)"')
id_re     = re.compile(r'\bid\s*=\s*"([A-Za-z][\w\-]*)"')
import_re = re.compile(r"import\s+(\w+)\s+from\s+['\"](\.\.?/[^'\"]+)['\"]")

# Build a map: page path -> set of ids visible on that rendered page
# (the page's own ids plus those of any directly imported component)
def collect_ids_for_page(page_file):
    ids = set()
    txt = page_file.read_text(encoding="utf-8", errors="ignore")
    ids.update(id_re.findall(txt))
    for m in import_re.finditer(txt):
        rel = m.group(2)
        comp_path = (page_file.parent / rel).resolve()
        if comp_path.suffix != ".astro":
            comp_path = comp_path.with_suffix(".astro")
        if comp_path.exists():
            ids.update(id_re.findall(comp_path.read_text(encoding="utf-8", errors="ignore")))
    return ids

broken_anchors = set()
for f in PAGES.rglob("*.astro"):
    txt = f.read_text(encoding="utf-8", errors="ignore")
    visible_ids = collect_ids_for_page(f)
    for m in anchor_re.finditer(txt):
        frag = m.group(1)
        if frag not in visible_ids:
            # check imported components' anchors too
            broken_anchors.add((f.name, "#" + frag))
if broken_anchors:
    failures.append(f"{len(broken_anchors)} broken in-page anchors")
    for src, frag in sorted(broken_anchors):
        print(f"  BROKEN   {src}: {frag}")
else:
    print("  PASS — every #fragment href on each page resolves (incl. imported components)")


# ---------- 4. Duplicate id audit ----------
print("\n=== [4] Duplicate id audit (per file) ===")
dup_ids = []
for f in ASTRO_FILES:
    txt = f.read_text(encoding="utf-8", errors="ignore")
    counts = Counter(id_re.findall(txt))
    for ident, n in counts.items():
        if n > 1:
            dup_ids.append((f.name, ident, n))
if dup_ids:
    failures.append(f"{len(dup_ids)} duplicate ids")
    for src, ident, n in dup_ids:
        print(f"  DUP      {src}: id=\"{ident}\" appears {n}x")
else:
    print("  PASS — no duplicate ids in any file")


# ---------- 5. Carousel dots = slides ----------
# Bound each carousel by finding the opening div and counting only what's
# inside the matching .carousel-dots block plus all preceding .carousel-slide
# siblings within that container.
print("\n=== [5] Carousel dot-count vs slide-count ===")
slide_re = re.compile(r'<div\s+class="carousel-slide(?:\s|")')
dot_re   = re.compile(r'<button[^>]*class="carousel-dot(?:\s|")')
carousel_open_re = re.compile(r'<div\s+class="([\w-]+-carousel)[^"]*"')

html_comment_re = re.compile(r'<!--.*?-->', re.DOTALL)
mismatches = []
for f in ASTRO_FILES:
    raw = f.read_text(encoding="utf-8", errors="ignore")
    # Strip HTML comments so example markup inside docs doesn't get counted
    txt = html_comment_re.sub("", raw)
    # Find each carousel container by name; for each, slice from the open
    # tag to the next </div> that follows a carousel-dots block.
    for m in carousel_open_re.finditer(txt):
        name = m.group(1)
        start = m.start()
        # Find the carousel-dots opening within ~12000 chars
        dots_open = txt.find('class="carousel-dots', start, start + 15000)
        if dots_open == -1:
            continue
        # End of dots block = next "</div>" after dots_open
        dots_end = txt.find("</div>", dots_open)
        if dots_end == -1:
            continue
        block = txt[start:dots_end + 6]
        slides = len(slide_re.findall(block))
        dots = len(dot_re.findall(block))
        if slides != dots:
            mismatches.append((f.name, name, slides, dots))
        else:
            print(f"  {f.name} .{name}: {slides} slides, {dots} dots — match")
if mismatches:
    failures.append(f"{len(mismatches)} carousel dot/slide mismatches")
    for src, name, s, d in mismatches:
        print(f"  MISMATCH {src} .{name}: {s} slides, {d} dots")


# ---------- 6. Dead-import audit (catches the kind of break that took down
#                the GitHub Pages build on 2026-04-29 — renamed an export in a
#                data file, missed an importer in a legacy component) ----------
print("\n=== [6] Dead-import audit (named imports from local files) ===")

SRC_DIR = ROOT / "src"
TS_LIKE = (".ts", ".tsx", ".astro", ".js", ".jsx")

# Files we audit imports IN
IMPORT_FILES = (
    list(SRC_DIR.rglob("*.astro"))
    + list(SRC_DIR.rglob("*.ts"))
    + list(SRC_DIR.rglob("*.tsx"))
)

# Match named-import statements:
#   import { X, Y as Z } from '...'
#   import type { X } from '...'
#   import Default, { X, Y } from '...'  (we only check the {} part here)
named_import_re = re.compile(
    r"import\s+(?:type\s+)?(?:[A-Za-z_$][\w$]*\s*,\s*)?\{([^}]+)\}\s*from\s*['\"]([^'\"]+)['\"]",
    re.DOTALL,
)

# Match exported names from a source file (covers the common patterns).
export_named_re = re.compile(
    r"export\s+(?:default\s+)?(?:async\s+)?(?:const|let|var|function|class|interface|type|enum)\s+([A-Za-z_$][\w$]*)"
)
# Re-export style: export { X, Y as Z } from '...'  /  export { X, Y };
export_object_re = re.compile(r"export\s+\{([^}]+)\}")


def resolve_local_import(importer: Path, spec: str) -> Path | None:
    """Resolve a relative import spec to an actual source file path."""
    if not (spec.startswith("./") or spec.startswith("../") or spec.startswith("/")):
        return None  # bare/package import, skip
    base = (importer.parent / spec).resolve()
    # Try direct extensions
    for ext in ("", *TS_LIKE):
        p = Path(str(base) + ext) if ext else base
        if p.is_file():
            return p
    # Try /index.* if base is a directory
    if base.is_dir():
        for ext in TS_LIKE:
            p = base / f"index{ext}"
            if p.is_file():
                return p
    return None


def parse_exports(src_path: Path) -> set[str]:
    """Return the set of named exports from a source file."""
    txt = src_path.read_text(encoding="utf-8", errors="ignore")
    # Strip /* */ and // comments crudely so they don't pollute matches
    txt = re.sub(r"/\*.*?\*/", "", txt, flags=re.DOTALL)
    txt = re.sub(r"(?m)^\s*//.*$", "", txt)
    names: set[str] = set()
    names.update(export_named_re.findall(txt))
    for blob in export_object_re.findall(txt):
        for raw in blob.split(","):
            piece = raw.strip()
            if not piece:
                continue
            # Handle "X as Y" — export name is whatever appears AFTER `as`
            after_as = re.match(r"[A-Za-z_$][\w$]*\s+as\s+([A-Za-z_$][\w$]*)", piece)
            if after_as:
                names.add(after_as.group(1))
            else:
                m = re.match(r"([A-Za-z_$][\w$]*)", piece)
                if m:
                    names.add(m.group(1))
    return names


def imported_names_from_clause(blob: str) -> list[str]:
    """Extract the source-side names from a {...} import clause (handle 'as')."""
    out: list[str] = []
    for raw in blob.split(","):
        piece = raw.strip()
        if not piece:
            continue
        # Strip leading "type " (TypeScript inline type imports)
        piece = re.sub(r"^type\s+", "", piece)
        # "X as Y" — what we need to verify on the source side is X
        m = re.match(r"([A-Za-z_$][\w$]*)(?:\s+as\s+[A-Za-z_$][\w$]*)?", piece)
        if m:
            out.append(m.group(1))
    return out


# Cache parsed exports so we don't re-parse the same file for every importer
exports_cache: dict[Path, set[str]] = {}
dead_imports = []
for f in IMPORT_FILES:
    txt = f.read_text(encoding="utf-8", errors="ignore")
    for m in named_import_re.finditer(txt):
        clause = m.group(1)
        spec = m.group(2)
        target = resolve_local_import(f, spec)
        if target is None:
            continue  # external/package import, skip
        if target not in exports_cache:
            exports_cache[target] = parse_exports(target)
        exports = exports_cache[target]
        for name in imported_names_from_clause(clause):
            if name not in exports:
                dead_imports.append((f.name, name, spec, target.name))

if dead_imports:
    failures.append(f"{len(dead_imports)} dead/missing named imports")
    for src, name, spec, target in dead_imports:
        print(f"  DEAD     {src}: imports '{name}' from '{spec}' — not exported by {target}")
else:
    print(f"  PASS — every named import from {len(exports_cache)} local source files resolves to an actual export")


# ---------- summary ----------
print("\n" + "=" * 50)
if failures:
    print("FAILURES:")
    for x in failures:
        print(f"  - {x}")
    sys.exit(1)
print("ALL GUARDRAILS PASS")
