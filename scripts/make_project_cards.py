"""Generate pinned-repository style project cards and their link buttons.

Cards replicate the look of GitHub's pinned repos, in the shared terminal dark palette.
Rerun when a project's description or tech changes:

    python scripts/make_project_cards.py
"""

import os
import textwrap
from html import escape

BG = "#0d1117"
BORDER = "#30363d"
DIM = "#8b949e"
SANS = "-apple-system, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

STYLE = (
    "<style>.a{animation:a .7s ease-out both}"
    "@keyframes a{from{opacity:0}to{opacity:1}}</style>"
)

REPOS = [
    (
        "card-swarmai.svg",
        "soumyachk101/SwarmAI",
        "Local-first desktop IDE for running coding agents in parallel with shared project memory. Tasks dispatch across Git worktrees with dynamic file locks. Pheromone memory layer combines BM25 and dense retrieval.",
        ("Rust", "#dea584"),
        ["Tauri v2", "React", "SQLite"],
    ),
    (
        "card-orbit.svg",
        "soumyachk101/Orbit-Code",
        "Drives your coding agents (Claude, Cursor, Codex, Devin, Grok, Hermes) from a lightweight engine on each device. Local-only by default with optional VPS & device sync.",
        ("Rust", "#dea584"),
        ["Agent Engine", "Local-First", "Zero Telemetry"],
    ),
    (
        "card-ensembyte.svg",
        "soumyachk101/Ensembyte",
        "Open-source multi-agent coding client. macOS runs Hydra delegating to up to 8 parallel heads in isolated worktrees; Windows and Linux run on GPUI with CRDT sync.",
        ("Swift", "#f05138"),
        ["Swift 6", "GPUI", "Loro CRDT"],
    ),
    (
        "card-credow.svg",
        "soumyachk101/Credow",
        "Corporate credit allocation on Algorand. Allowances are claimed through x402 payments, and unclaimed credits earn yield in an on-chain vault. FusioniX'26 winner.",
        ("TypeScript", "#3178c6"),
        ["Algorand", "x402 Protocol", "FusioniX'26"],
    ),
    (
        "card-drishtinet.svg",
        "soumyachk101/DrishtiNet",
        "Maps a network as a graph of real attack paths and ranks vulnerable nodes by financial impact instead of CVSS alone. Graph-based risk prioritization engine.",
        ("Python", "#3572a5"),
        ["Cybersecurity", "Graph Analysis", "Innofusion 3.0"],
    ),
]

REPO_ICON = (
    "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75"
    "v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708"
    "A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2"
    "l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"
)

PILLS = [
    ("live", "Live demo ↗"),
    ("site", "Live site ↗"),
    ("github", "GitHub repo"),
    ("demo", "Watch demo ↗"),
]


def repo_card(name, repo, desc, lang, meta) -> None:
    w, pad = 640, 24
    lines = textwrap.wrap(desc, int((w - 2 * pad) / (14 * 0.55)))
    h = pad + 26 + len(lines) * 22 + 16 + 22 + pad - 6
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        STYLE,
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{BORDER}"/>',
        '<g class="a" style="animation-delay:0.10s">',
        f'<path d="{REPO_ICON}" fill="{DIM}" transform="translate({pad},{pad + 3}) scale(1.1)"/>',
        f'<text x="{pad + 26}" y="{pad + 16}" font-family="{SANS}" font-size="17" '
        f'font-weight="600" fill="#58a6ff">{escape(repo)}</text>',
        f'<rect x="{w - pad - 52}" y="{pad + 1}" width="52" height="22" rx="11" fill="none" stroke="{BORDER}"/>',
        f'<text x="{w - pad - 26}" y="{pad + 16}" font-family="{SANS}" font-size="12" '
        f'font-weight="500" fill="{DIM}" text-anchor="middle">Public</text>',
    ]
    y = pad + 26 + 22
    for line in lines:
        p.append(f'<text x="{pad}" y="{y}" font-family="{SANS}" font-size="14" fill="{DIM}">{escape(line)}</text>')
        y += 22
    y += 8
    p.append(f'<circle cx="{pad + 6}" cy="{y - 4}" r="6" fill="{lang[1]}"/>')
    p.append(f'<text x="{pad + 18}" y="{y}" font-family="{SANS}" font-size="13" fill="{DIM}">{lang[0]}</text>')
    mx = pad + 18 + len(lang[0]) * 7.6 + 20
    # Star icon & star count
    p.append(f'<path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.75.75 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z" fill="{DIM}" transform="translate({mx:.0f},{y - 12}) scale(0.95)"/>')
    p.append(f'<text x="{mx + 18:.0f}" y="{y}" font-family="{SANS}" font-size="13" fill="{DIM}">0</text>')
    mx += 44
    for m in meta:
        p.append(f'<text x="{mx:.0f}" y="{y}" font-family="{SANS}" font-size="13" fill="{DIM}">{escape(m)}</text>')
        mx += len(m) * 7.4 + 20
    p.append("</g></svg>")
    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote assets/{name}")


def pills() -> None:
    os.makedirs("badges", exist_ok=True)
    h = 34
    for name, label in PILLS:
        w = round(len(label) * 7.7 + 34)
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="#21262d" stroke="#363b42"/>'
            f'<text x="{w / 2}" y="{h / 2 + 5}" font-family="{SANS}" font-size="14" font-weight="500" '
            f'fill="#e6edf3" text-anchor="middle">{escape(label)}</text></svg>'
        )
        with open(f"badges/{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"wrote badges/{name}.svg")


if __name__ == "__main__":
    for r in REPOS:
        repo_card(*r)
    pills()
