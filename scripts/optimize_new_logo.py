"""
One-shot optimizer for the new "BEST LOGO EVER" navy-blue-background
Countdown 250 seal Mike approved on 2026-05-01.

Saves a web-sized PNG and a WebP into public/images/logos/.

The hero displays the logo at max ~340px wide, so 700px source is
plenty for retina (2x) on any reasonable display.
"""

from pathlib import Path
from PIL import Image

SRC = Path(r"C:\Users\USER\Downloads\BEST LOGO EVER_ChatGPT Image May 1, 2026, 06_37_21 PM.png")
DST_DIR = Path(r"C:\Users\USER\countdown250\public\images\logos")
PNG_DST = DST_DIR / "countdown250-seal-navy-blue.png"
WEBP_DST = DST_DIR / "countdown250-seal-navy-blue.webp"

MAX_WIDTH = 700  # logo displays at max 340px; 2x for retina is sufficient


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    img = Image.open(SRC)
    print(f"[INFO] source: {img.size[0]}x{img.size[1]}, mode {img.mode}, {SRC.stat().st_size // 1024} KB")

    # Convert to RGBA so we can read the alpha channel
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Auto-crop: trim the transparent padding around the seal so the
    # rendered logo fills its CSS box (the old square logo did this
    # naturally; the new source has rectangular padding).
    bbox = img.getbbox()
    if bbox:
        before = img.size
        img = img.crop(bbox)
        print(f"[INFO] cropped to seal: {before} -> {img.size}")

    # Downscale if wider than MAX_WIDTH (never upscale)
    w, h = img.size
    if w > MAX_WIDTH:
        new_h = int(h * (MAX_WIDTH / w))
        img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    DST_DIR.mkdir(parents=True, exist_ok=True)

    # PNG: keep alpha, optimize
    img.save(PNG_DST, format="PNG", optimize=True)
    # WebP: lossless quality 90 still huge for 700px logos. Use lossy
    # quality 90 which keeps the gold filigree sharp.
    img.save(WEBP_DST, format="WEBP", quality=90, method=6)

    print(f"[OK] {PNG_DST.name}  {PNG_DST.stat().st_size // 1024} KB  @ {img.size[0]}x{img.size[1]}")
    print(f"[OK] {WEBP_DST.name}  {WEBP_DST.stat().st_size // 1024} KB  @ {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
