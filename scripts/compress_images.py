"""
compress_images.py
==================
One-shot in-place compression for /public/images/.

Strategy (conservative — no filename changes, no path changes):

  JPG/JPEG
    - If max(width, height) > 2400 px, downscale (LANCZOS) so the
      longest edge is 2400 px. This is plenty for a 1440-wide CSS
      hero on a 2x DPR display.
    - Re-save quality=82, optimize=True, progressive=True,
      subsampling=2 (4:2:0). Strip EXIF (saves ~50–200 KB on
      camera originals).

  PNG
    - If image has alpha (transparency), keep as PNG. Run
      Pillow's quantize(method=2, colors=256) only if the file is
      >1.5 MB AND result is smaller. Falls back to optimize=True.
    - If no alpha and file is >1.5 MB, the PNG is almost certainly
      a photograph saved in the wrong format. Convert in place by
      saving as JPG at quality=82 BUT keeping the .png filename
      (browsers sniff content type by bytes for images, and the
      file is served as binary; references in HTML use the .png
      path and stay intact). This avoids a sweep of HTML/Astro
      refs.

  Safety
    - Only writes a new file if it is at least 15 % smaller than
      the original (avoid making things worse on already-optimised
      assets). Otherwise leaves the file untouched.
    - Skips icons/logos under 200 KB — not worth the risk of
      visible artifacting on small brand marks.
    - Prints a per-file before/after table and a grand total at
      the end.
"""

from __future__ import annotations

import io
import os
import sys
from pathlib import Path

# Windows cmd defaults to cp1252; force stdout to UTF-8 so arrows render.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent / "public" / "images"
MAX_EDGE = 2400          # px — longest edge for JPGs
JPG_QUALITY = 82
PNG_SIZE_THRESHOLD = 1.5 * 1024 * 1024
SKIP_BELOW = 200 * 1024
MIN_SAVING_RATIO = 0.15  # require >=15% smaller before overwriting

results = []  # list of (path, before, after, action)


def format_mb(n: int) -> str:
    return f"{n / 1024 / 1024:6.2f} MB"


def compress_jpg(path: Path) -> tuple[int, int, str]:
    before = path.stat().st_size
    with Image.open(path) as im:
        im.load()
        action_parts = []

        # Drop EXIF; strip ICC profile only if image is already sRGB-ish
        if max(im.size) > MAX_EDGE:
            w, h = im.size
            scale = MAX_EDGE / max(w, h)
            new_size = (int(round(w * scale)), int(round(h * scale)))
            im = im.resize(new_size, Image.LANCZOS)
            action_parts.append(f"resize->{new_size[0]}x{new_size[1]}")

        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")

        buf = io.BytesIO()
        im.save(
            buf,
            format="JPEG",
            quality=JPG_QUALITY,
            optimize=True,
            progressive=True,
            subsampling=2,
        )
        data = buf.getvalue()
        after = len(data)

        if before - after < before * MIN_SAVING_RATIO:
            return before, before, "skipped (savings <15%)"

        path.write_bytes(data)
        return before, after, "jpg re-encode" + (" + " + " + ".join(action_parts) if action_parts else "")


def compress_png(path: Path) -> tuple[int, int, str]:
    before = path.stat().st_size
    with Image.open(path) as im:
        im.load()
        has_alpha = "A" in im.getbands()

        if has_alpha:
            # Keep PNG. Try palette quantize if big.
            best = before
            best_bytes = None
            best_action = ""

            # Attempt 1: simple optimize, in current mode
            buf = io.BytesIO()
            try:
                im.save(buf, format="PNG", optimize=True)
                cand = buf.getvalue()
                if len(cand) < best:
                    best, best_bytes, best_action = len(cand), cand, "png optimize"
            except Exception:
                pass

            # Attempt 2: quantize down to 256 colours (preserves alpha via mode P + transparency)
            if before > PNG_SIZE_THRESHOLD:
                try:
                    q = im.quantize(colors=256, method=2)
                    buf = io.BytesIO()
                    q.save(buf, format="PNG", optimize=True)
                    cand = buf.getvalue()
                    if len(cand) < best:
                        best, best_bytes, best_action = len(cand), cand, "png quantize(256)"
                except Exception:
                    pass

            if best_bytes is None or before - best < before * MIN_SAVING_RATIO:
                return before, before, "skipped (alpha PNG, savings <15%)"

            path.write_bytes(best_bytes)
            return before, best, best_action

        # No alpha. If file is small, just optimize. If big, re-save as JPG bytes under .png filename.
        if before <= PNG_SIZE_THRESHOLD:
            buf = io.BytesIO()
            im.save(buf, format="PNG", optimize=True)
            cand = buf.getvalue()
            if before - len(cand) < before * MIN_SAVING_RATIO:
                return before, before, "skipped (small PNG, savings <15%)"
            path.write_bytes(cand)
            return before, len(cand), "png optimize"

        # Big PNG, no alpha — convert to JPG bytes but keep .png filename.
        rgb = im.convert("RGB")
        if max(rgb.size) > MAX_EDGE:
            w, h = rgb.size
            scale = MAX_EDGE / max(w, h)
            rgb = rgb.resize(
                (int(round(w * scale)), int(round(h * scale))), Image.LANCZOS
            )

        buf = io.BytesIO()
        rgb.save(
            buf,
            format="JPEG",
            quality=JPG_QUALITY,
            optimize=True,
            progressive=True,
            subsampling=2,
        )
        data = buf.getvalue()
        if before - len(data) < before * MIN_SAVING_RATIO:
            return before, before, "skipped (PNG->JPG, savings <15%)"

        path.write_bytes(data)
        return before, len(data), "PNG->JPG bytes (filename kept)"


def main() -> int:
    if not ROOT.exists():
        print(f"Root not found: {ROOT}", file=sys.stderr)
        return 1

    files = sorted(p for p in ROOT.rglob("*") if p.is_file())
    total_before = 0
    total_after = 0
    touched = 0

    for path in files:
        ext = path.suffix.lower()
        if ext not in {".jpg", ".jpeg", ".png"}:
            continue
        size = path.stat().st_size
        if size < SKIP_BELOW:
            continue

        try:
            if ext in {".jpg", ".jpeg"}:
                before, after, action = compress_jpg(path)
            else:
                before, after, action = compress_png(path)
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR  {path.relative_to(ROOT)}: {exc}")
            continue

        total_before += before
        total_after += after
        if after < before:
            touched += 1
        rel = path.relative_to(ROOT)
        try:
            print(
                f"  {format_mb(before)} -> {format_mb(after)}  "
                f"({(1 - after / before) * 100:5.1f}% saved)  "
                f"[{action}]  {rel}"
            )
        except UnicodeEncodeError:
            print(
                f"  {format_mb(before)} -> {format_mb(after)}  "
                f"({(1 - after / before) * 100:5.1f}% saved)  "
                f"[{action}]  {rel}".encode("ascii", "replace").decode("ascii")
            )

    print("=" * 70)
    print(
        f"  TOTAL  {format_mb(total_before)} -> {format_mb(total_after)}  "
        f"({(1 - total_after / max(total_before, 1)) * 100:5.1f}% saved)  "
        f"{touched} files modified"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
