"""
One-shot image optimizer for the 5 new AI crowd shots Mike approved on
2026-05-01. Converts the heavy PNGs in Downloads to web-ready JPGs in
public/images/event/.

Targets:
  - Max width 1600px (preserves desktop hero quality, more than enough)
  - JPEG quality 84 (good visual fidelity, much smaller than PNG)
  - Aim for under 400KB per file

Run once. Safe to re-run (overwrites).
"""

from pathlib import Path
from PIL import Image

# (source path in Downloads, destination path in public/images/event/)
PAIRS = [
    (
        r"C:\Users\USER\Downloads\GOOD AI CROWD SHOTS_02_small_group_mingling.png",
        r"C:\Users\USER\countdown250\public\images\event\small-group-toasting.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\GOOD AI CROWD SHOTS_03_dj_dance_floor.png",
        r"C:\Users\USER\countdown250\public\images\event\dj-dance-floor-flags.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\GOOD AI CROWD SHOTS_04_step_and_repeat.png",
        r"C:\Users\USER\countdown250\public\images\event\step-and-repeat-photo.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\GOOD AI CROWD SHOTS_09_vip_dinner_table.png",
        r"C:\Users\USER\countdown250\public\images\event\vip-dinner-table-group.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\GOOD AI CROWD SHOTS_ChatGPT Image May 1, 2026, 01_59_57 PM.png",
        r"C:\Users\USER\countdown250\public\images\event\statesmans-vip-tables.jpg",
    ),
]

MAX_WIDTH = 1600
JPEG_QUALITY = 84


def optimize(src: str, dst: str) -> None:
    p_src, p_dst = Path(src), Path(dst)
    if not p_src.exists():
        print(f"[SKIP] missing: {p_src.name}")
        return

    img = Image.open(p_src)
    # Convert to RGB (PNG may be RGBA)
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Downscale if wider than MAX_WIDTH (never upscale)
    w, h = img.size
    if w > MAX_WIDTH:
        new_h = int(h * (MAX_WIDTH / w))
        img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    p_dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(p_dst, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

    src_kb = p_src.stat().st_size // 1024
    dst_kb = p_dst.stat().st_size // 1024
    print(f"[OK] {p_src.name}  ({src_kb} KB) -> {p_dst.name}  ({dst_kb} KB) @ {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    for src, dst in PAIRS:
        optimize(src, dst)
