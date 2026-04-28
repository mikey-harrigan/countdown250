"""Compress all 12 experience-carousel images.

7 NEW real photos from Downloads + 4 existing photos to recompress.
Slide 1 (hilton-twilight.jpg) was already compressed in the prior pass.

Strategy:
  - Real photos: max 1600px wide, JPEG q82, progressive, EXIF stripped
  - Existing PNGs that are photos: convert to .jpg
"""
from pathlib import Path
from PIL import Image, ImageOps

DOWN = Path(r"C:/Users/USER/Downloads")
EVT  = Path(r"C:/Users/USER/countdown250/public/images/event")
MAX_W = 1600
QUALITY = 82

# (src_path, dst_path, mode)
JOBS = [
    # NEW from Downloads
    (DOWN / "Entertainment_Picture_piano player.jpg",                       EVT / "piano-player.jpg",          "jpg"),
    (DOWN / "Entertainment_AA Inagural Ball Jan 18 2025 Jpeg-39.jpg",       EVT / "saxophonist.jpg",           "jpg"),
    (DOWN / "Entertainment_AA Inagural Ball Jan 18 2025 Jpeg-84.jpg",       EVT / "singer-flag-screen.jpg",    "jpg"),
    (DOWN / "Entertainment_AA Inagural Ball Jan 18 2025 Jpeg-192.jpg",      EVT / "performer-eagle-screen.jpg","jpg"),
    (DOWN / "Celebrating_AA Inagural Ball Jan 18 2025 Jpeg-528.jpg",        EVT / "veterans-celebrating.jpg",  "jpg"),
    (DOWN / "Celebrating!!_AA Inagural Ball Jan 18 2025 Jpeg-534.jpg",      EVT / "guests-elegant-quartet.jpg","jpg"),
    (DOWN / "Celebrating_AA Inagural Ball Jan 18 2025 Jpeg-549.jpg",        EVT / "guests-friendship.jpg",     "jpg"),

    # EXISTING — recompress in place (jpg) or convert (png photo -> jpg)
    (EVT / "ballroom-crowd.jpg",                                             EVT / "ballroom-crowd.jpg",       "jpg"),
    (EVT / "countdown-toast.png",                                            EVT / "countdown-toast.jpg",      "jpg"),
    (EVT / "dj-party-lights.png",                                            EVT / "dj-party-lights.jpg",      "jpg"),
    (EVT / "red-carpet-arrival.png",                                         EVT / "red-carpet-arrival.jpg",   "jpg"),
]


for src, dst, mode in JOBS:
    if not src.exists():
        print(f"MISSING: {src}")
        continue
    before = src.stat().st_size / 1024
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    if img.width > MAX_W:
        ratio = MAX_W / img.width
        img = img.resize((MAX_W, int(round(img.height * ratio))), Image.LANCZOS)
    img.save(dst, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    after = dst.stat().st_size / 1024
    print(f"{dst.name:38s}  {img.width}x{img.height:5d}  {before:7.1f} KB -> {after:7.1f} KB")
