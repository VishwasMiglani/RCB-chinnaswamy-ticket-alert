# 🎟️ RCB Ticket Monitor — Playwright-based Auto-Alert Scripts

Automatically watch the [RCB ticket page](https://shop.royalchallengers.com/ticket) and **alert you the instant match tickets go live** — with a loud beep, a desktop notification, and your browser opening automatically.

Built for high-demand pages that sell out in seconds before you can manually refresh.

---

## Why not just use `requests`?

The RCB shop is built with React/Next.js — the page content is rendered by **JavaScript after** the HTML loads. A plain `requests` call only gets an empty HTML shell with no ticket data.

These scripts use **Playwright**, which launches a real Chromium browser (invisible/headless), runs all JavaScript, and reads the fully-rendered page — exactly like a human would.

---

## How It Works

The script loads the ticket page every 30–50 seconds and reads all visible text. It then checks for keywords:

- If **"buy tickets"** (or similar) is found → 🚨 **ALERT — tickets are live!**
- If **"sold out"**, **"tickets not available"**, etc. are found → logs "Not live yet"
- LIVE keywords are always checked first — so if one match is sold out but another has "buy tickets", the alert still fires correctly

---

## The Three Scripts

| Feature | Script 1 — Ultimate | Script 2 — Proxy Only | Script 3 — No Proxy |
|---|---|---|---|
| **Proxy / IP rotation** | ✅ Rotates IPs | ✅ Rotates IPs | ❌ Direct IP |
| **Anti-bot protection** | ✅ Maximum (19 techniques) | ⚠️ Basic only | ✅ Maximum (19 techniques) |
| **Mouse / scroll simulation** | ✅ Yes | ❌ No | ✅ Yes |
| **WebGL GPU spoof** | ✅ Yes | ❌ No | ✅ Yes |
| **Fallback on failure** | ✅ Proxy → Proxy → Direct | ✅ Proxy → Proxy → Direct | ✅ Smart backoff |
| **Complexity** | High | Medium | Low |
| **Best for** | Everything (long duration) | Sites with IP blocks only | No proxies / proxies failing |

---

## Which Script Should I Use?

```
Do you have working proxies?
├── YES → Does the site have aggressive bot protection (Cloudflare, Akamai)?
│         ├── YES → Use Script 1 (Ultimate)
│         └── NO  → Use Script 2 (Proxy Only) — simpler, slightly faster
└── NO  → Use Script 3 (No Proxy)
```

---

## Script 1 — Ultimate Edition
**File:** `script1_ultimate.py`

The most powerful option. Combines IP rotation via proxies with all 19 anti-bot techniques.

**Use when:**
- Target site has aggressive bot protection (Cloudflare, Akamai, etc.)
- You need to monitor for many hours and want the lowest IP-ban risk
- You have working proxies available

**Pros:**
- Rotates IP every check — site never sees the same IP twice in a row
- All 19 anti-bot techniques: WebGL spoof, fake hardware, mouse/scroll simulation, realistic HTTP headers
- 3-layer fallback: proxy 1 → proxy 2 → direct (monitoring never stops)
- Smart backoff after 3 consecutive empty pages

**Cons:**
- Requires a paid proxy account (Webshare, Bright Data, Oxylabs, etc.)
- Most complex setup
- Slight overhead per check due to proxy connection (~2–5s extra)

---

## Script 2 — Proxy Rotation Edition
**File:** `script2_proxy_only.py`

Lighter version of Script 1. Rotates proxies but uses only basic anti-bot protection.

**Use when:**
- The target site blocks by IP but doesn't do deep fingerprint checks
- You want simpler, faster code with proxy rotation

**Pros:**
- Different IP every check
- Simpler and slightly faster than Script 1
- 3-layer fallback: proxy 1 → proxy 2 → direct

**Cons:**
- Basic anti-bot only — advanced fingerprinting detection can still catch it
- No mouse/scroll simulation, no WebGL spoof, no hardware faking

---

## Script 3 — No Proxy Edition
**File:** `script3_no_proxy.py`

Simplest setup. No proxies needed. Applies all 19 anti-bot techniques to disguise the browser as a real human.

**Use when:**
- You don't have proxies, or your proxies keep failing
- Monitoring for a few hours (not days)
- You want zero external dependencies and the simplest setup

**19 Anti-Bot Techniques Applied:**
1. `navigator.webdriver` hidden
2. Fake browser plugins (PDF, NaCl)
3. Fake language list
4. Fake platform (`Win32`)
5. Fake CPU core count (returns 8)
6. Fake device RAM (returns 8 GB)
7. `window.chrome` object added
8. Permissions API fixed
9. WebGL GPU spoofed (fakes Intel GPU)
10. Screen dimensions matched to viewport
11. Full `Sec-Fetch-*` HTTP headers
12. User-agent rotated every check
13. Viewport size rotated every check
14. Fresh browser session every check (no cookies)
15. Random mouse movement simulation
16. Random scroll behaviour
17. Random pre-load delay (2–4.5s)
18. Randomized check intervals (30–50s)
19. Smart backoff after 3 empty pages (waits 90–150s then retries)

**Pros:**
- Free — no proxy cost or setup
- Maximum anti-bot protection every check
- Fastest per-check (no proxy overhead)
- Simplest setup

**Cons:**
- Same IP every check — sustained monitoring (12+ hours) on aggressive sites carries IP ban risk
- Cannot solve CAPTCHAs

---

## Setup

**One-time install (all scripts use the same dependency):**

```bash
pip install playwright
python -m playwright install chromium
```

---

## Configuration

Open whichever script you want to use and edit the config section near the top:

```python
# The URL of the page to monitor — already set to RCB tickets
TICKET_URL = "https://shop.royalchallengers.com/ticket"

# For Script 1 and 2 only — your proxy credentials
PROXY_USER = "YOUR_PROXY_USERNAME"
PROXY_PASS = "YOUR_PROXY_PASSWORD"
RAW_PROXIES = [
    "IP_1:PORT_1",
    "IP_2:PORT_2",
]
```

### Keyword Lists

The script reads all visible text on the page and checks for these phrases:

```python
# Page is NOT live if any of these appear
NOT_LIVE_SIGNALS = [
    "sold out",
    "tickets not available",
    "please await further announcements",
    "coming soon",
    ...
]

# Page IS live if any of these appear
LIVE_SIGNALS = [
    "buy tickets",
    "select seats",
    "book tickets",
    ...
]
```

> **Important:** LIVE_SIGNALS are always checked first. So if one match on the page shows "sold out" but another shows "buy tickets", the alert fires correctly.

> **Tip:** Run the script once and read the `Page:` log line — it shows exactly what text the page is currently displaying, including which keyword matched. Use this to tune the lists if needed.

---

## Run

```bash
# Script 1 — Ultimate (proxies + max anti-bot)
python script1_ultimate.py

# Script 2 — Proxy only
python script2_proxy_only.py

# Script 3 — No proxy (simplest)
python script3_no_proxy.py
```

When tickets go live, the script will:
1. 🔔 Play a loud repeating beep
2. 🖥️ Show a desktop notification
3. 🌐 Auto-open the ticket page in your browser

Press `Ctrl+C` at any time to stop monitoring.

---

## What the Output Looks Like

```
[#0001 | 03:28:13 PM]  Not live yet  [DIRECT]
           Page: "[matched: 'sold out'] #playbold | ... | royal challengers bengaluru vs lucknow super giants | sold out"
           Next check in 38s...

[#0002 | 03:29:46 PM]  Not live yet  [DIRECT]
           Page: "[matched: 'tickets not available'] ... | tickets not available | please await further announcements"
           Next check in 41s...
```

The `[matched: '...']` tag tells you exactly which keyword triggered the status — useful for debugging if something looks wrong.

---

## Proxy Providers

If you need proxies (Script 1 or 2), these services have free or low-cost tiers:

- [Webshare.io](https://webshare.io) — free tier available
- [Bright Data](https://brightdata.com)
- [Oxylabs](https://oxylabs.io)
- [ProxyScrape](https://proxyscrape.com)

Your provider will give you a username, password, and a list of `IP:PORT` pairs to paste into the config.

---

## Requirements

- Python 3.8+
- `playwright` (auto-installs Chromium on first run if not present)
- Windows, macOS, or Linux

---

## Known Site Behaviours (RCB Shop)

| What the page shows | What the script logs |
|---|---|
| "SOLD OUT" button | Not live yet |
| "Tickets not available. Please await further announcements." | Not live yet |
| "Buy Now" button (merchandise only) | Not live yet ✅ correctly ignored |
| "BUY TICKETS" button (match tickets) | 🚨 LIVE — alert fires |
| Two matches: one sold out + one with Buy Tickets | 🚨 LIVE — alert fires correctly |

---

## Legal / Ethical Note

These scripts are intended for personal use — to monitor public pages for availability. Always check a website's Terms of Service before running automated monitoring tools against it.
