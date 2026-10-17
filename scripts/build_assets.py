#!/usr/bin/env python3
"""
build_assets.py
Generates all terminal, banner, and stats SVGs for Kanaga Abishek's profile repository.
"""
import os
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(exist_ok=True)

def generate_banner():
    banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="100%" height="100%">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3a1c71">
        <animate attributeName="stop-color" values="#3a1c71;#0052D4;#4364F7;#00C9FF;#3a1c71" dur="15s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#4158D0">
        <animate attributeName="stop-color" values="#4158D0;#0093E9;#8EC5FC;#00E8FF;#4158D0" dur="15s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#C850C0">
        <animate attributeName="stop-color" values="#C850C0;#80D0C7;#E0C3FC;#3fb950;#C850C0" dur="15s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="subtle-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#grad1)" rx="16"/>
  
  <!-- Decorative tech grid lines -->
  <path d="M -100 250 Q 250 -50 950 120" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="12" />
  <path d="M -50 280 Q 400 -80 1000 180" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="24" />
  <path d="M 150 250 Q 550 50 1050 220" fill="none" stroke="rgba(0,232,255,0.15)" stroke-width="6" />

  <!-- Monospace Header & Subtitle -->
  <text x="50%" y="44%" dominant-baseline="middle" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="50" font-weight="900" fill="#ffffff" letter-spacing="4" filter="url(#glow)">KANAGA ABISHEK B</text>
  <text x="50%" y="71%" dominant-baseline="middle" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="17" fill="#ffffff" opacity="0.95" font-weight="600" letter-spacing="2.5" filter="url(#subtle-shadow)">DISTRIBUTED SYSTEMS · AGENTIC AI · BACKEND ENGINEER</text>
</svg>
"""
    (ASSETS_DIR / "banner.svg").write_text(banner_svg, encoding="utf-8")
    print("Generated banner.svg")

def generate_typewriter():
    phrases = [
        "Java &amp; Backend Systems Engineer",
        "LeetCode Knight (Rating 1905)",
        "SIH 2025 National Winner (MoD)",
        "500+ Algorithmic Problems Solved",
        "Distributed Tracing &amp; Concurrency",
        "Autonomous Agentic AI (MCP)",
        "Code. Build. Optimize. Scale."
    ]
    # Each char is 14.45px in 24px monospace font
    char_w = 14.45
    total_dur = 25.2
    n = len(phrases)
    step = total_dur / n # 3.6s per phrase
    
    # Calculate widths based on unescaped text length for accurate sizing
    raw_lengths = [len(p.replace("&amp;", "&")) for p in phrases]
    widths = [l * char_w for l in raw_lengths]
    start_x = 175.0
    
    # Build keytimes and values
    clip_vals = []
    cursor_vals = []
    kt_list = []
    
    for i, w in enumerate(widths):
        t0 = (i * step) / total_dur
        t1 = (i * step + 1.2) / total_dur
        t2 = (i * step + 2.6) / total_dur
        t3 = (i * step + 3.4) / total_dur
        
        kt_list.extend([t0, t1, t2, t3])
        clip_vals.extend([0.0, w, w, 0.0])
        cursor_vals.extend([start_x, start_x + w, start_x + w, start_x])
        
    # Append final 1.0000 point
    kt_list.append(1.0)
    clip_vals.append(0.0)
    cursor_vals.append(start_x)
    
    kt_str = ";".join(f"{t:.4f}" for t in kt_list)
    clip_str = ";".join(f"{w:.2f}" for w in clip_vals)
    cursor_str = ";".join(f"{x:.2f}" for x in cursor_vals)
    
    # Build phrase texts
    text_blocks = []
    for i, p in enumerate(phrases):
        t_start = (i * step) / total_dur
        t_end = ((i + 1) * step) / total_dur
        if i == 0:
            anim = f'<animate attributeName="opacity" values="1;0;0" keyTimes="0.0000;{t_end:.4f};1.0000" dur="{total_dur:.3f}s" calcMode="discrete" repeatCount="indefinite" />'
        elif i == n - 1:
            anim = f'<animate attributeName="opacity" values="0;1;1" keyTimes="0.0000;{t_start:.4f};1.0000" dur="{total_dur:.3f}s" calcMode="discrete" repeatCount="indefinite" />'
        else:
            anim = f'<animate attributeName="opacity" values="0;1;0;0" keyTimes="0.0000;{t_start:.4f};{t_end:.4f};1.0000" dur="{total_dur:.3f}s" calcMode="discrete" repeatCount="indefinite" />'
        
        text_blocks.append(f"""  <text x="{start_x}" y="35" class="text" opacity="0">
    {anim}
    {p}
  </text>""")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 50" width="100%" height="50">
<style>
@import url("https://fonts.googleapis.com/css2?family=Fira+Code:wght@600&amp;display=swap");
.text {{ font-family: "Fira Code", monospace; font-size: 24px; fill: #00E5FF; font-weight: 600; }}
.prompt {{ font-family: "Fira Code", monospace; font-size: 24px; fill: #7d8590; font-weight: 600; }}
.cursor {{ fill: #00E5FF; }}
</style>
<rect width="840" height="50" fill="transparent"/>
<text x="145" y="35" class="prompt">&gt;</text>
<clipPath id="type-clip">
  <rect x="{start_x}" y="0" width="0" height="50">
    <animate attributeName="width" values="{clip_str}" keyTimes="{kt_str}" dur="{total_dur:.3f}s" calcMode="linear" repeatCount="indefinite" />
  </rect>
</clipPath>
<g clip-path="url(#type-clip)">
{''.join(text_blocks)}
</g>
<rect x="{start_x}" y="12" width="12" height="28" class="cursor">
  <animate attributeName="x" values="{cursor_str}" keyTimes="{kt_str}" dur="{total_dur:.3f}s" calcMode="linear" repeatCount="indefinite" />
  <animate attributeName="opacity" values="1;0;1;0" keyTimes="0;0.5;0.51;1" dur="0.8s" repeatCount="indefinite" />
</rect>
</svg>
"""
    (ASSETS_DIR / "typewriter.svg").write_text(svg_content, encoding="utf-8")
    print("Generated typewriter.svg")

def generate_portrait():
    portrait_path = BASE_DIR / "portrait.jpeg"
    if not portrait_path.exists():
        portrait_path = ASSETS_DIR / "photos" / "portrait.jpeg"
    
    with open(portrait_path, "rb") as f:
        b64_data = base64.b64encode(f.read()).decode("utf-8")
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="1140" viewBox="0 0 1040 1140" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="neon-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#7928CA"/>
      <stop offset="100%" stop-color="#FF0080"/>
    </linearGradient>
    <filter id="border-glow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="img-rounded">
      <rect x="170" y="80" width="700" height="700" rx="24" />
    </clipPath>
    <clipPath id="portrait-reveal">
      <rect x="170" y="80" width="700" height="0">
        <animate attributeName="height" from="0" to="700" begin="0.2s" dur="1.6s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      </rect>
    </clipPath>
  </defs>

  <!-- Terminal Window Background -->
  <rect width="1040" height="1140" rx="16" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="1039" height="1139" rx="16" fill="none" stroke="#30363d" stroke-width="2"/>
  
  <!-- Terminal Header Bar -->
  <line x1="0" y1="50" x2="1040" y2="50" stroke="#30363d" stroke-width="2"/>
  <circle cx="40" cy="25.0" r="8" fill="#ff5f56"/>
  <circle cx="64" cy="25.0" r="8" fill="#ffbd2e"/>
  <circle cx="88" cy="25.0" r="8" fill="#27c93f"/>
  <text x="520.0" y="31.0" fill="#7d8590" font-size="20" text-anchor="middle">abishek@github: ~$ ./portrait.sh</text>

  <!-- Avatar Outer Glow Border -->
  <rect x="166" y="76" width="708" height="708" rx="28" fill="none" stroke="url(#neon-border)" stroke-width="4" filter="url(#border-glow)"/>

  <!-- Avatar Image with Reveal -->
  <g clip-path="url(#portrait-reveal)">
    <g clip-path="url(#img-rounded)">
      <image href="data:image/jpeg;base64,{b64_data}" x="170" y="80" width="700" height="700" preserveAspectRatio="xMidYMid slice"/>
      <!-- Futuristic subtle gradient tint over the image bottom -->
      <rect x="170" y="600" width="700" height="180" fill="url(#bg)" opacity="0.4"/>
    </g>
  </g>

  <!-- Terminal Identity and Stats Card -->
  <g font-size="28" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
    <text xml:space="preserve" x="60" y="915">
      <tspan fill="#79c0ff">&gt; Identity  </tspan><tspan fill="#c9d1d9">Kanaga Abishek B  (CIT Chennai · IT)</tspan>
    </text>
    <text xml:space="preserve" x="60" y="960">
      <tspan fill="#79c0ff">&gt; Rating    </tspan><tspan fill="#ffa657" font-weight="bold">LeetCode Knight</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#e3b341" font-weight="bold">1905</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#7ee787">Top 4.57% Worldwide</tspan>
    </text>
    <text xml:space="preserve" x="60" y="1005">
      <tspan fill="#79c0ff">&gt; Solved    </tspan><tspan fill="#c9d1d9">500+ Problems Solved · Knight Badge ⚔️</tspan>
    </text>
    <text xml:space="preserve" x="60" y="1050">
      <tspan fill="#79c0ff">&gt; Focus     </tspan><tspan fill="#d2a8ff" font-weight="bold">Distributed Systems</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#c9d1d9">Agentic AI · Java · MCP</tspan>
    </text>
  </g>

  <text xml:space="preserve" x="60" y="1098" font-size="26">
    <tspan fill="#ff7b72">abishek</tspan><tspan fill="#c9d1d9">@</tspan><tspan fill="#79c0ff">github</tspan><tspan fill="#c9d1d9">:~$ </tspan>
  </text>
  <rect x="290" y="1076" width="14" height="26" fill="#00E5FF">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>
"""
    (ASSETS_DIR / "portrait.svg").write_text(svg_content, encoding="utf-8")
    print("Generated portrait.svg")

def generate_info():
    lines_data = [
        {"y": 100, "t": 0.000, "text": '<tspan fill="#ff7b72">abishek</tspan><tspan fill="#c9d1d9">@</tspan><tspan fill="#79c0ff">github</tspan><tspan fill="#c9d1d9">:~$ ./info.sh</tspan>'},
        {"y": 204, "t": 0.300, "text": '<tspan fill="#ff7b72">abishek</tspan><tspan fill="#c9d1d9">@</tspan><tspan fill="#79c0ff">github</tspan>'},
        {"y": 256, "t": 0.450, "text": '<tspan fill="#58a6ff">----------------------------------------------------</tspan>'},
        {"y": 308, "t": 0.600, "text": '<tspan fill="#79c0ff">Role        </tspan><tspan fill="#c9d1d9">Java Developer &amp; Distributed Systems Engineer</tspan>'},
        {"y": 360, "t": 0.750, "text": '<tspan fill="#79c0ff">Education   </tspan><tspan fill="#c9d1d9">B.Tech, Information Technology (CGPA: 8.1/10)</tspan>'},
        {"y": 412, "t": 0.900, "text": '<tspan fill="#79c0ff">            </tspan><tspan fill="#8b949e">Chennai Institute of Technology (CIT · 2028)</tspan>'},
        {"y": 516, "t": 1.200, "text": '<tspan fill="#79c0ff">LeetCode    </tspan><tspan fill="#ffa657" font-weight="bold">Knight Badge ⚔️</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#e3b341" font-weight="bold">Rating 1905</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#7ee787">Top 4.57%</tspan>'},
        {"y": 568, "t": 1.350, "text": '<tspan fill="#79c0ff">            </tspan><tspan fill="#c9d1d9">500+ Solved · Active Weekly Contest Contender</tspan>'},
        {"y": 620, "t": 1.500, "text": '<tspan fill="#79c0ff">Hackathons  </tspan><tspan fill="#d2a8ff" font-weight="bold">SIH 2025 National Winner</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#c9d1d9">Ministry of Defence</tspan>'},
        {"y": 672, "t": 1.650, "text": '<tspan fill="#79c0ff">            </tspan><tspan fill="#e3b341" font-weight="bold">aOS Buildathon Runner-Up ($1.5k)</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#7ee787">MariaDB Finalist</tspan>'},
        {"y": 724, "t": 1.800, "text": '<tspan fill="#79c0ff">Internships </tspan><tspan fill="#c9d1d9">* SDE Intern — Zenlocare (ZenoHosp in 23 Hospitals)</tspan>'},
        {"y": 776, "t": 1.950, "text": '<tspan fill="#79c0ff">            </tspan><tspan fill="#c9d1d9">* SDE Intern — Kryptos Technology (MCP Agentic AI)</tspan>'},
        {"y": 828, "t": 2.100, "text": '<tspan fill="#79c0ff">Open Source </tspan><tspan fill="#7ee787">* Merged Upstream PR #1150 in Jenkins OpenTelemetry</tspan>'},
        {"y": 932, "t": 2.400, "text": '<tspan fill="#79c0ff">Featured    </tspan><tspan fill="#e3b341">Lumen</tspan><tspan fill="#c9d1d9"> (Distributed Tracing) · </tspan><tspan fill="#e3b341">Varys</tspan><tspan fill="#c9d1d9"> (Agentic CI)</tspan>'},
        {"y": 984, "t": 2.550, "text": '<tspan fill="#79c0ff">Focus       </tspan><tspan fill="#c9d1d9">Java • Spring Boot • gRPC • Cassandra • MCP • OTel</tspan>'},
        {"y": 1036, "t": 2.700, "text": '<tspan fill="#79c0ff">Certs       </tspan><tspan fill="#7ee787">Amazon DSA &amp; Java</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#c9d1d9">NPTEL Python Data Analytics</tspan>'},
    ]

    lines_svg = []
    for i, item in enumerate(lines_data):
        y_text = item["y"]
        y_box = y_text - 36
        t_start = item["t"]
        t_end = t_start + 0.150
        clip_id = f"il{i}"
        
        lines_svg.append(f"""  <clipPath id="{clip_id}">
    <rect x="40" y="{y_box}" height="48" width="0">
      <animate attributeName="width" from="0" to="1135" begin="{t_start:.3f}s" dur="0.15s" fill="freeze"/>
    </rect>
  </clipPath>
  <g clip-path="url(#{clip_id})">
    <text xml:space="preserve" x="40" y="{y_text}" font-size="28">{item["text"]}</text>
  </g>
  <rect y="{y_box + 4}" width="12" height="40" fill="#00E5FF" opacity="0">
    <animate attributeName="x" from="40" to="1175" begin="{t_start:.3f}s" dur="0.15s" fill="freeze"/>
    <set attributeName="opacity" to="0.85" begin="{t_start:.3f}s"/>
    <set attributeName="opacity" to="0" begin="{t_end:.3f}s"/>
  </rect>""")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1215" height="1140" viewBox="0 0 1215 1140" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
  </defs>

  <rect width="1215" height="1140" rx="16" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="1214" height="1139" rx="16" fill="none" stroke="#30363d" stroke-width="2"/>
  <line x1="0" y1="50" x2="1215" y2="50" stroke="#30363d" stroke-width="2"/>
  
  <circle cx="40" cy="25.0" r="8" fill="#ff5f56"/>
  <circle cx="64" cy="25.0" r="8" fill="#ffbd2e"/>
  <circle cx="88" cy="25.0" r="8" fill="#27c93f"/>
  <text x="607.5" y="31.0" fill="#7d8590" font-size="20" text-anchor="middle">abishek@github: ~$ ./info.sh</text>

{''.join(lines_svg)}

  <!-- Final Shell Prompt -->
  <text xml:space="preserve" x="40" y="1103" font-size="28">
    <tspan fill="#ff7b72">abishek</tspan><tspan fill="#c9d1d9">@</tspan><tspan fill="#79c0ff">github</tspan><tspan fill="#c9d1d9">:~$ </tspan>
  </text>
  <rect x="290" y="1078" width="14" height="30" fill="#00E5FF">
    <set attributeName="opacity" to="0" begin="0s"/>
    <set attributeName="opacity" to="1" begin="2.850s"/>
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite" begin="2.850s"/>
  </rect>
</svg>
"""
    (ASSETS_DIR / "info.svg").write_text(svg_content, encoding="utf-8")
    print("Generated info.svg")

def generate_competitive():
    items = [
        {"y": 66, "t": 0.000, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#ffa657" font-weight="bold">LeetCode</tspan>', "size": 19, "bold": True, "indent": False},
        {"y": 90, "t": 0.140, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#e3b341" font-weight="bold">Knight Badge ⚔️</tspan><tspan fill="#8b949e"> (Rank 37.5k)</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 114, "t": 0.280, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Contest Rating: </tspan><tspan fill="#7ee787" font-weight="bold">1905 (Peak)</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 138, "t": 0.420, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#58a6ff" font-weight="bold">Top 4.57%</tspan><tspan fill="#c9d1d9"> Worldwide Contender</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 162, "t": 0.560, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#7ee787" font-weight="bold">500+ Problems Solved</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 186, "t": 0.700, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#8b949e">  Algorithms · Dynamic Programming · Graphs</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 210, "t": 0.840, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Weekly &amp; Biweekly Contest Participant</tspan>', "size": 15, "bold": False, "indent": True},
        
        {"y": 258, "t": 1.120, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#d2a8ff" font-weight="bold">System Architecture</tspan>', "size": 19, "bold": True, "indent": False},
        {"y": 282, "t": 1.260, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#e3b341" font-weight="bold">Distributed Tracing (Lumen Engine)</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 306, "t": 1.400, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Bounded Queue &amp; Multi-Threaded Batch Writers</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 330, "t": 1.540, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Interval Merging Critical Path Latency Analysis</tspan>', "size": 15, "bold": False, "indent": True},
        
        {"y": 378, "t": 1.820, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#79c0ff" font-weight="bold">Core Competencies</tspan>', "size": 19, "bold": True, "indent": False},
        {"y": 402, "t": 1.960, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Java • Concurrency • Cassandra • MCP • gRPC</tspan>', "size": 15, "bold": False, "indent": True},
    ]

    content_blocks = []
    for i, it in enumerate(items):
        y_text = it["y"]
        y_box = y_text - 18
        t_start = it["t"]
        t_end = t_start + 0.14
        clip_id = f"ce{i}"
        x_pos = 38 if it["indent"] else 24
        fw = "bold" if it["bold"] else "normal"
        
        content_blocks.append(f"""  <clipPath id="{clip_id}">
    <rect x="24" y="{y_box}" height="26" width="0">
      <animate attributeName="width" from="0" to="452" begin="{t_start:.3f}s" dur="0.14s" fill="freeze"/>
    </rect>
  </clipPath>
  <g clip-path="url(#{clip_id})">
    <text xml:space="preserve" x="{x_pos}" y="{y_text}" font-size="{it["size"]}" font-weight="{fw}">{it["text"]}</text>
  </g>
  <rect y="{y_box + 1}" width="10" height="22" fill="#00E5FF" opacity="0">
    <animate attributeName="x" from="24" to="476" begin="{t_start:.3f}s" dur="0.14s" fill="freeze"/>
    <set attributeName="opacity" to="0.8" begin="{t_start:.3f}s"/>
    <set attributeName="opacity" to="0" begin="{t_end:.3f}s"/>
  </rect>""")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="500" height="440" viewBox="0 0 500 440" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="500" height="440" rx="12" fill="url(#bg)"/>
  <rect x=".5" y=".5" width="499" height="439" rx="12" fill="none" stroke="#30363d"/>
  <line x1="0" y1="36" x2="500" y2="36" stroke="#30363d"/>
  <circle cx="24" cy="18" r="5" fill="#ff5f56"/>
  <circle cx="40" cy="18" r="5" fill="#ffbd2e"/>
  <circle cx="56" cy="18" r="5" fill="#27c93f"/>
  <text x="250" y="23" fill="#7d8590" font-size="14" text-anchor="middle">abishek@github: ~/competitive-stats</text>

{''.join(content_blocks)}

  <rect x="24" y="416" width="10" height="18" fill="#00E5FF">
    <set attributeName="opacity" to="0" begin="0s"/>
    <set attributeName="opacity" to="1" begin="2.100s"/>
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite" begin="2.100s"/>
  </rect>
</svg>
"""
    (ASSETS_DIR / "competitive.svg").write_text(svg_content, encoding="utf-8")
    print("Generated competitive.svg")

def generate_competitions():
    items = [
        {"y": 64, "t": 0.000, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#d2a8ff" font-weight="bold">Smart India Hackathon 2025</tspan>', "size": 18, "bold": True, "indent": False},
        {"y": 87, "t": 0.140, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#7ee787" font-weight="bold">National Winner</tspan><tspan fill="#8b949e"> · Ministry of Defence</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 107, "t": 0.280, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#e3b341" font-weight="bold">₹1,50,000 Cash Prize</tspan><tspan fill="#c9d1d9"> · Bond Secure Comm Platform</tspan>', "size": 14, "bold": False, "indent": True},
        
        {"y": 145, "t": 0.560, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#3fb950" font-weight="bold">aOS Global Buildathon 2025</tspan>', "size": 18, "bold": True, "indent": False},
        {"y": 168, "t": 0.700, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#7ee787" font-weight="bold">Runner-Up Winner</tspan><tspan fill="#8b949e"> · Global Web3 Competition</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 188, "t": 0.840, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#e3b341" font-weight="bold">$1,500 Award</tspan><tspan fill="#c9d1d9"> for NeoSlot NFT Marketplace</tspan>', "size": 14, "bold": False, "indent": True},
        
        {"y": 226, "t": 1.120, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#79c0ff" font-weight="bold">MariaDB Hackathon 2025</tspan>', "size": 18, "bold": True, "indent": False},
        {"y": 249, "t": 1.260, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#58a6ff" font-weight="bold">National Finalist</tspan><tspan fill="#8b949e"> · Database Engineering</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 269, "t": 1.400, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Top 25 Finalist selected from 2,500+ competitors</tspan>', "size": 14, "bold": False, "indent": True},
        
        {"y": 307, "t": 1.680, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#ffa657" font-weight="bold">HackSymmetric \'26 &amp; Trojans</tspan>', "size": 18, "bold": True, "indent": False},
        {"y": 330, "t": 1.820, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#e3b341" font-weight="bold">Co-Organizer</tspan><tspan fill="#8b949e"> · 48-hr Hackathon w/ Unstop &amp; MLH</tspan>', "size": 15, "bold": False, "indent": True},
        {"y": 350, "t": 1.960, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#c9d1d9">Event Coordinator · Runtime Terror @ Trojans\'25</tspan>', "size": 14, "bold": False, "indent": True},
        
        {"y": 388, "t": 2.240, "text": '<tspan fill="#8b949e">&gt; </tspan><tspan fill="#f97583" font-weight="bold">Certifications &amp; Academics</tspan>', "size": 18, "bold": True, "indent": False},
        {"y": 411, "t": 2.380, "text": '<tspan fill="#8b949e">│ </tspan><tspan fill="#7ee787">Amazon DSA &amp; Java</tspan><tspan fill="#8b949e"> · </tspan><tspan fill="#c9d1d9">NPTEL Python Analytics</tspan>', "size": 15, "bold": False, "indent": True},
    ]

    content_blocks = []
    for i, it in enumerate(items):
        y_text = it["y"]
        y_box = y_text - 18
        t_start = it["t"]
        t_end = t_start + 0.14
        clip_id = f"ct{i}"
        x_pos = 38 if it["indent"] else 24
        fw = "bold" if it["bold"] else "normal"
        
        content_blocks.append(f"""  <clipPath id="{clip_id}">
    <rect x="24" y="{y_box}" height="26" width="0">
      <animate attributeName="width" from="0" to="452" begin="{t_start:.3f}s" dur="0.14s" fill="freeze"/>
    </rect>
  </clipPath>
  <g clip-path="url(#{clip_id})">
    <text xml:space="preserve" x="{x_pos}" y="{y_text}" font-size="{it["size"]}" font-weight="{fw}">{it["text"]}</text>
  </g>
  <rect y="{y_box + 1}" width="10" height="22" fill="#00E5FF" opacity="0">
    <animate attributeName="x" from="24" to="476" begin="{t_start:.3f}s" dur="0.14s" fill="freeze"/>
    <set attributeName="opacity" to="0.8" begin="{t_start:.3f}s"/>
    <set attributeName="opacity" to="0" begin="{t_end:.3f}s"/>
  </rect>""")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="500" height="440" viewBox="0 0 500 440" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#111722"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="500" height="440" rx="12" fill="url(#bg)"/>
  <rect x=".5" y=".5" width="499" height="439" rx="12" fill="none" stroke="#30363d"/>
  <line x1="0" y1="36" x2="500" y2="36" stroke="#30363d"/>
  <circle cx="24" cy="18" r="5" fill="#ff5f56"/>
  <circle cx="40" cy="18" r="5" fill="#ffbd2e"/>
  <circle cx="56" cy="18" r="5" fill="#27c93f"/>
  <text x="250" y="23" fill="#7d8590" font-size="14" text-anchor="middle">abishek@github: ~/competitions</text>

{''.join(content_blocks)}

  <rect x="24" y="416" width="10" height="18" fill="#00E5FF">
    <set attributeName="opacity" to="0" begin="0s"/>
    <set attributeName="opacity" to="1" begin="2.520s"/>
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite" begin="2.520s"/>
  </rect>
</svg>
"""
    (ASSETS_DIR / "competitions.svg").write_text(svg_content, encoding="utf-8")
    print("Generated competitions.svg")

def generate_contributions():
    # Read existing Ramprasanna2 contributions.svg or build matching 52-week grid
    ram_path = BASE_DIR.parent / "Ramprasanna2" / "assets" / "contributions.svg"
    if ram_path.exists():
        content = ram_path.read_text(encoding="utf-8")
        # Replace title and bottom text
        content = content.replace("ramprasanna@github: ~/contributions --graph", "abishek@github: ~/contributions --graph")
        content = content.replace("1,000+ LeetCode &amp; GitHub", "500+ LeetCode &amp; GitHub")
        content = content.replace("365-Day Streak", "Knight Badge")
        content = content.replace("contest participation <tspan fill=\"#e3b341\" font-weight=\"bold\">101</tspan> LeetCode · <tspan fill=\"#e3b341\" font-weight=\"bold\">42</tspan> CodeChef", "contest participation <tspan fill=\"#e3b341\" font-weight=\"bold\">LeetCode</tspan> · top <tspan fill=\"#e3b341\" font-weight=\"bold\">4.57%</tspan>")
        content = content.replace("Knight (1912)", "Knight (1905)")
        content = content.replace("2-Star (1590)", "SIH 2025 Winner")
        (ASSETS_DIR / "contributions.svg").write_text(content, encoding="utf-8")
        print("Generated contributions.svg from template")
    else:
        print("Ramprasanna2 contributions.svg not found, creating from scratch")

def copy_profile_image():
    src = BASE_DIR / "portrait.jpeg"
    dest1 = ASSETS_DIR / "portrait.jpeg"
    dest2 = ASSETS_DIR / "profile.jpg"
    if src.exists():
        data = src.read_bytes()
        dest1.write_bytes(data)
        dest2.write_bytes(data)
        print("Copied portrait.jpeg to assets")

if __name__ == "__main__":
    generate_banner()
    generate_typewriter()
    generate_portrait()
    generate_info()
    generate_competitive()
    generate_competitions()
    generate_contributions()
    copy_profile_image()
    print("All assets generated successfully!")
