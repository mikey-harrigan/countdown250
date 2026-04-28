"""Convert PNGs with transparency to WebP for modern browsers.

WebP supports alpha and is dramatically smaller than PNG for
photographic / gradient content. We KEEP the .png siblings so
the <picture> element can fall back for the ~3% of browsers
that don't support WebP.
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(r"C:/Users/USER/countdown250/public/images")

JOBS = [
    (ROOT / "misc/all-amer-heroes-medal.png",          ROOT / "misc/all-amer-heroes-medal.webp",          1000),
    (ROOT / "logos/countdown250-seal-circle-dark.png", ROOT / "logos/countdown250-seal-circle-dark.webp", 800),
]

# WebP quality 88 is visually lossless for gradients; keeps file tiny.
QUALITY = 88

for src, dst, max_w in JOBS:
    if not src.exists():
        print(f"MISSING: {src}")
        continue
    before = src.stat().st_size / 1024
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)
    if img.mode not in ("RGBA", "LA"):
        img = img.convert("RGBA")
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(round(img.height * ratio))), Image.LANCZOS)
    img.save(dst, format="WEBP", quality=QUALITY, method=6, lossless=False)
    after = dst.stat().st_size / 1024
    saved = (1 - after / before) * 100
    print(f"{src.name:42s} -> {dst.name:42s}  {before:7.1f} KB -> {after:7.1f} KB   ({saved:5.1f}% smaller)")
