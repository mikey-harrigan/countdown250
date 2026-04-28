"""Batch compress hero photos for web.

Resizes to max 1600px wide, JPEG quality 82, strips EXIF.
Source: C:/Users/USER/Downloads/
Dest:   C:/Users/USER/countdown250/public/images/event/
"""
from pathlib import Path
from PIL import Image, ImageOps

SRC = Path(r"C:/Users/USER/Downloads")
DST = Path(r"C:/Users/USER/countdown250/public/images/event")
MAX_W = 1600
QUALITY = 82

JOBS = [
    ("Heroes!!!_AA Inagural Ball Jan 18 2025 Jpeg-171.jpg",  "sean-spicer-stage.jpg"),
]

DST.mkdir(parents=True, exist_ok=True)

for src_name, dst_name in JOBS:
    src = SRC / src_name
    dst = DST / dst_name
    if not src.exists():
        print(f"MISSING: {src}")
        continue
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)  # honor EXIF rotation, then strip
    if img.mode != "RGB":
        img = img.convert("RGB")
    if img.width > MAX_W:
        ratio = MAX_W / img.width
        new_h = int(round(img.height * ratio))
        img = img.resize((MAX_W, new_h), Image.LANCZOS)
    img.save(dst, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    kb = dst.stat().st_size / 1024
    print(f"{dst_name:35s}  {img.width}x{img.height}  {kb:7.1f} KB")
