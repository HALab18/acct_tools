#!/usr/bin/env node
// Converts one icon SVG into the PNG sizes iOS actually reads for apple-touch-icon.
// Why this exists: apple-touch-icon is not reliably honored as SVG on iOS Safari,
// so every icon needs PNG fallbacks or the home-screen icon silently falls back
// to a screenshot of the page.
//
// Usage: node svg_to_pngs.js <icon-key> <icons-dir>
//   e.g. node svg_to_pngs.js kessan_icon ../../../src/icons
//
// Requires the `sharp` package to be resolvable (see SKILL.md for the
// install-run-cleanup recipe used in this project's environment).

const path = require('path');
const sharp = require('sharp');

const [, , iconKey, iconsDir] = process.argv;
if (!iconKey || !iconsDir) {
  console.error('Usage: node svg_to_pngs.js <icon-key> <icons-dir>');
  process.exit(1);
}

// 180: default/iPhone, 152: iPad, 167: iPad Pro, 120: smaller iPhone fallback,
// 512: spare high-res (OGP, favicons, future use).
const sizes = [180, 152, 167, 120, 512];
const svgPath = path.join(iconsDir, `${iconKey}.svg`);

(async () => {
  for (const size of sizes) {
    const outName = size === 180 ? `${iconKey}.png` : `${iconKey}-${size}.png`;
    await sharp(svgPath).resize(size, size).png().toFile(path.join(iconsDir, outName));
  }
  console.log(`${iconKey}: generated ${sizes.length} PNG sizes in ${iconsDir}`);
})();
