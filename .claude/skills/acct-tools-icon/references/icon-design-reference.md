# icon design reference — existing 5 tools

This is the concrete pattern all 5 current acct_tools icons follow. Copy the
structure below and swap in new values — don't redesign from scratch, since
visual consistency across the tool set is the whole point.

## Anatomy of one icon SVG

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="180" height="180" viewBox="0 0 180 180">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{GRADIENT_START};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{GRADIENT_END};stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.2"/>
    </filter>
    <filter id="cardshadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="180" height="180" fill="url(#grad)"/>

  <!-- ambient depth, always the same two circles -->
  <circle cx="140" cy="45" r="48" fill="#ffffff" opacity="0.08"/>
  <circle cx="35" cy="140" r="40" fill="#ffffff" opacity="0.06"/>

  <!-- SMALL pictogram that hints at the tool's subject, tucked into a corner
       so it reads as background texture, not the focal point. Use white
       and/or gold (#fbbf24) at 0.2-0.9 opacity. Keep it inside roughly
       x:20-70, y:85-140 (bottom-left) so it doesn't collide with the card. -->
  {PICTOGRAM_ELEMENTS}

  <!-- the 2-character label card: this IS the focal point -->
  <rect x="50" y="42" width="80" height="98" rx="18" fill="#0f172a" opacity="0.42" filter="url(#cardshadow)"/>
  <rect x="50" y="42" width="80" height="98" rx="18" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.18"/>
  <text x="90" y="93" font-family="'Noto Serif JP','Hiragino Mincho ProN',serif" font-size="48" font-weight="700" fill="#ffffff" text-anchor="middle">{CHAR_1}</text>
  <text x="90" y="137" font-family="'Noto Serif JP','Hiragino Mincho ProN',serif" font-size="48" font-weight="700" fill="#ffffff" text-anchor="middle">{CHAR_2}</text>

  <line x1="20" y1="18" x2="160" y2="18" stroke="#ffffff" stroke-width="2" opacity="0.15"/>
</svg>
```

Fixed constants — don't vary these between tools, that's what makes the set
read as one family:
- Overall size/viewBox: `180 180`, no rounded corners on the outer square (iOS masks it)
- Card geometry: `x=50 y=42 width=80 height=98 rx=18`
- Card fill: `#0f172a` at `opacity=0.42`, 1px white stroke at `opacity=0.18`
- Character size/position: `font-size=48`, `x=90`, `y=93` and `y=137`
- Font stack: `'Noto Serif JP','Hiragino Mincho ProN',serif`, weight `700`
- Decorative circles: same two, same opacity, every time

What should vary per tool: the gradient colors, the pictogram, and the two characters.

## The 5 existing tools (don't reuse these colors for a new tool)

| Tool | File | Gradient | 2-char label | Pictogram |
|---|---|---|---|---|
| ふるさと納税 寄付上限額 算定ツール | Furusto_Rimit_Tax.html | `#1e40af` → `#3b82f6` (blue) | ふ / 納 | heart shape + small ¥ badge circle |
| 法人税・地方税 概算計算ツール | houjinzei_gaisan_v1.html | `#0369a1` → `#0ea5e9` (cyan-blue) | 法 / 税 | small building/window grid + bar chart |
| 法人版 利子所得税 計算シート | interest_calculator_v4.html | `#059669` → `#10b981` (green) | 利 / 所 | bank building (roof + pillars + window grid) + up arrow |
| 借入金 返済予定表 作成ツール | kariire_hensai_v1.html | `#7c3aed` → `#a78bfa` (purple) | 借 / 返 | calendar (header strip + date dots) + checkmark |
| 手取り逆算ツール｜給与計算 | tedori_gyaku_v3.html | `#d97706` → `#f59e0b` (orange) | 手 / 取 | pay-slip sheet (header + text lines) + arrow |

Actual pictogram SVG fragments (copy the closest match and adapt scale/position — these all live in `src/icons/*.svg` if you want the full file):

```svg
<!-- heart (furusato) -->
<path d="M 40 118 Q 30 108 30 98 Q 30 91 37 91 Q 42 91 45 95 Q 48 91 53 91 Q 60 91 60 98 Q 60 108 50 118 Z" fill="#fbbf24" opacity="0.9" filter="url(#shadow)"/>

<!-- building/window grid (houjinzei) -->
<rect x="30" y="95" width="34" height="34" fill="#ffffff" opacity="0.2" rx="4"/>
<rect x="35" y="100" width="9" height="9" fill="#fbbf24" opacity="0.6" rx="1"/>
<rect x="50" y="100" width="9" height="9" fill="#fbbf24" opacity="0.6" rx="1"/>
<rect x="35" y="114" width="9" height="9" fill="#fbbf24" opacity="0.4" rx="1"/>
<rect x="50" y="114" width="9" height="9" fill="#fbbf24" opacity="0.4" rx="1"/>

<!-- bank building (interest) -->
<path d="M 26 108 L 46 95 L 66 108 L 66 103 L 26 103 Z" fill="#ffffff" opacity="0.3"/>
<rect x="26" y="108" width="40" height="26" fill="#ffffff" opacity="0.2" rx="2"/>
<rect x="33" y="114" width="7" height="7" fill="#fbbf24" opacity="0.7" rx="1"/>
<rect x="48" y="114" width="7" height="7" fill="#fbbf24" opacity="0.7" rx="1"/>

<!-- calendar (kariire) -->
<rect x="26" y="98" width="42" height="38" fill="#ffffff" opacity="0.2" rx="4"/>
<rect x="26" y="98" width="42" height="10" fill="#ffffff" opacity="0.3" rx="4"/>
<circle cx="34" cy="118" r="2.5" fill="#ffffff" opacity="0.6"/>
<circle cx="47" cy="118" r="2.5" fill="#fbbf24" opacity="0.8"/>

<!-- pay-slip sheet (tedori) -->
<rect x="24" y="100" width="38" height="32" fill="#ffffff" opacity="0.2" rx="2"/>
<rect x="24" y="100" width="38" height="7" fill="#ffffff" opacity="0.3" rx="2"/>
<line x1="29" y1="112" x2="57" y2="112" stroke="#ffffff" stroke-width="1" opacity="0.5"/>
```

## Choosing a gradient for a new tool

Pick two colors that are visually distinct from all 5 above at a glance (this
is what lets someone scan a row of icons and tell them apart instantly).
Rough hue families already taken: blue, cyan, green, purple, orange. Good
next choices: red/rose (`#be123c`→`#f43f5e`), teal (`#0f766e`→`#2dd4bf`),
indigo (`#4338ca`→`#818cf8`), pink (`#a21caf`→`#e879f9`). Keep the gradient
direction `x1=0% y1=0% x2=100% y2=100%` and keep both stops fully opaque —
only the hue should change.

## Choosing the 2-character label

The goal is that someone glancing at a phone home screen full of small icons
can tell what each one does without reading the full name. Pick two
characters using this priority:
1. If the tool's official name is a natural 2-kanji compound word, use it
   as-is (e.g. 返済 for "repayment", 利子 for "interest") — but check it's
   not already used to label a *different* tool, since the point is
   disambiguation. If the two most natural characters would be ambiguous
   with an existing icon, pick a different pair from the name that's still
   meaningful (this project has done this — 借返 and 利所 were chosen over
   the more obvious 返済/利子 specifically to avoid confusion with related
   tools covering adjacent tax topics).
2. If the tool's name starts in hiragana with no natural kanji anchor (e.g.
   ふるさと納税), take the first hiragana character plus one kanji from
   later in the name (ふ + 納).
3. Avoid using a character already used in another tool's label unless the
   tool is genuinely a variant/successor of that one (e.g. a v2 of an
   existing tool could reasonably reuse its label).

Always sanity-check that the two characters, stacked vertically at font-size
48 in a 90x98 card, read clearly at a glance — very stroke-dense kanji (many
strokes, like 鬱 or 齢) don't render legibly at this size. Prefer common,
low-to-medium stroke-count characters.
