"""Render the GitHub contribution calendar as a platformer level, with repos as high scores.

Usage: GITHUB_TOKEN=... python3 build.py <username> <output.svg>
Uses only the standard library. Exits non-zero on any API problem so a failed
run never overwrites the last good image.
"""
import base64
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.request

USER, OUT = sys.argv[1], sys.argv[2]
HERE = pathlib.Path(__file__).parent

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount contributionLevel } }
      }
      commitContributionsByRepository(maxRepositories: 25) {
        repository { name owner { login } isPrivate }
        contributions { totalCount }
      }
    }
  }
}
"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={
            "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}",
            "Content-Type": "application/json",
            "User-Agent": "arcade-contrib",
        },
    )
    body = json.load(urllib.request.urlopen(req, timeout=30))
    if body.get("errors") or not body.get("data", {}).get("user"):
        raise SystemExit(f"GraphQL error: {body.get('errors')}")
    return body["data"]["user"]["contributionsCollection"]


data = fetch()
cal = data["contributionCalendar"]
weeks = [w["contributionDays"] for w in cal["weeks"]]
days = [d for w in weeks for d in w]
total = cal["totalContributions"]

# ---- stats -----------------------------------------------------------------
best_day = max(days, key=lambda d: d["contributionCount"])
longest = run = 0
for d in days:
    run = run + 1 if d["contributionCount"] else 0
    longest = max(longest, run)
current = 0
for i, d in enumerate(reversed(days)):
    if d["contributionCount"]:
        current += 1
    elif i == 0:
        continue  # today may simply not have activity yet
    else:
        break

scores = {}
for r in data["commitContributionsByRepository"]:
    repo = r["repository"]
    if repo["isPrivate"] or repo["name"] == USER:
        continue
    scores[repo["name"]] = scores.get(repo["name"], 0) + r["contributions"]["totalCount"]
high = sorted(scores.items(), key=lambda kv: -kv[1])[:3]
if not high:
    raise SystemExit("no repository scores returned")

# ---- layout ----------------------------------------------------------------
W = 960
CELL, GAP = 13, 3
STEP = CELL + GAP
GRID_W = len(weeks) * STEP - GAP
GX = (W - GRID_W) // 2
GY = 150
GRID_H = 7 * STEP - GAP
MAX_STACK = max(3, max(sum(d["contributionLevel"] in ("FIRST_QUARTILE", "SECOND_QUARTILE", "THIRD_QUARTILE", "FOURTH_QUARTILE") for d in w) for w in weeks))
FLOOR_Y = GY + MAX_STACK * STEP + 40
HS_Y = FLOOR_Y + 86
ROW = 34
H = HS_Y + 40 + len(high) * ROW + 70

C = {
    "bg": "#05060f", "frame": "#1b1f3b", "text": "#e6edf3", "dim": "#4b5578",
    "cyan": "#3ee6ff", "pink": "#ff3ea5", "gold": "#ffd23e", "green": "#5dff8a",
}
LEVEL = {
    "FIRST_QUARTILE": ("#123a73", None),
    "SECOND_QUARTILE": ("#1f6feb", None),
    "THIRD_QUARTILE": ("#3ee6ff", None),
    "FOURTH_QUARTILE": ("#ffd23e", "gem"),
}

font = base64.b64encode((HERE / "PressStart2P-subset.woff").read_bytes()).decode()


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=12, fill=C["text"], anchor="start", cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{c}>{esc(s)}</text>')


out = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contribution graph as an arcade level: {total} contributions this year">
<defs>
<style>
@font-face{{font-family:'PS2P';src:url(data:font/woff;base64,{font}) format('woff');}}
text{{font-family:'PS2P',monospace;}}
.blink{{animation:blink 1.1s steps(1) infinite;}}
.gem{{animation:shine 2.4s ease-in-out infinite;}}
.fa{{animation:fa .32s steps(1) infinite;}}
.fb{{animation:fb .32s steps(1) infinite;}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes shine{{0%,100%{{opacity:1}}50%{{opacity:.55}}}}
@keyframes fa{{0%{{opacity:1}}50%{{opacity:0}}}}
@keyframes fb{{0%{{opacity:0}}50%{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.blink,.gem,.fa{{animation:none}}.fb{{display:none}}}}
</style>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity=".28"/></pattern>
<radialGradient id="glow" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#101736"/><stop offset="1" stop-color="{C['bg']}"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" rx="22" fill="{C['frame']}"/>
<rect x="10" y="10" width="{W-20}" height="{H-20}" rx="16" fill="url(#glow)" stroke="#2c3366" stroke-width="2"/>''']

# HUD
hud_y = 52
out += [
    text(GX, hud_y, "1UP", 12, C["pink"], cls="blink"),
    text(GX, hud_y + 24, f"{total:06d}", 16, C["text"]),
    text(W // 2, hud_y, "HI-SCORE DAY", 12, C["pink"], "middle"),
    text(W // 2, hud_y + 24, f"{best_day['contributionCount']:06d}", 16, C["gold"], "middle"),
    text(GX + GRID_W, hud_y, "STREAK", 12, C["pink"], "end"),
    text(GX + GRID_W, hud_y + 24, f"{current:02d} / BEST {longest:02d}", 16, C["text"], "end"),
]

start = dt.date.fromisoformat(days[0]["date"])
end = dt.date.fromisoformat(days[-1]["date"])
out.append(text(W // 2, GY - 34, f"LEVEL {end.year}  •  {start:%b %Y} → {end:%b %Y}".upper(), 10, C["cyan"], "middle"))

# month markers
last_month = None
for wi, w in enumerate(weeks):
    m = dt.date.fromisoformat(w[0]["date"]).month
    if m != last_month and wi < len(weeks) - 2:
        if last_month is not None or w[0]["date"][-2:] <= "07":
            out.append(text(GX + wi * STEP, GY - 10, dt.date(2000, m, 1).strftime("%b").upper(), 8, C["dim"]))
        last_month = m

# level: each week's contributed days fall into a stack of blocks
order = {"FIRST_QUARTILE": 0, "SECOND_QUARTILE": 1, "THIRD_QUARTILE": 2, "FOURTH_QUARTILE": 3}
heights = []
for wi, w in enumerate(weeks):
    active = sorted((d for d in w if d["contributionLevel"] in LEVEL),
                    key=lambda d: (order[d["contributionLevel"]], d["contributionCount"]))
    heights.append(len(active))
    x = GX + wi * STEP
    for i, d in enumerate(active):
        y = FLOOR_Y - CELL - i * STEP
        color, kind = LEVEL[d["contributionLevel"]]
        tip = f"<title>{d['date']}: {d['contributionCount']} contributions</title>"
        if kind == "gem":
            cx, cy = x + CELL / 2, y + CELL / 2
            out.append(
                f'<g class="gem"><rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{color}" opacity=".22"/>'
                f'<path d="M{cx} {y+1} L{x+CELL-1} {cy} L{cx} {y+CELL-1} L{x+1} {cy}Z" fill="{color}"/>'
                f'<rect x="{cx-1.5}" y="{cy-3.5}" width="2" height="2" fill="#fff"/>{tip}</g>')
        else:
            out.append(
                f'<g><rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{color}"/>'
                f'<rect x="{x}" y="{y}" width="{CELL}" height="2" fill="#fff" opacity=".3"/>'
                f'<rect x="{x}" y="{y+CELL-2}" width="{CELL}" height="2" fill="#000" opacity=".3"/>'
                f'<rect x="{x+CELL-2}" y="{y}" width="2" height="{CELL}" fill="#000" opacity=".2"/>{tip}</g>')

# ground
for i in range(0, GRID_W + 8, 16):
    out.append(f'<rect x="{GX-4+i}" y="{FLOOR_Y}" width="15" height="7" fill="#2a1f55"/>'
               f'<rect x="{GX-4+i}" y="{FLOOR_Y}" width="15" height="2" fill="{C["pink"]}" opacity=".85"/>')
for i in range(0, GRID_W + 8, 16):
    out.append(f'<rect x="{GX+4+i}" y="{FLOOR_Y+9}" width="15" height="7" fill="#1d1640"/>')

# today marker
tx = GX + (len(weeks) - 1) * STEP + CELL / 2
out.append(text(tx, FLOOR_Y + 34, "TODAY", 7, C["dim"], "middle"))

# runner path: walk across the tops of the stacks, jumping between heights
def surface(h):
    return FLOOR_Y - h * STEP + (GAP if h else 0)

centers = [GX + wi * STEP + CELL / 2 for wi in range(len(weeks))]
path = [f"M{GX - 4} {surface(heights[0])}"]
for wi in range(len(weeks)):
    xc, y = centers[wi], surface(heights[wi])
    if wi == 0 or heights[wi] == heights[wi - 1]:
        path.append(f"L{xc} {y}")
    else:
        yp = surface(heights[wi - 1])
        peak = min(y, yp) - 24
        path.append(f"Q{(centers[wi - 1] + xc) / 2} {peak} {xc} {y}")
path.append(f"L{GX + GRID_W + 4} {surface(heights[-1])}")
path_d = " ".join(path)

robot_a = [
    "....#....",
    "..#####..",
    ".#ccccc#.",
    ".#ckcck#.",
    ".#ccccc#.",
    "..#####..",
    ".#ppppp#.",
    "#.ppppp.#",
    "..ppppp..",
    "..#...#..",
    ".##...##.",
]
robot_b = robot_a[:9] + ["...#.#...", "..##.##.."]
px = 2


def sprite(rows, cls):
    cells = []
    w, h = len(rows[0]) * px, len(rows) * px
    for r, line in enumerate(rows):
        for c, ch in enumerate(line):
            if ch != ".":
                col = {"#": C["text"], "c": C["cyan"], "k": C["bg"], "p": C["pink"]}[ch]
                cells.append(f'<rect x="{c*px - w/2}" y="{r*px - h}" width="{px}" height="{px}" fill="{col}"/>')
    return f'<g class="{cls}">{"".join(cells)}</g>'


out.append(f'<path d="{path_d}" fill="none" stroke="{C["cyan"]}" stroke-opacity=".12" stroke-width="1" stroke-dasharray="2 4"/>')
out.append(
    f'<g>{sprite(robot_a, "fa")}{sprite(robot_b, "fb")}'
    f'<animateMotion dur="18s" repeatCount="indefinite" path="{path_d}"/></g>')

# high scores
out.append(text(W // 2, HS_Y, "HIGH SCORES", 16, C["gold"], "middle"))
out.append(text(W // 2, HS_Y + 22, "COMMITS THIS YEAR", 8, C["dim"], "middle"))
rank_colors = [C["gold"], C["cyan"], C["green"], C["pink"], C["text"]]
ranks = ["1ST", "2ND", "3RD", "4TH", "5TH"]
col_rank, col_name, col_score = W // 2 - 300, W // 2 - 210, W // 2 + 300
for i, (name, score) in enumerate(high):
    y = HS_Y + 64 + i * ROW
    col = rank_colors[i]
    label = name.upper()[:20]
    dots_from = col_name + len(label) * 14 + 12
    out.append(text(col_rank, y, ranks[i], 14, col))
    out.append(text(col_name, y, label, 14, col))
    if dots_from < col_score - 110:
        out.append(f'<line x1="{dots_from}" x2="{col_score - 104}" y1="{y-5}" y2="{y-5}" stroke="{C["dim"]}" stroke-width="2" stroke-dasharray="2 8"/>')
    out.append(text(col_score, y, f"{score:06d}", 14, col, "end"))

out.append(text(W // 2, H - 34, "INSERT COIN TO CONTINUE", 10, C["pink"], "middle", "blink"))
out.append(f'<rect x="10" y="10" width="{W-20}" height="{H-20}" rx="16" fill="url(#scan)" pointer-events="none"/>')
out.append("</svg>")

pathlib.Path(OUT).parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(OUT).write_text("\n".join(out))
print(f"wrote {OUT}: {total} contributions, top repo {high[0]}")
