"""Swap in the new medal image, keeping the same filenames, max-width,
and output formats (PNG fallback + WebP) as the existing assets."""
from pathlib import Path
from PIL import Image, ImageOps

SRC      = Path(r"C:/Users/USER/Downloads/All-American Heroes Lifetime Achievement Award Metal 2.png")
DST_PNG  = Path(r"C:/Users/USER/countdown250/public/images/misc/all-amer-heroes-medal.png")
DST_WEBP = Path(r"C:/Users/USER/countdown250/public/images/misc/all-amer-heroes-medal.webp")
MAX_W    = 1000  # same as before

img = Image.open(SRC)
img = ImageOps.exif_transpose(img)
if img.mode not in ("RGBA", "LA"):
    img = img.convert("RGBA")
if img.width > MAX_W:
    ratio = MAX_W / img.width
    img = img.resize((MAX_W, int(round(img.height * ratio))), Image.LANCZOS)

img.save(DST_PNG,  format="PNG",  optimize=True)
img.save(DST_WEBP, format="WEBP", quality=88, method=6, lossless=False)

print(f"PNG:  {DST_PNG.stat().st_size/1024:7.1f} KB  ({img.width}x{img.height})")
print(f"WebP: {DST_WEBP.stat().st_size/1024:7.1f} KB  ({img.width}x{img.height})")
