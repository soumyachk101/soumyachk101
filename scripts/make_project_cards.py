"""Cinematic project cards — 'Noir · Gold & Crimson' theme.
Every card is a 'frame': warm-black rounded canvas, a crimson->gold left keyline,
champagne-gold repo name, a slow top sheen, faint outline tags. Award pills in crimson.
Language dots are muted/desaturated so they never read as neon. No green.
"""

import os
import textwrap
from html import escape

from theme import PAL, MONO, SANS, P

# Muted, desaturated language accents (readable on noir, non-neon)
LANG_DOT = {
    "Swift": "#c98a5e",
    "TypeScript": "#6b7f9c",
    "Python": "#b08a5e",
    "Rust": "#c9705a",
    "Go": "#6b7f9c",
}


def _dot(lang):
    return LANG_DOT.get(lang, P("steel"))


REPOS = [
    (
        "card-ensembyte.svg",
        "soumyachk101/Ensembyte",
        "Open-source multi-agent coding client. macOS runs Hydra delegating to up to ∞ parallel heads in isolated worktrees; Windows and Linux run on GPUI with CRDT sync.",
        "Swift",
        ["Swift ∞ Hydra", "GPUI", "Loro CRDT"],
        None,
    ),
    (
        "card-veylqorix.svg",
        "soumyachk101/Veylqorix",
        "Code-security and quality gate platform. Orchestrates real scanners, normalizes findings into one schema, and enforces deterministic gate decisions with a standalone Rust security engine.",
        "TypeScript",
        ["Security Gate", "Rust Engine", "Scanner Suite"],
        None,
    ),
    (
        "card-vercode.svg",
        "soumyachk101/VERCODE",
        "AI-powered code review SaaS for GitHub PRs. Deterministic static analysis (ESLint, Semgrep, secrets) runs first, then task-routed LLM reasoning with inline findings and a team dashboard.",
        "TypeScript",
        ["AI Code Review", "Static Analysis", "Monorepo"],
        None,
    ),
    (
        "card-credow.svg",
        "soumyachk101/Credow",
        "Corporate credit allocation on Algorand. Allowances are claimed through x402 payments; unclaimed credits earn yield in an on-chain vault. FusioniX'26 winner.",
        "TypeScript",
        ["Algorand", "x402 Protocol", "FusioniX'26"],
        "FusioniX'26 WINNER",
    ),
    (
        "card-drishtinet.svg",
        "soumyachk101/DrishtiNet",
        "Maps a network as a graph of real attack paths and ranks vulnerable nodes by financial impact instead of CVSS alone. Graph-based risk prioritization engine.",
        "Python",
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


def defs():
    return (
        "<defs>"
        '<linearGradient id="gBase" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{P("base2")}"/><stop offset="1" stop-color="{P("base")}"/>'
        "</linearGradient>"
        '<linearGradient id="gKeyline" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{P("crim")}"/><stop offset="0.55" stop-color="{P("gold")}"/>'
        f'<stop offset="1" stop-color="{P("gold_lo")}"/></linearGradient>'
        '<linearGradient id="gSheen" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{P("gold_hi")}" stop-opacity="0"/>'
        f'<stop offset="0.5" stop-color="{P("gold_hi")}" stop-opacity="0.35"/>'
        f'<stop offset="1" stop-color="{P("gold_hi")}" stop-opacity="0"/></linearGradient>'
        "</defs>"
    )


def repo_card(name, repo, desc, lang, meta, award=None) -> None:
    w, pad = 860, 26
    lines = textwrap.wrap(desc, int((w - 2 * pad) / (14 * 0.55)))
    h = 26 + 20 + len(lines) * 22 + 18 + 26
    head = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        + "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}</style>\n"
        + defs()
    )

    p = [head]
    # canvas + left keyline
    p.append(f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="url(#gBase)" stroke="{P("border")}" stroke-width="1"/>')
    p.append(f'<rect x="0.5" y="8.5" width="3.5" height="{h - 17}" fill="url(#gKeyline)"/>')

    # top hairline + slow sheen
    p.append(f'<line x1="12" y1="10.5" x2="{w - 12}" y2="10.5" stroke="{P("hair")}" stroke-width="1"/>')
    p.append(
        f'<g><rect x="-220" y="10" width="220" height="1.4" fill="url(#gSheen)">'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{w + 40} 0" '
        f'dur="5.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1"/></rect></g>'
    )

    # repo row
    ry = 34
    p.append(f'<path d="{REPO_ICON}" fill="{P("dim")}" transform="translate({pad},{ry - 12}) scale(1.05)"/>')
    p.append(
        f'<text x="{pad + 28}" y="{ry}" font-family="{SANS}" font-size="17" font-weight="700" '
        f'fill="{P("text")}"><tspan fill="{P("dim")}">soumyachk101/</tspan><tspan fill="{P("gold_hi")}">{escape(repo.split("/")[1])}</tspan></text>'
    )
    # Public pill
    p.append(
        f'<rect x="{w - pad - 66}" y="{ry - 13}" width="66" height="20" rx="5" fill="{P("surface")}" stroke="{P("border")}" stroke-width="0.8"/>'
    )
    p.append(
        f'<text x="{w - pad - 33}" y="{ry}" font-family="{MONO}" font-size="10.5" fill="{P("dim")}" text-anchor="middle">Public</text>'
    )

    # award (crimson pill, upper-right under Public)
    if award:
        aw_w = round(len(award) * 6.2 + 22)
        ax = w - pad - aw_w
        p.append(
            f'<g><rect x="{ax}" y="{ry - 24}" width="{aw_w}" height="19" rx="5" fill="none" stroke="{P("crim")}" stroke-width="1"/>'
            f'<circle cx="{ax + 11}" cy="{ry - 14.5}" r="2.5" fill="{P("gold")}"/>'
            f'<text x="{ax + 20}" y="{ry - 10.5}" font-family="{MONO}" font-size="10" font-weight="600" '
            f'letter-spacing="0.6" fill="{P("crim_hi")}">{escape(award)}</text></g>'
        )

    # description
    y = ry + 22
    for line in lines:
        p.append(f'<text x="{pad}" y="{y}" font-family="{SANS}" font-size="13.5" fill="{P("dim")}">{escape(line)}</text>')
        y += 21
    y += 8

    # language + tags
    p.append(f'<circle cx="{pad + 6}" cy="{y - 4}" r="5" fill="{_dot(lang)}"/>')
    p.append(f'<text x="{pad + 18}" y="{y}" font-family="{SANS}" font-size="13" font-weight="500" fill="{P("text")}">{lang}</text>')

    mx = pad + 18 + len(lang) * 7.6 + 22
    for m in meta:
        mw = round(len(m) * 6.6 + 16)
        p.append(
            f'<rect x="{mx:.0f}" y="{y - 13}" width="{mw}" height="18" rx="4" fill="{P("surface")}" stroke="{P("hair")}" stroke-width="0.8"/>'
            f'<text x="{mx + mw / 2:.0f}" y="{y}" font-family="{MONO}" font-size="10.5" fill="{P("dim")}" text-anchor="middle">{escape(m)}</text>'
        )
        mx += mw + 9

    p.append("</svg>")
    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote assets/{name}")


if __name__ == "__main__":
    for r in REPOS:
        repo_card(*r)
    print("project cards regenerated (noir · gold & crimson)")
