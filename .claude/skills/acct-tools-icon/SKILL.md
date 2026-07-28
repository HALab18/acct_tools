---
name: acct-tools-icon
description: Create an iPhone home-screen icon (apple-touch-icon) and add a QR-code entry to the printable A4 tool sheet for a tool in this acct_tools repository, matching the existing 5 tools' visual design (gradient background, small pictogram, 2-character kanji label card). Use this whenever a new tool is added to acct_tools, or when the user asks to make/update/redesign an icon for one of the existing HTML tools, or asks to add a tool to the QR code sheet (src/qr_codes_v1.html / qr_codes_v1.pdf). Trigger even if the user just says "add an icon for this" or "make this look like the others" without naming the skill.
---

# acct_tools icon + QR sheet generator

This project (a set of standalone single-file HTML tax/payroll tools for
Japanese accounting, see the root `CLAUDE.md`) gives every tool an iPhone
home-screen icon and an entry on a printable A4 QR-code sheet. All 5 existing
tools share one visual language; the point of this skill is that the 6th,
7th, ... tool looks like it belongs to the same family instead of being
designed from scratch.

Read `references/icon-design-reference.md` before drawing anything — it has
the exact SVG structure, the fixed geometry that must not change, the 5
existing tools' colors/pictograms/labels (so you don't accidentally repeat
one), and the reasoning for how to pick a new gradient and a new 2-character
label.

## Workflow

### 1. Design the icon
Using the reference file's template and guidance, decide:
- a gradient (two hex colors, distinct from the 5 already in use)
- a small corner pictogram hinting at what the tool does
- a 2-character label (kanji, or hiragana+kanji) that identifies the tool at a glance

Write the SVG to `src/icons/<tool_key>_icon.svg` (pick `<tool_key>` to match
the tool's existing filename convention, e.g. `kessan_icon` for a tool file
named `kessan_v1.html`).

### 2. Convert to PNG
iOS does not reliably honor SVG for `apple-touch-icon` — without PNG
fallbacks the home-screen icon silently falls back to a screenshot of the
page instead of your design. The bundled `scripts/svg_to_pngs.js` handles
this; it depends on the `sharp` package, installed once as a local,
gitignored dependency of the scripts folder itself (not of the web app —
`sharp` never ships to the browser).

```bash
# one-time setup, only if scripts/node_modules doesn't exist yet:
cd /path/to/this/skill/scripts && npm install --no-fund --no-audit
# if this reports exit code 1 with no node_modules created, just run it
# again — that first failure is transient, not a real error

# every time you need PNGs:
node /path/to/this/skill/scripts/svg_to_pngs.js <tool_key>_icon <path/to/repo>/src/icons
```

Run `node .../svg_to_pngs.js` from anywhere — module resolution depends on
where `node_modules` lives relative to the script file, not on the current
directory, so there's no need to `cd` into the icons folder or a temp
directory first. This produces `<tool_key>_icon.png` (180×180), `-152.png`,
`-167.png`, `-120.png`, and `-512.png` alongside the SVG.

### 3. Wire up the HTML `<head>`
In the tool's HTML file, right after `<title>` and before any other
`<link>`/CDN tags, add:

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="（short app name, ~6 zenkaku chars max）">
<link rel="apple-touch-icon" href="icons/<tool_key>_icon.png">
<link rel="apple-touch-icon" sizes="152x152" href="icons/<tool_key>_icon-152.png">
<link rel="apple-touch-icon" sizes="167x167" href="icons/<tool_key>_icon-167.png">
<link rel="apple-touch-icon" sizes="180x180" href="icons/<tool_key>_icon.png">
<link rel="icon" href="icons/<tool_key>_icon.svg" type="image/svg+xml">
```

The plain `<link rel="icon">` can safely point at the SVG — that's just the
browser-tab favicon, and browsers handle SVG favicons fine. Only
`apple-touch-icon` needs the PNG.

### 4. Add the tool to the QR-code sheet
`src/qr_codes_v1.html` is a single A4 page listing every tool as a row (icon,
name, one-line description, URL, QR code). Add a new `.row` following the
existing markup pattern (each row has `--accent` set to that tool's darker
gradient stop, an `<img class="icon">`, and a `.qr-box` containing an inline
`<svg>`).

Generate that inline QR SVG with the bundled script instead of hand-rolling
QR matrix logic — it renders the QR as static `<rect>` elements so the sheet
has no runtime dependency on an external QR service:

```bash
pip install qrcode  # if not already available
python /path/to/this/skill/scripts/generate_qr_svg.py \
  "https://halab18.github.io/acct_tools/src/<tool_file>.html" \
  -o /tmp/qr.svg
```
Paste the contents of `/tmp/qr.svg` into the row's `.qr-box`.

After editing the HTML, regenerate the PDF (the sheet is meant to be
printable without opening a browser). Start the project's static server
(`.claude/launch.json` → `static`, port 8734) if it isn't already running,
then:

```bash
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="<absolute path>\src\qr_codes_v1.pdf" \
  --no-margins "http://localhost:8734/src/qr_codes_v1.html"
```

Verify the result by reading the generated PDF back (the Read tool renders
PDF pages as images) — check the new row's icon, kanji label, and QR code
all look right before considering this step done.

### 5. Update README.md / CLAUDE.md
Per this project's convention, add the new tool to README.md's tool table
and detail section, and to CLAUDE.md's file-structure listing, following the
existing entries' format.

## When only the icon is needed

If the user only asks for an icon (not the QR sheet), do steps 1-3 and stop
there — don't force step 4/5 on them unprompted. Confirm scope if it's
ambiguous whether they want the full treatment or just the icon.
