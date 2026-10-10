"""Hand-author the animated htop-style Agent Process Monitor SVG.

Visualizes running agent systems, parallel worktrees, and memory engine
in an authentic terminal htop layout.

    python scripts/make_agent_monitor.py            # agent-monitor.svg
    STATIC=1 python scripts/make_agent_monitor.py   # frozen frame
"""

import os
from html import escape

BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"
CYAN = "#58a6ff"
YELLOW = "#d29922"
PURPLE = "#bc8cff"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 12.5
LH = 21.0
PAD_X = 22.0
BAR_H = 30.0
W = 860
TITLE = "soumyachk101@github: ~/htop (agent runtimes)"

PROCESSES = [
    ("101", "SwarmAI", "Rust / Tauri v2", "Parallel worktree agent IDE", "[ACTIVE]", ACCENT),
    ("102", "Orbit", "Rust Engine", "Lightweight agent orchestrator", "[SYNCING]", CYAN),
    ("103", "Ensembyte", "Swift 6 / GPUI", "Hydra 8-head CRDT client", "[RUNNING]", PURPLE),
    ("104", "Credow", "Algorand x402", "Corporate credit vault v1", "[DEPLOYED]", YELLOW),
    ("105", "DrishtiNet", "Python / Graph", "Attack-path dollar risk engine", "[ONLINE]", ACCENT),
]


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    # header + 2 gauge lines + separator + col header + 5 procs + footer
    H = round(BAR_H + 14 + 10 * LH + 18)

    op = "1" if static else "0"

    def anim(delay: float) -> str:
        if static:
            return ""
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{delay:.2f}s" dur="0.4s" fill="freeze"/>'
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>',
        # terminal title bar
        f'<path d="M1 9 a8 8 0 0 1 8-8 h{W - 18} a8 8 0 0 1 8 8 v{BAR_H - 9} h-{W - 2} z" fill="{BAR}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{BORDER}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="5" fill="#f85149"/>',
        f'<circle cx="38" cy="{BAR_H / 2}" r="5" fill="#d29922"/>',
        f'<circle cx="56" cy="{BAR_H / 2}" r="5" fill="{ACCENT}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + FS * 0.36}" fill="{DIM}" font-family="{FONT}" '
        f'font-size="{FS - 1.5}" text-anchor="middle">{escape(TITLE)}</text>',
        f'<g font-family="{FONT}" font-size="{FS}" xml:space="preserve">',
    ]

    y = BAR_H + 16 + LH * 0.7

    # Gauge row 1: CPU & Load
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="{PAD_X}" y="{y:.1f}">'
        f'<tspan fill="{DIM}">CPU [</tspan>'
        f'<tspan fill="{ACCENT}">||||||||||||||||||||||||||||░░░░░░░░░░</tspan>'
        f'<tspan fill="{DIM}">] </tspan>'
        f'<tspan fill="{INK}">74.2%</tspan>'
        f'<tspan fill="{DIM}">       Tasks: </tspan><tspan fill="{ACCENT}">5 running</tspan><tspan fill="{DIM}">, 0 stopped · Uptime: 192d</tspan>'
        f'</text>{anim(0.15)}</g>'
    )
    y += LH

    # Gauge row 2: MEM (Pheromone layer)
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="{PAD_X}" y="{y:.1f}">'
        f'<tspan fill="{DIM}">MEM [</tspan>'
        f'<tspan fill="{CYAN}">||||||||||||||||||||░░░░░░░░░░░░░░░░░░</tspan>'
        f'<tspan fill="{DIM}">] </tspan>'
        f'<tspan fill="{INK}">52.8%</tspan>'
        f'<tspan fill="{DIM}">       Layer: </tspan><tspan fill="{PURPLE}">Pheromone (BM25 + dense n-grams)</tspan>'
        f'</text>{anim(0.25)}</g>'
    )
    y += LH * 1.1

    # Separator line
    parts.append(
        f'<line x1="{PAD_X}" y1="{y - 6:.1f}" x2="{W - PAD_X}" y2="{y - 6:.1f}" '
        f'stroke="{BORDER}" stroke-dasharray="3 3" stroke-width="1"/>'
    )

    # Column header
    parts.append(
        f'<g opacity="{op}">'
        f'<rect x="{PAD_X - 4}" y="{y - 12:.1f}" width="{W - 2 * PAD_X + 8}" height="{LH - 2}" '
        f'fill="{BAR}" rx="3"/>'
        f'<text x="{PAD_X}" y="{y + 2:.1f}">'
        f'<tspan fill="{DIM}" font-weight="bold">PID   AGENT / SYSTEM     RUNTIME          CORE ENGINE ARCHITECTURE           STATUS</tspan>'
        f'</text>{anim(0.35)}</g>'
    )
    y += LH + 4

    # Process rows
    for i, (pid, agent, runtime, engine, status, color) in enumerate(PROCESSES):
        pid_pad = pid.ljust(6)
        agent_pad = agent.ljust(19)
        rt_pad = runtime.ljust(17)
        eng_pad = engine.ljust(35)
        delay = 0.45 + i * 0.12
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}">'
            f'<tspan fill="{DIM}">{escape(pid_pad)}</tspan>'
            f'<tspan fill="{color}" font-weight="bold">{escape(agent_pad)}</tspan>'
            f'<tspan fill="{INK}">{escape(rt_pad)}</tspan>'
            f'<tspan fill="{DIM}">{escape(eng_pad)}</tspan>'
            f'<tspan fill="{color}" font-weight="bold">{escape(status)}</tspan>'
            f'</text>{anim(delay)}</g>'
        )
        y += LH

    # Footer note
    y += 2
    parts.append(
        f'<text x="{PAD_X}" y="{y:.1f}" fill="{DIM}" font-size="{FS - 1.5}">'
        f'<tspan fill="{ACCENT}">F1</tspan>Help  '
        f'<tspan fill="{ACCENT}">F2</tspan>Setup  '
        f'<tspan fill="{ACCENT}">F3</tspan>Search  '
        f'<tspan fill="{ACCENT}">F9</tspan>Kill  '
        f'<tspan fill="{ACCENT}">F10</tspan>Quit · Local-first multi-agent parallel environments'
        f'</text>'
    )

    parts.append("</g></svg>")

    with open("agent-monitor.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote agent-monitor.svg ({W}x{H}, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
