"""Generate pinned-repository style project cards with Option 2:
- Self-contained cards with rounded corners (rx=8) on all 4 corners
- Full card links to GitHub repository
- Eliminated redundant GitHub repo button
- Sleek, compact Live demo / Architecture pill buttons (width ~130px, height ~30px)
- Standard GitHub dark-mode palette (#0d1117, #161b22, #30363d, #58a6ff, #8b949e)
"""

import os
import textwrap
from html import escape

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
MUTED_BORDER = "#21262d"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"

STYLE = (
    "<style>"
    "text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}"
    "</style>"
)

REPOS = [
    (
        "card-ensembyte.svg",
        "soumyachk101/Ensembyte",
        "Open-source multi-agent coding client. macOS runs Hydra delegating to up to ∞ parallel heads in isolated worktrees; Windows and Linux run on GPUI with CRDT sync.",
        ("Swift", "#f05138"),
        ["Swift ∞ Hydra", "GPUI", "Loro CRDT"],
        None,
    ),
    (
        "card-veylqorix.svg",
        "soumyachk101/Veylqorix",
        "Code-security and quality gate platform. Orchestrates real scanners, normalizes findings into one schema, and enforces deterministic gate decisions with a standalone Rust security engine.",
        ("TypeScript", "#3178c6"),
        ["Security Gate", "Rust Engine", "Scanner Suite"],
        None,
    ),
    (
        "card-vercode.svg",
        "soumyachk101/VERCODE",
        "AI-powered code review SaaS for GitHub PRs. Deterministic static analysis (ESLint, Semgrep, secrets) runs first, followed by task-routed LLM reasoning with inline findings and team dashboard.",
        ("TypeScript", "#3178c6"),
        ["AI Code Review", "Static Analysis", "Monorepo"],
        None,
    ),
    (
        "card-credow.svg",
        "soumyachk101/Credow",
        "Corporate credit allocation on Algorand. Allowances are claimed through x402 payments, and unclaimed credits earn yield in an on-chain vault. FusioniX'26 winner.",
        ("TypeScript", "#3178c6"),
        ["Algorand", "x402 Protocol", "FusioniX'26"],
        ("FusioniX'26 Winner", "#d29922", "#161b22", "#3d2f16"),
    ),
    (
        "card-drishtinet.svg",
        "soumyachk101/DrishtiNet",
        "Maps a network as a graph of real attack paths and ranks vulnerable nodes by financial impact instead of CVSS alone. Graph-based risk prioritization engine.",
        ("Python", "#3572a5"),
        ["Cybersecurity", "Graph Analysis", "Innofusion 3.0"],
        None,
    ),
]

REPO_ICON = (
    "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75"
    "v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708"
    "A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2"
    "l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"
)

EXTERNAL_LINK_ICON = (
    "M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a1.25 1.25 0 0 0-1.25 1.25v7.5c0 .69.56 1.25 1.25 1.25h7.5c.69 0 1.25-.56 1.25-1.25"
    "v-3.5a.75.75 0 0 1 1.5 0v3.5A2.75 2.75 0 0 1 11.25 15h-7.5A2.75 2.75 0 0 1 1 12.25v-7.5A2.75 2.75 0 0 1 3.75 2Zm7.5 1.5"
    "H8.75a.75.75 0 0 1 0-1.5h4.5c.414 0 .75.336.75.75v4.5a.75.75 0 0 1-1.5 0V4.56L7.53 9.53a.75.75 0 0 1-1.06-1.06l4.97-4.97h-.19Z"
)

LAYERS_ICON = (
    "M1.5 4.5 8 1l6.5 3.5L8 8 1.5 4.5Zm0 4.25L8 12.25l6.5-3.5m-13 4.25L8 16.5l6.5-3.5"
)


def repo_card(name, repo, desc, lang, meta, award_badge=None) -> None:
    w, pad = 860, 24
    lines = textwrap.wrap(desc, int((w - 2 * pad) / (14 * 0.55)))
    h = pad + 26 + len(lines) * 22 + 16 + 22 + pad - 6

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        STYLE,
        # Full card has clean rx=8 on all 4 corners
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>',
        f'<path d="{REPO_ICON}" fill="{DIM}" transform="translate({pad},{pad + 3}) scale(1.1)"/>',
        f'<text x="{pad + 26}" y="{pad + 16}" font-family="{SANS}" font-size="16" '
        f'font-weight="600" fill="#58a6ff">{escape(repo)}</text>',
    ]

    # Award badge if present (e.g. FusioniX winner)
    if award_badge:
        aw_text, aw_fg, aw_bg, aw_bdr = award_badge
        aw_w = round(len(aw_text) * 6.5 + 18)
        p.append(
            f'<rect x="{w - pad - 48 - aw_w - 8}" y="{pad + 1}" width="{aw_w}" height="20" rx="4" '
            f'fill="{aw_bg}" stroke="{aw_bdr}" stroke-width="0.8"/>'
        )
        p.append(
            f'<text x="{w - pad - 48 - aw_w - 8 + aw_w / 2}" y="{pad + 14.5}" font-family="{MONO}" '
            f'font-size="10.5" font-weight="600" fill="{aw_fg}" text-anchor="middle">{escape(aw_text)}</text>'
        )

    # Clean Public Pill
    p.append(
        f'<rect x="{w - pad - 48}" y="{pad + 1}" width="48" height="20" rx="4" fill="#161b22" stroke="{BORDER}" stroke-width="0.8"/>'
    )
    p.append(
        f'<text x="{w - pad - 24}" y="{pad + 14.5}" font-family="{MONO}" font-size="11" '
        f'fill="{DIM}" text-anchor="middle">Public</text>'
    )

    y = pad + 26 + 21
    for line in lines:
        p.append(f'<text x="{pad}" y="{y}" font-family="{SANS}" font-size="13.5" fill="{DIM}">{escape(line)}</text>')
        y += 21
    y += 8

    # Language dot + name
    p.append(f'<circle cx="{pad + 6}" cy="{y - 4}" r="5.5" fill="{lang[1]}"/>')
    p.append(f'<text x="{pad + 18}" y="{y}" font-family="{SANS}" font-size="13" font-weight="500" fill="{INK}">{lang[0]}</text>')

    # Meta Tags rendered as clean, low-contrast slate pills
    mx = pad + 18 + len(lang[0]) * 7.6 + 20
    for m in meta:
        mw = round(len(m) * 6.6 + 14)
        p.append(
            f'<rect x="{mx:.0f}" y="{y - 13}" width="{mw}" height="18" rx="3.5" fill="#161b22" stroke="{MUTED_BORDER}" stroke-width="0.8"/>'
        )
        p.append(
            f'<text x="{mx + mw / 2:.0f}" y="{y}" font-family="{MONO}" font-size="10.5" fill="{DIM}" text-anchor="middle">{escape(m)}</text>'
        )
        mx += mw + 8

    p.append("</svg>")
    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote assets/{name}")


def dock_buttons() -> None:
    os.makedirs("assets", exist_ok=True)
    
    # 1. Compact dock-btn-live.svg (Option 2: sleek compact pill button)
    w_live, h = 132, 28
    live_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w_live}" height="{h}" viewBox="0 0 {w_live} {h}">\n'
        f'<rect x="0.5" y="0.5" width="{w_live - 1}" height="{h - 1}" rx="6" fill="#161b22" stroke="{BORDER}" stroke-width="0.8"/>\n'
        f'<g transform="translate(14, 6)">\n'
        f'  <path d="{EXTERNAL_LINK_ICON}" fill="#58a6ff"/>\n'
        f'  <text x="22" y="11.5" font-family="{SANS}" font-size="12" font-weight="600" fill="#58a6ff">Live demo ↗</text>\n'
        f'</g>\n</svg>'
    )
    with open("assets/dock-btn-live.svg", "w", encoding="utf-8") as f:
        f.write(live_svg)
    print("wrote assets/dock-btn-live.svg (compact pill)")

    # 2. Compact dock-btn-arch.svg
    w_arch = 142
    arch_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w_arch}" height="{h}" viewBox="0 0 {w_arch} {h}">\n'
        f'<rect x="0.5" y="0.5" width="{w_arch - 1}" height="{h - 1}" rx="6" fill="#161b22" stroke="{BORDER}" stroke-width="0.8"/>\n'
        f'<g transform="translate(14, 6)">\n'
        f'  <path d="{LAYERS_ICON}" fill="none" stroke="#58a6ff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>\n'
        f'  <text x="22" y="11.5" font-family="{SANS}" font-size="12" font-weight="600" fill="#58a6ff">Architecture ↗</text>\n'
        f'</g>\n</svg>'
    )
    with open("assets/dock-btn-arch.svg", "w", encoding="utf-8") as f:
        f.write(arch_svg)
    print("wrote assets/dock-btn-arch.svg (compact pill)")


if __name__ == "__main__":
    for r in REPOS:
        repo_card(*r)
    dock_buttons()
