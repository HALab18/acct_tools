#!/usr/bin/env python3
"""Generate a self-contained SVG QR code for a URL.

Why: the tool-sheet QR codes must not depend on an external QR-rendering
service at print time or view time (acct_tools has a no-external-dependency
convention). This renders the QR matrix straight into <rect> elements, so the
resulting SVG is fully static and offline-safe.

Usage:
    python generate_qr_svg.py "https://halab18.github.io/acct_tools/src/foo.html"
    python generate_qr_svg.py "https://..." -o qr.svg
    python generate_qr_svg.py "https://..." --module-px 6 --dark "#1e293b"

Requires the `qrcode` package (pip install qrcode).
"""
import argparse

import qrcode


def svg_qr(url: str, module_px: int = 6, dark: str = "#1e293b", light: str = "#ffffff", border: int = 4) -> str:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=border,  # 4-module quiet zone is required for reliable scanning
    )
    qr.add_data(url)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    n = len(matrix)
    px = n * module_px

    rects = []
    for y, row in enumerate(matrix):
        x = 0
        while x < n:
            if row[x]:
                start = x
                while x < n and row[x]:
                    x += 1
                w = x - start
                rects.append(f'<rect x="{start*module_px}" y="{y*module_px}" width="{w*module_px}" height="{module_px}"/>')
            else:
                x += 1
    body = "".join(rects)
    return (
        f'<svg viewBox="0 0 {px} {px}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{px}" height="{px}" fill="{light}"/>'
        f'<g fill="{dark}">{body}</g></svg>'
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="URL to encode")
    parser.add_argument("--module-px", type=int, default=6, help="Pixel size of one QR module (default 6)")
    parser.add_argument("--dark", default="#1e293b", help="Dark module color (default #1e293b)")
    parser.add_argument("-o", "--output", help="Write SVG to this file instead of stdout")
    args = parser.parse_args()

    svg = svg_qr(args.url, module_px=args.module_px, dark=args.dark)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Wrote {args.output}")
    else:
        print(svg)
