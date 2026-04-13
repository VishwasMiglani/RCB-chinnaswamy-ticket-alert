"""
RCB Chinnaswamy Ticket Alert

Author: mannkavishwas
GitHub: https://github.com/VishwasMiglani/RCB-chinnaswamy-ticket-alert

Note: Please give proper credit if you reuse this code.
"""
"""
╔══════════════════════════════════════════════════════════════════╗
║         SCRIPT 1 — ULTIMATE EDITION                             ║
║         Proxy Rotation + Maximum Anti-Bot Protection            ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHAT PROBLEM DOES THIS SOLVE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Many high-demand ticket/product pages (concerts, IPL matches,
 limited sneakers, etc.) sell out within SECONDS of going live.
 You cannot manually refresh a page fast enough to catch that
 moment reliably.

 This script solves that by:
   1. Running a real browser in the background 24/7
   2. Checking the target page every 25-45 seconds automatically
   3. The moment it detects a "Book Now" / "Buy" button appear,
      it immediately:
        - Plays a loud beep (repeating)
        - Sends a desktop popup notification
        - Auto-opens the ticket page in your browser
   So you can complete the purchase while others are still
   manually refreshing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHY USE A REAL BROWSER (PLAYWRIGHT) INSTEAD OF REQUESTS?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Modern ticket sites (RCB, BookMyShow, etc.) are built with
 React/Next.js/Angular — the page content is rendered by JavaScript
 AFTER the initial HTML loads. If you use Python requests library,
 you only get the raw empty HTML shell — no ticket info, no buttons.

 Playwright launches a real Chromium browser (invisible/headless),
 loads the page exactly like a human would, waits for all JavaScript
 to finish, then reads the fully rendered text.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHY PROXIES?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 When you check the same page every 30 seconds from the same IP
 address, the website's security system (Cloudflare, Akamai, etc.)
 detects that pattern and blocks your IP — returning an empty page
 or a CAPTCHA instead of real content.

 Proxies solve this by routing each check through a DIFFERENT IP
 address, so the site sees requests from many different users
 instead of one bot.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROS AND CONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 ✅ PROS:
   + Best overall protection — combines IP rotation AND anti-bot JS
   + IP rotates every check — site never sees same IP twice in a row
   + Anti-bot JS hides all automation fingerprints (webdriver,
     WebGL, plugins, hardware info, permissions)
   + Simulates human mouse movement and scrolling
   + Sends realistic HTTP headers like a real Chrome browser
   + 3-layer fallback: proxy 1 → proxy 2 → direct connection
     (monitoring NEVER fully stops even if all proxies die)
   + Smart backoff: waits 90-150s after 3 consecutive empty pages
   + Fresh browser session every check (no tracking cookies)
   + Randomized timing (25-45s) so requests don't look robotic
   + Works on Windows, Mac, Linux
   + Auto-installs itself (Playwright) if not already installed

 ❌ CONS:
   - Requires a paid proxy account (Webshare, Bright Data, etc.)
     Free proxies exist but are unreliable and slow
   - More complex setup than Script 2 or 3
   - Each check takes longer (proxy connection overhead ~2-5s extra)
   - If proxies are misconfigured, all checks fall back to direct IP
   - Proxy costs money (typically $2-10/month for basic plans)
   - SOCKS5/HTTP proxy format must match what provider supports

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHEN TO USE THIS SCRIPT (vs Script 2 or 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 USE Script 1 (this) when:
   → Target site has aggressive bot protection (Cloudflare, etc.)
   → You need to monitor for many hours (IP ban risk is high)
   → You have working proxies available
   → Stakes are high (e.g. rare concert tickets, limited drops)
   → You want the most robust, never-stop monitoring possible

 USE Script 2 instead when:
   → You want simpler code with proxy rotation
   → Target site has only basic bot protection
   → You don't need mouse/scroll simulation

 USE Script 3 instead when:
   → You don't have proxies or they keep failing
   → The target site doesn't aggressively block by IP
   → You want zero external dependencies beyond Playwright

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SETUP (one time only):
   pip install playwright
   python -m playwright install chromium

 RUN:
   python script1_ultimate.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import time
import random
import subprocess
import sys
import platform
import webbrowser
from datetime import datetime

# ── Auto-install Playwright if not already installed ──────────────
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Playwright not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright


# ═══════════════════════════════════════════════════════════════════
#  PROXY SETTINGS
#  ─────────────────────────────────────────────────────────────────
#  Replace the values below with your own proxy credentials.
#  Format of each proxy in RAW_PROXIES: "IP_ADDRESS:PORT"
#
#  Recommended proxy providers:
#    - Webshare.io      (webshare.io)         — free tier available
#    - Bright Data      (brightdata.com)
#    - Oxylabs          (oxylabs.io)
#    - ProxyScrape      (proxyscrape.com)
#
#  Your provider will give you:
#    username, password, and a list of IP:PORT pairs
# ═══════════════════════════════════════════════════════════════════

PROXY_USER = "YOUR_PROXY_USERNAME"   # ← replace with your proxy username
PROXY_PASS = "YOUR_PROXY_PASSWORD"   # ← replace with your proxy password

RAW_PROXIES = [
    "IP_1:PORT_1",    # ← replace with your proxy IP:PORT pairs
    "IP_2:PORT_2",
    "IP_3:PORT_3",
    "IP_4:PORT_4",
    "IP_5:PORT_5",
    # add as many proxies as you have
]

# Build a combined list of HTTP and SOCKS5 variants for each proxy.
# We try both because some providers support one or the other (or both).
# HTTP proxies  → work for most websites
# SOCKS5 proxies → lower-level, work even when HTTP is blocked
PROXIES = []
for p in RAW_PROXIES:
    PROXIES.append({"server": f"http://{p}",   "username": PROXY_USER, "password": PROXY_PASS})
    PROXIES.append({"server": f"socks5://{p}", "username": PROXY_USER, "password": PROXY_PASS})


# ═══════════════════════════════════════════════════════════════════
#  MAIN CONFIG — Edit these to match the page you are monitoring
# ═══════════════════════════════════════════════════════════════════

# The URL of the page to monitor (the ticket/product page)
TICKET_URL = "https://shop.royalchallengers.com/ticket"   # ← replace with target URL

# How often to check (seconds). Randomized between min and max
# to avoid looking like a bot with a fixed rhythm.
CHECK_INTERVAL_MIN = 25
CHECK_INTERVAL_MAX = 45

# If True, auto-opens the ticket URL in your browser when tickets go live
OPEN_BROWSER = True


# ═══════════════════════════════════════════════════════════════════
#  KEYWORD LISTS
#  ─────────────────────────────────────────────────────────────────
#  The script reads all visible text from the page after JS renders.
#  It then searches for these keywords to determine ticket status.
#
#  NOT_LIVE_SIGNALS → keywords that mean tickets are NOT available yet
#  LIVE_SIGNALS     → keywords that mean tickets ARE available to buy
#
#  Customise these based on what your target page actually says.
#  TIP: Run the script once and read the "Page:" log line to see
#       exactly what text the page is showing right now.
# ═══════════════════════════════════════════════════════════════════

NOT_LIVE_SIGNALS = [
    "sold out",
    "soldout",
    "tickets not available",
    "please await further announcements",
    "await further",
    "coming soon",
    "no tickets",
]

LIVE_SIGNALS = [
    "buy tickets",
    "add to cart",
    "select seats",
    "book tickets",
    "proceed to buy",
    "choose seats",
    "buy ticket",
]

# Rotate through different browser identities each check.
# Sites fingerprint the User-Agent header — rotating it makes
# each request look like it came from a different browser/person.
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

# Rotate through realistic screen sizes.
# Headless browsers default to tiny viewports — sites detect this.
VIEWPORTS = [
    {"width": 1920, "height": 1080},
    {"width": 1366, "height": 768},
    {"width": 1536, "height": 864},
    {"width": 1440, "height": 900},
    {"width": 1280, "height": 720},
    {"width": 1600, "height": 900},
]


# ═══════════════════════════════════════════════════════════════════
#  ANTI-BOT JAVASCRIPT
#  ─────────────────────────────────────────────────────────────────
#  This JavaScript is injected into the browser BEFORE every page
#  load. It overrides properties that websites use to detect
#  automated/headless browsers.
#
#  Without this, sites can detect Playwright via:
#    navigator.webdriver === true  (the most common check)
#    navigator.plugins.length === 0  (headless has no plugins)
#    navigator.languages === []      (headless has no language)
#    WebGL returns "Google SwiftShader" (headless GPU)
#    window.chrome is undefined      (headless lacks this)
# ═══════════════════════════════════════════════════════════════════

ANTI_BOT_SCRIPT = """
    // 1. Hide the #1 automation detection flag
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

    // 2. Fake browser plugins (headless has none by default)
    Object.defineProperty(navigator, 'plugins', {
        get: () => [
            { name: 'Chrome PDF Plugin',     filename: 'internal-pdf-viewer' },
            { name: 'Chrome PDF Viewer',     filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai' },
            { name: 'Native Client',         filename: 'internal-nacl-plugin' },
        ]
    });

    // 3. Fake browser language (headless often has no language set)
    Object.defineProperty(navigator, 'languages', { get: () => ['en-IN', 'en-US', 'en'] });

    // 4. Fake OS platform
    Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });

    // 5. Fake CPU core count (headless often returns 1 or 2)
    Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });

    // 6. Fake RAM amount
    Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });

    // 7. Add window.chrome object (undefined in headless)
    window.chrome = {
        runtime:   {},
        loadTimes: function() {},
        csi:       function() {},
        app:       {}
    };

    // 8. Fix Permissions API (returns different values in headless)
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications'
            ? Promise.resolve({ state: Notification.permission })
            : originalQuery(parameters)
    );

    // 9. Spoof WebGL GPU fingerprint
    //    Headless returns "Google SwiftShader" which is a dead giveaway.
    //    We fake it as a normal Intel GPU instead.
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) return 'Intel Inc.';               // VENDOR
        if (parameter === 37446) return 'Intel Iris OpenGL Engine'; // RENDERER
        return getParameter.call(this, parameter);
    };

    // 10. Match screen size to viewport (headless mismatches these)
    Object.defineProperty(screen, 'availWidth',  { get: () => window.innerWidth });
    Object.defineProperty(screen, 'availHeight', { get: () => window.innerHeight });
"""


# ── Internal state ─────────────────────────────────────────────────
proxy_index  = 0   # cycles through PROXIES list
empty_streak = 0   # counts consecutive empty pages (triggers backoff)

def get_next_proxy():
    """Returns the next proxy from the list, cycling back to start."""
    global proxy_index
    proxy = PROXIES[proxy_index % len(PROXIES)]
    proxy_index += 1
    return proxy


# ═══════════════════════════════════════════════════════════════════
#  ALERT FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def notify(title, message):
    """
    Send a desktop popup notification.
    Automatically uses the right system command for Windows/Mac/Linux.
    """
    system = platform.system()
    try:
        if system == "Darwin":   # macOS
            subprocess.run(["osascript", "-e",
                f'display notification "{message}" with title "{title}" sound name "Glass"'])
        elif system == "Linux":
            subprocess.run(["notify-send", "-u", "critical", "-t", "0", title, message],
                           capture_output=True)
        elif system == "Windows":
            ps = f"""
Add-Type -AssemblyName System.Windows.Forms
$n = New-Object System.Windows.Forms.NotifyIcon
$n.Icon = [System.Drawing.SystemIcons]::Exclamation
$n.BalloonTipTitle = "{title}"
$n.BalloonTipText = "{message}"
$n.Visible = $True
$n.ShowBalloonTip(20000)
Start-Sleep -Seconds 20
$n.Dispose()
"""
            subprocess.run(["powershell", "-Command", ps], capture_output=True)
    except Exception as e:
        print(f"  [Notification error: {e}]")


def beep():
    """Play a loud alert sound. Falls back to terminal bell if unavailable."""
    try:
        if platform.system() == "Darwin":
            subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
        elif platform.system() == "Windows":
            import winsound
            for _ in range(8):
                winsound.Beep(1200, 500)
                time.sleep(0.1)
    except Exception:
        pass
    # Terminal bell fallback (works in any terminal)
    for _ in range(10):
        print("\a", end="", flush=True)
        time.sleep(0.15)


# ═══════════════════════════════════════════════════════════════════
#  HUMAN BEHAVIOUR SIMULATION
#  ─────────────────────────────────────────────────────────────────
#  Sites track mouse movement and scroll behaviour to detect bots.
#  These functions simulate a human casually reading the page.
# ═══════════════════════════════════════════════════════════════════

def human_mouse_movement(page):
    """Move the mouse to 3-6 random positions on the page."""
    try:
        vp = page.viewport_size
        if not vp:
            return
        w, h = vp["width"], vp["height"]
        for _ in range(random.randint(3, 6)):
            x = random.randint(100, w - 100)
            y = random.randint(100, h - 100)
            page.mouse.move(x, y)
            time.sleep(random.uniform(0.1, 0.4))
    except Exception:
        pass


def human_scroll(page):
    """Scroll down then back up, like a human reading the page."""
    try:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 3)")
        time.sleep(random.uniform(0.5, 1.2))
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(random.uniform(0.3, 0.8))
        page.evaluate("window.scrollTo(0, 0)")
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════════════
#  BROWSER BUILDER
#  ─────────────────────────────────────────────────────────────────
#  Creates a fresh Chromium browser instance with all anti-bot
#  measures applied. Optionally attaches a proxy.
#
#  Key idea: a NEW browser is created for EVERY check.
#  This means no persistent cookies, cache, or session that
#  the site could use to track and block us.
# ═══════════════════════════════════════════════════════════════════

def build_context(playwright, proxy=None):
    browser = playwright.chromium.launch(
        headless=True,   # invisible — no browser window appears
        args=[
            "--disable-blink-features=AutomationControlled",  # hides automation
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--window-size=1920,1080",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-site-isolation-trials",
        ]
    )

    viewport = random.choice(VIEWPORTS)   # random screen size each check
    ua       = random.choice(USER_AGENTS) # random browser identity each check

    context_opts = dict(
        user_agent=ua,
        viewport=viewport,
        locale="en-IN",
        timezone_id="Asia/Kolkata",   # ← change to your timezone if needed
        color_scheme="light",
        has_touch=False,
        # Realistic HTTP headers that real Chrome sends.
        # Missing headers are a major bot detection signal.
        extra_http_headers={
            "Accept-Language":           "en-IN,en-US;q=0.9,en;q=0.8",
            "Accept":                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":           "gzip, deflate, br",
            "Cache-Control":             "no-cache",
            "Pragma":                    "no-cache",
            "Sec-Ch-Ua":                 '"Chromium";v="124", "Google Chrome";v="124"',
            "Sec-Ch-Ua-Mobile":          "?0",
            "Sec-Ch-Ua-Platform":        '"Windows"',
            "Sec-Fetch-Dest":            "document",
            "Sec-Fetch-Mode":            "navigate",
            "Sec-Fetch-Site":            "none",
            "Sec-Fetch-User":            "?1",
            "Upgrade-Insecure-Requests": "1",
        }
    )

    # Attach proxy if provided
    if proxy:
        context_opts["proxy"] = {
            "server":   proxy["server"],
            "username": proxy["username"],
            "password": proxy["password"],
        }

    context = browser.new_context(**context_opts)

    # Inject anti-bot JS — runs before every page load in this context
    context.add_init_script(ANTI_BOT_SCRIPT)

    return browser, context


# ═══════════════════════════════════════════════════════════════════
#  PAGE READER
#  ─────────────────────────────────────────────────────────────────
#  Loads the target URL in a real browser, waits for JS to render,
#  simulates human behaviour, then reads all visible text.
#  Returns a status string and a text snippet for logging.
# ═══════════════════════════════════════════════════════════════════

def read_page(playwright, proxy=None):
    browser = None
    label   = "DIRECT" if not proxy else (
        proxy["server"].split("://")[0].upper() + " " +
        proxy["server"].split("://")[1]
    )

    try:
        browser, context = build_context(playwright, proxy)
        page = context.new_page()

        # Random human-like delay before navigating
        time.sleep(random.uniform(2.0, 4.5))

        # Load the page — wait until all network requests finish
        # (important: JS-rendered sites fetch data after initial HTML loads)
        page.goto(TICKET_URL, wait_until="networkidle", timeout=25000)

        # Extra wait for any delayed JS rendering
        page.wait_for_timeout(random.randint(3000, 6000))

        # Simulate human reading the page
        human_mouse_movement(page)
        human_scroll(page)
        time.sleep(random.uniform(0.5, 1.5))

        # Read ALL visible text rendered on the page (post-JS)
        text = page.inner_text("body").lower().strip()

        if not text:
            return "empty", label, ""

        # Flatten multi-line text into a readable one-line snippet for logs
        snippet = " | ".join(line.strip() for line in text.split("\n") if line.strip())[:120]

        # Check LIVE first — if ANY event has tickets, alert immediately
        # (handles case where page has both "sold out" and "buy tickets" for different events)
        for phrase in LIVE_SIGNALS:
            if phrase in text:
                return "live", label, snippet

        # Only check not-live if no live signal found
        for phrase in NOT_LIVE_SIGNALS:
            if phrase in text:
                return "not_live", label, snippet

        return "unknown", label, snippet

    except Exception as e:
        err = str(e)
        # Detect proxy-specific errors so we can rotate instead of crash
        if any(x in err.lower() for x in ["proxy", "407", "connection refused", "timeout", "econnrefused"]):
            return "proxy_fail", label, err[:60]
        return "error", label, err[:60]

    finally:
        # Always close the browser — prevents memory leaks
        if browser:
            try:
                browser.close()
            except Exception:
                pass


# ═══════════════════════════════════════════════════════════════════
#  SMART CHECK — 3-layer fallback
#  ─────────────────────────────────────────────────────────────────
#  Layer 1: Try current proxy
#  Layer 2: If proxy fails → try a different proxy
#  Layer 3: If both proxies fail → use direct connection (your IP)
#
#  This ensures monitoring NEVER fully stops due to proxy issues.
# ═══════════════════════════════════════════════════════════════════

def check(playwright):
    global empty_streak

    # Layer 1: Try proxy
    proxy = get_next_proxy()
    status, label, snippet = read_page(playwright, proxy)

    if status == "proxy_fail":
        # Layer 2: Try a different proxy
        print(f"           [{label}] failed → trying next proxy...")
        proxy2 = get_next_proxy()
        status, label, snippet = read_page(playwright, proxy2)

    if status == "proxy_fail":
        # Layer 3: Fall back to direct connection
        print(f"           [{label}] also failed → falling back to DIRECT...")
        status, label, snippet = read_page(playwright, proxy=None)

    # Track empty pages for smart backoff logic
    empty_streak = (empty_streak + 1) if status == "empty" else 0

    return status, label, snippet


# ─── Main loop ─────────────────────────────────────────────────────

def print_banner():
    print()
    print("=" * 65)
    print("  Ticket Monitor — ULTIMATE EDITION")
    print("  Proxy Rotation + Maximum Anti-Bot Protection")
    print("=" * 65)
    print(f"  URL     : {TICKET_URL}")
    print(f"  Proxies : {len(RAW_PROXIES)} proxies (HTTP + SOCKS5 = {len(PROXIES)} variants)")
    print("  Fallback: Direct connection if all proxies fail")
    print("  Anti-bot: JS masking + WebGL spoof + mouse/scroll sim")
    print("            + realistic headers + fresh session per check")
    print("  Checks  : Every 25-45 seconds (randomized)")
    print("  Started : " + datetime.now().strftime("%d %b %Y, %I:%M:%S %p"))
    print("=" * 65)
    print("  Will BEEP + open browser the moment tickets go live!")
    print("  Press Ctrl+C to stop")
    print()


def main():
    print_banner()
    count = 0

    with sync_playwright() as playwright:
        while True:
            count += 1
            now = datetime.now().strftime("%I:%M:%S %p")

            # If blocked 3 times in a row, back off significantly
            # to let the site's rate-limit timer reset
            if empty_streak >= 3:
                backoff = random.uniform(90, 150)
                print(f"           Empty page 3x in a row — backing off {backoff:.0f}s...")
                time.sleep(backoff)

            status, label, snippet = check(playwright)

            if status == "live":
                print("\n" + "!" * 65)
                print()
                print("   *** TICKETS / PRODUCT IS LIVE RIGHT NOW! ***")
                print(f"   >>> {TICKET_URL}")
                print(f"   Page says: {snippet}")
                print()
                print("!" * 65 + "\n")

                for _ in range(3):
                    beep()
                    notify("TICKETS LIVE NOW!", f"Book NOW at {TICKET_URL}")
                    time.sleep(0.8)

                if OPEN_BROWSER:
                    webbrowser.open(TICKET_URL)
                break

            elif status == "not_live":
                print(f"[#{count:04d} | {now}]  Not live yet  [{label}]")
                print(f"           Page: \"{snippet[:75]}\"")

            elif status == "empty":
                print(f"[#{count:04d} | {now}]  Empty page    [{label}]  streak={empty_streak}")

            elif status == "unknown":
                print(f"[#{count:04d} | {now}]  Unclear       [{label}]")
                print(f"           Page: \"{snippet[:75]}\"")

            else:
                print(f"[#{count:04d} | {now}]  {status.upper():<12} [{label}]  {snippet[:50]}")

            wait = random.uniform(CHECK_INTERVAL_MIN, CHECK_INTERVAL_MAX)
            print(f"           Next check in {wait:.0f}s...\n")
            # signature: mannkavishwas_rcb_alert_v1
            time.sleep(wait)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nMonitor stopped.")
        sys.exit(0)
