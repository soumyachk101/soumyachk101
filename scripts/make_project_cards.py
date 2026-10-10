"""Generate pinned-repository style project cards with seamlessly docked action bars.

Cards replicate the look of GitHub's pinned repos, in the shared terminal dark palette.
Each card has an integrated bottom action shelf divided into:
- Left: Live demo / Architecture
- Right: GitHub repo
"""

import os
import textwrap
from html import escape

BG = "#0d1117"
BORDER = "#30363d"
DIM = "#8b949e"
SANS = "-apple-system, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

STYLE = ""

REPOS = [
    (
        "card-ensembyte.svg",
        "soumyachk101/Ensembyte",
        "Open-source multi-agent coding client. macOS runs Hydra delegating to up to ∞ parallel heads in isolated worktrees; Windows and Linux run on GPUI with CRDT sync.",
        ("Swift", "#f05138"),
        ["Swift ∞ Hydra", "GPUI", "Loro CRDT"],
    ),
    (
        "card-orbit.svg",
        "soumyachk101/Orbit-Code",
        "Drives your coding agents (Claude, Cursor, Codex, Devin, Grok, Hermes) from a lightweight engine on each device. Local-only by default with optional VPS & device sync.",
        ("Rust", "#dea584"),
        ["Agent Engine", "Local-First", "Zero Telemetry"],
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
    (
        "card-swarmai.svg",
        "soumyachk101/SwarmAI",
        "Local-first desktop IDE for running coding agents in parallel with shared project memory. Tasks dispatch across Git worktrees with dynamic file locks. Pheromone memory layer combines BM25 and dense retrieval.",
        ("Rust", "#dea584"),
        ["Tauri v2", "React", "SQLite"],
    ),
]

REPO_ICON = (
    "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75"
    "v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708"
    "A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2"
    "l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"
)

OCTOCAT_ICON = (
    "M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 "
    "1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-"
    ".68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 "
    "3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 "
    "1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"
)

EXTERNAL_LINK_ICON = (
    "M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a1.25 1.25 0 0 0-1.25 1.25v7.5c0 .69.56 1.25 1.25 1.25h7.5c.69 0 1.25-.56 1.25-1.25"
    "v-3.5a.75.75 0 0 1 1.5 0v3.5A2.75 2.75 0 0 1 11.25 15h-7.5A2.75 2.75 0 0 1 1 12.25v-7.5A2.75 2.75 0 0 1 3.75 2Zm7.5 1.5"
    "H8.75a.75.75 0 0 1 0-1.5h4.5c.414 0 .75.336.75.75v4.5a.75.75 0 0 1-1.5 0V4.56L7.53 9.53a.75.75 0 0 1-1.06-1.06l4.97-4.97h-.19Z"
)

LAYERS_ICON = (
    "M1.5 4.5 8 1l6.5 3.5L8 8 1.5 4.5Zm0 4.25L8 12.25l6.5-3.5m-13 4.25L8 16.5l6.5-3.5"
)


def repo_card(name, repo, desc, lang, meta) -> None:
    w, pad = 640, 24
    lines = textwrap.wrap(desc, int((w - 2 * pad) / (14 * 0.55)))
    h = pad + 26 + len(lines) * 22 + 16 + 22 + pad - 6
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        STYLE,
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{BORDER}"/>',
        '<g>',
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
    mx = pad + 18 + len(lang[0]) * 7.6 + 24
    for m in meta:
        p.append(f'<text x="{mx:.0f}" y="{y}" font-family="{SANS}" font-size="13" fill="{DIM}">{escape(m)}</text>')
        mx += len(m) * 7.4 + 24
    p.append("</g></svg>")
    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote assets/{name}")


def dock_buttons() -> None:
    os.makedirs("assets", exist_ok=True)
    w, h = 150, 34

    # 1. dock-btn-live.svg (Left)
    live_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="#161b22" stroke="{BORDER}"/>\n'
        f'  <g transform="translate(0, 9)">\n'
        f'    <path d="{EXTERNAL_LINK_ICON}" fill="#58a6ff" transform="translate(25, 0)"/>\n'
        f'    <text x="47" y="12" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#58a6ff">Live demo ↗</text>\n'
        f'  </g>\n'
        f'</svg>'
    )
    with open("assets/dock-btn-live.svg", "w", encoding="utf-8") as f:
        f.write(live_svg)
    print("wrote assets/dock-btn-live.svg")

    # 2. dock-btn-arch.svg (Left)
    arch_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="#161b22" stroke="{BORDER}"/>\n'
        f'  <g transform="translate(0, 9)">\n'
        f'    <path d="{LAYERS_ICON}" fill="none" stroke="#58a6ff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" transform="translate(15, 0)"/>\n'
        f'    <text x="38" y="12" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#58a6ff">Architecture ↗</text>\n'
        f'  </g>\n'
        f'</svg>'
    )
    with open("assets/dock-btn-arch.svg", "w", encoding="utf-8") as f:
        f.write(arch_svg)
    print("wrote assets/dock-btn-arch.svg")

    # 3. dock-btn-repo.svg (Right)
    repo_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="#161b22" stroke="{BORDER}"/>\n'
        f'  <g transform="translate(0, 9)">\n'
        f'    <path d="{OCTOCAT_ICON}" fill="#c9d1d9" transform="translate(24, 0)"/>\n'
        f'    <text x="47" y="12" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#c9d1d9">GitHub repo</text>\n'
        f'  </g>\n'
        f'</svg>'
    )
    with open("assets/dock-btn-repo.svg", "w", encoding="utf-8") as f:
        f.write(repo_svg)
    print("wrote assets/dock-btn-repo.svg")


if __name__ == "__main__":
    for r in REPOS:
        repo_card(*r)
    dock_buttons()
