"""
One-shot optimizer for the 6 new "Reserved table pic" PNGs Mike added
to Downloads on 2026-05-01 ~8 PM. Same settings as
optimize_new_images.py: max width 1600px, JPEG quality 84, progressive,
target under 400 KB.

Run once. Safe to re-run (overwrites).
"""

from pathlib import Path
from PIL import Image

PAIRS = [
    (
        r"C:\Users\USER\Downloads\Reserved table pic 1_ChatGPT Image May 1, 2026, 08_18_44 PM.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-formal-dinner.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\Reserved table pic 2_02_hightop_table_mingling.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-hightop-mingling.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\Reserved table pic 3_03_vip_bar_mingling.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-vip-bar.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\Reserved table pic 4_04_hightop_group_conversation.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-hightop-conversation.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\Reserved table pic 5_05_passed_hors_doeuvres.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-hors-doeuvres.jpg",
    ),
    (
        r"C:\Users\USER\Downloads\Reserved table pic 6_05_passed_hors_doeuvres.png",
        r"C:\Users\USER\countdown250\public\images\event\reserved-table-jmu-alumni-signage.jpg",
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
    if img.mode != "RGB":
        img = img.convert("RGB")

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
