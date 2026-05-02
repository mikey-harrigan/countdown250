"""
One-shot optimizer for the new horizontal navbar wordmark Mike approved
on 2026-05-02 ("Logo_250_final_BEST LOGO COLOR EVER_navbar.png").

The source is 1536x1024 with substantial transparent padding around a
horizontal banner. We:
  1. Auto-crop transparent edges to the banner's bounding box
  2. Downscale so the banner is no more than 800px wide (2x of the
     ~340-400px display width is plenty for retina)
  3. Save as both PNG (transparent fallback) and WebP (smaller)
"""

from pathlib import Path
from PIL import Image

SRC = Path(r"C:\Users\USER\Downloads\Logo_250_final_BEST LOGO COLOR EVER_navbar.png")
DST_DIR = Path(r"C:\Users\USER\countdown250\public\images\logos")
PNG_DST = DST_DIR / "countdown250-wordmark-navbar-blue.png"
WEBP_DST = DST_DIR / "countdown250-wordmark-navbar-blue.webp"

MAX_WIDTH = 900  # banner displays at ~280-450px; 900 gives 2x retina headroom


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    img = Image.open(SRC)
    print(f"[INFO] source: {img.size[0]}x{img.size[1]}, mode {img.mode}, {SRC.stat().st_size // 1024} KB")

    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Step 1: tight-crop transparent padding (alpha threshold > 60/255)
    alpha = img.split()[-1]
    threshold_mask = alpha.point(lambda a: 255 if a > 60 else 0)
    bbox = threshold_mask.getbbox()
    if bbox:
        before = img.size
        img = img.crop(bbox)
        print(f"[INFO] tight-cropped to banner: {before} -> {img.size}")

    # Step 2: re-pad with transparent space to match the OLD navbar logo's
    # container aspect ratio (1.5:1 — the container the previous wordmark
    # sat inside, with the banner taking ~60% width / ~25% height). This
    # way the existing navbar CSS heights render the new banner at the
    # same visual size as the old one.
    bw, bh = img.size
    target_aspect = 1.5  # container width:height
    container_h = int(bh / 0.25)         # banner = ~25% of container height
    container_w = int(container_h * target_aspect)
    # Make sure container is wide enough for the banner (else widen it)
    if container_w < int(bw / 0.60):
        container_w = int(bw / 0.60)
        container_h = int(container_w / target_aspect)
    padded = Image.new("RGBA", (container_w, container_h), (0, 0, 0, 0))
    paste_x = (container_w - bw) // 2
    paste_y = (container_h - bh) // 2
    padded.paste(img, (paste_x, paste_y))
    img = padded
    print(f"[INFO] padded to old container ratio: {img.size}")

    # Step 3: downscale if wider than MAX_WIDTH
    w, h = img.size
    if w > MAX_WIDTH:
        new_h = int(h * (MAX_WIDTH / w))
        img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    DST_DIR.mkdir(parents=True, exist_ok=True)
    img.save(PNG_DST, format="PNG", optimize=True)
    img.save(WEBP_DST, format="WEBP", quality=90, method=6)

    print(f"[OK] {PNG_DST.name}  {PNG_DST.stat().st_size // 1024} KB  @ {img.size[0]}x{img.size[1]}")
    print(f"[OK] {WEBP_DST.name}  {WEBP_DST.stat().st_size // 1024} KB  @ {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
