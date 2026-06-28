---
name: cover-image-generator
description: Generate a 2000x2000 cover-image PNG from an image the user provides or attaches. Use whenever the user asks to "make/generate/create a cover-image" (or "cover from this image") from a PNG or JPEG. The image is scaled to fill a 2000x2000 square keeping aspect ratio (overflow cropped), then the logo badge is overlaid in the bottom-right corner.
---

# Cover-image generator

Turns any PNG/JPEG into a 2000×2000 cover-image with the logo
badge composited onto the bottom-right corner.

## When to use
The user attaches or points to an image and asks to "make a cover-image",
"generate a cover-image", "create a cover from this image", etc.

## How to run
1. Make sure Pillow is available in the execution environment. If importing
   `PIL` fails, install it first:
   ```bash
   pip install Pillow
   ```
2. Run the bundled script, passing the user's image and an output path.
   Use the skill directory as the base for the script and its asset.
   ```bash
   python3 make_cover.py "<INPUT_IMAGE>" "<OUTPUT>.png"
   ```
   - `<INPUT_IMAGE>` — the file the user attached/provided (PNG or JPEG).
   - `<OUTPUT>.png` — where to write the result; name it after the input,
     e.g. `some_cover.png`.
3. Return the generated PNG back to the user in the chat as a downloadable
   file. Confirm the output is 2000×2000.

## Notes
- The script always fills the 2000×2000 frame keeping aspect ratio and crops
  anything outside it — it never distorts or pads. It takes exactly two
  arguments (input, output); there are no other options.
- `assets/cover_overlay.png` is the transparent 2000×2000 badge layer.
  The script loads it relative to its own location, so keep `make_cover.py`
  and `assets/` together. Replace that PNG to change the branding; keep it 2000×2000.
