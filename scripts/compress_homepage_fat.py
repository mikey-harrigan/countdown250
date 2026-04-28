"""One-time compression pass on the 5 fat homepage images.

Strategy:
  - PNG photos with NO transparency  -> convert to .jpg @ 1600px q82
  - Existing JPG                     -> recompress in place @ 1600px q82
  - PNG with transparency            -> keep PNG, resize + optimize=True

Run from repo root:  python scripts/compress_homepage_fat.py
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(r"C:/Users/USER/countdown250/public/images")
QUALITY = 82

# (input_path, output_path, max_width, mode)
# mode: 'jpg' = convert/save jpg, 'png' = save optimized png (preserve transparency)
JOBS = [
    (ROOT / "event/hero-countdown250-toast.png", ROOT / "event/hero-countdown250-toast.jpg", 1600, "jpg"),
    (ROOT / "event/hilton-twilight.png",         ROOT / "event/hilton-twilight.jpg",         1600, "jpg"),
    (ROOT / "event/inaugural-ceremony-flag.jpg", ROOT / "event/inaugural-ceremony-flag.jpg", 1600, "jpg"),
    (ROOT / "misc/all-amer-heroes-medal.png",    ROOT / "misc/all-amer-heroes-medal.png",    1000, "png"),
    (ROOT / "logos/countdown250-seal-circle-dark.png", ROOT / "logos/countdown250-seal-circle-dark.png", 800, "png"),
]


def fmt_size(p: Path) -> str:
    return f"{p.stat().st_size/1024:8.1f} KB"


for src, dst, max_w, mode in JOBS:
    if not src.exists():
        print(f"MISSING: {src}")
        continue

    before = src.stat().st_size / 1024
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)

    if mode == "jpg":
        # Flatten any alpha onto white before JPEG save
        if img.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")
    else:  # png — keep alpha
        if img.mode not in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")

    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(round(img.height * ratio))), Image.LANCZOS)

    if mode == "jpg":
        img.save(dst, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    else:
        img.save(dst, format="PNG", optimize=True)

    after = dst.stat().st_size / 1024
    saved_pct = (1 - after / before) * 100 if before > 0 else 0
    print(f"{src.name:42s} -> {dst.name:38s}  {before:7.1f} KB -> {after:7.1f} KB   ({saved_pct:5.1f}% smaller)")
