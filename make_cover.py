#!/usr/bin/env python3
"""Generate a 2000x2000 cover-image from a background image.

Takes a PNG/JPEG, scales it to fill a 2000x2000 square keeping its aspect
ratio (overflow is cropped off), then composites
badge (extracted from Cover_source.pdf) onto the bottom-right corner —
producing covers like Cover_result.png.

Usage:
    python3 make_cover.py INPUT OUTPUT

Example:
    python3 make_cover.py artwork.jpg cover.png
"""
import argparse
import os
import sys

from PIL import Image

SIZE = 2000
ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
OVERLAY_PATH = os.path.join(ASSET_DIR, "cover_overlay.png")


def fit_cover(img, size):
    """Scale to fill the square, center-crop the overflow (no distortion)."""
    w, h = img.size
    scale = max(size / w, size / h)
    nw, nh = round(w * scale), round(h * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - size) // 2
    top = (nh - size) // 2
    return img.crop((left, top, left + size, top + size))


def main(argv=None):
    p = argparse.ArgumentParser(description="Generate a 2000x2000 cover-image.")
    p.add_argument("input", help="Input PNG/JPEG used as the background")
    p.add_argument("output", help="Output PNG filename")
    args = p.parse_args(argv)

    if not os.path.isfile(args.input):
        p.error(f"input file not found: {args.input}")
    if not os.path.isfile(OVERLAY_PATH):
        p.error(f"overlay asset missing: {OVERLAY_PATH}")

    img = Image.open(args.input).convert("RGBA")
    base = fit_cover(img, SIZE)

    overlay = Image.open(OVERLAY_PATH).convert("RGBA")
    result = Image.alpha_composite(base, overlay)

    out = args.output
    if not os.path.splitext(out)[1]:
        out += ".png"
    result.save(out)
    print(f"Done: {out} ({result.size[0]}x{result.size[1]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
