"""
RCB Chinnaswamy Ticket Alert

Author: mannkavishwas
GitHub: https://github.com/VishwasMiglani/RCB-chinnaswamy-ticket-alert

Note: Please give proper credit if you reuse this code.
"""
"""
╔══════════════════════════════════════════════════════════════════╗
║         SCRIPT 3 — NO PROXY + MAXIMUM ANTI-BOT EDITION          ║
║         Direct Connection with Full Browser Disguise            ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHAT PROBLEM DOES THIS SOLVE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Same core goal: automatically detect when a ticket/product page
 goes live and alert you instantly so you can complete the purchase
 before it sells out.

 This script focuses on making your browser look exactly like a
 real human using Chrome — without needing any proxy service.

 The key insight: websites don't ONLY block by IP address.
 They also detect bots by examining dozens of browser properties
 (WebGL fingerprint, plugin list, navigator flags, hardware info,
 mouse patterns, scroll behaviour, HTTP headers, etc.).

 Even with a proxy, if those fingerprints scream "headless bot",
 the site can still block you. This script fixes ALL of those
 fingerprints while using your regular internet connection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW IS THIS DIFFERENT FROM SCRIPT 1 (ULTIMATE)?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Script 1 = Maximum anti-bot + proxy IP rotation
 Script 3 = Maximum anti-bot + NO proxy (same IP every check)

 The anti-bot techniques are IDENTICAL between Script 1 and 3.
 The only difference is Script 1 also rotates IP addresses via
 proxies, while Script 3 uses your real IP every time.

 Script 3 compensates for the fixed IP by:
   - Smart backoff (waits 90-150s when blocked, then retries)
   - Randomized check intervals (30-50s, not fixed)
   - Fresh session every check (no cookie-based tracking)
   - All fingerprints hidden so site can't confirm it's a bot
     even if it suspects the IP is automated

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW IS THIS DIFFERENT FROM SCRIPT 2 (PROXY ONLY)?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Script 2 = Proxy IP rotation + basic anti-bot only
 Script 3 = No proxy + ALL anti-bot techniques

 Script 2 solves the IP-block problem with different IPs.
 Script 3 solves the fingerprint-detection problem by disguising
 the browser so perfectly that sites can't confirm it's automated.

 In practice, Script 3 often outperforms Script 2 because:
   - Working proxies are not guaranteed (latency, failures)
   - Many modern sites detect bots by fingerprint, not just IP
   - A perfectly disguised direct connection can be more reliable
     than a broken or slow proxy connection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ANTI-BOT TECHNIQUES USED IN THIS SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1.  navigator.webdriver hidden  → #1 bot detection flag, set to undefined
 2.  Fake plugins                → Real browsers have PDF/NaCl plugins
 3.  Fake languages              → Headless often returns empty array
 4.  Fake platform               → Returns "Win32" like real Chrome
 5.  Fake CPU cores              → Returns 8, not 1 (headless default)
 6.  Fake device RAM             → Returns 8GB, not minimal headless value
 7.  window.chrome added         → Missing in headless by default
 8.  Permissions API fixed       → Returns correct notification state
 9.  WebGL GPU spoofed           → Returns Intel GPU, not "Google SwiftShader"
 10. Screen dimensions matched   → Headless mismatches screen vs viewport
 11. Full Sec-Fetch HTTP headers  → Real Chrome sends these; bots often don't
 12. User-agent rotated          → Different browser identity every check
 13. Viewport size rotated       → Different screen size every check
 14. Fresh browser every check   → No persistent session/cookie tracking
 15. Random mouse movement       → 3-6 random moves after page load
 16. Random scroll behaviour     → Scrolls down and back like a human
 17. Random pre-load delay       → 2-4.5s before navigating (bots load instantly)
 18. Randomized check intervals  → 30-50s, not a fixed robotic rhythm
 19. Smart backoff               → Backs off 90-150s after 3 empty pages

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROS AND CONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 ✅ PROS:
   + No proxy needed — zero cost, zero proxy setup
   + Maximum anti-bot protection applied every single check
   + Simulates human mouse movement and scrolling
   + Spoofs WebGL GPU fingerprint (headless dead giveaway)
   + Fakes ALL navigator properties (plugins, RAM, CPU, language)
   + Sends complete realistic HTTP headers like real Chrome
   + Randomized user-agent and viewport every check
   + Fresh browser session every check (no cookies)
   + Smart backoff when blocked (auto-recovers without crashing)
   + Faster per-check than Script 1 (no proxy connection overhead)
   + Simplest setup — just pip install playwright + one command
   + Works on Windows, Mac, Linux
   + Most reliable when proxies are unavailable or failing

 ❌ CONS:
   - Same IP address every check — if the site IP-bans you, all
     checks from that IP stop working until the ban expires
   - No IP rotation — sustained long-duration monitoring (12+ hours)
     on aggressive sites carries higher IP ban risk
   - Smart backoff (90-150s) means you could miss a short sale
     window if the block hits at exactly the wrong moment
   - Cannot bypass CAPTCHA — if the site serves a CAPTCHA challenge
     instead of the ticket page, this script cannot solve it
   - Works best for shorter monitoring sessions (a few hours)
     where IP bans are less likely to accumulate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHEN TO USE THIS SCRIPT (vs Script 1 or 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 USE Script 3 (this) when:
   → You don't have proxies, or your proxies keep failing
   → The target site blocks by fingerprint more than by IP
   → You are monitoring for a few hours (not days)
   → You want the simplest setup with zero external services
   → Proven working: confirmed page content is loading correctly

 USE Script 1 instead when:
   → You need multi-day monitoring (IP ban risk too high for Script 3)
   → The site has very aggressive rate limiting by IP
   → You have reliable proxies available
   → You want absolute maximum protection on all fronts

 USE Script 2 instead when:
   → You have proxies AND want simpler code than Script 1
   → The site blocks by IP but doesn't do deep fingerprinting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SETUP (one time only):
   pip install playwright
   python -m playwright install chromium

 RUN:
   python script3_no_proxy.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import time
import random
import subprocess
import sys
import platform
import webbrowser
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Playwright not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright


# ═══════════════════════════════════════════════════════════════════
#  MAIN CONFIG — only section you need to edit
# ═══════════════════════════════════════════════════════════════════

TICKET_URL         = "https://shop.royalchallengers.com/ticket"  # ← replace with target URL
CHECK_INTERVAL_MIN = 30
CHECK_INTERVAL_MAX = 50
OPEN_BROWSER       = True


# ═══════════════════════════════════════════════════════════════════
#  KEYWORD LISTS
#  ─────────────────────────────────────────────────────────────────
#  Edit to match what your target page actually shows.
#  TIP: Run the script once and read the "Page:" log line to see
#       exactly what text the page is currently displaying.
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

# Rotate browser identity every check
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

# Rotate screen resolution every check
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
#  Injected into the browser before EVERY page load.
#  Overrides JavaScript properties that websites use to detect
#  headless/automated browsers.
#
#  HOW EACH DETECTION WORKS (and how we counter it):
#
#  1. navigator.webdriver
#     Playwright sets this to `true`. Sites check it directly.
#     Fix: Override to return `undefined`.
#
#  2. navigator.plugins
#     Real browsers have PDF viewer, Flash, etc.
#     Headless has 0 plugins. Sites check plugin count.
#     Fix: Return a fake list of 3 realistic plugins.
#
#  3. navigator.languages
#     Headless often returns empty array [].
#     Fix: Return ['en-IN', 'en-US', 'en'].
#
#  4. WebGL fingerprint
#     Headless renders via "Google SwiftShader" (software GPU).
#     Real browsers show actual GPU names (Intel, NVIDIA).
#     Sites read WebGL VENDOR and RENDERER to fingerprint.
#     Fix: Return "Intel Inc." and "Intel Iris OpenGL Engine".
#
#  5. window.chrome
#     Chrome browser has this object. Headless doesn't.
#     Fix: Create a fake window.chrome object with runtime, app etc.
#
#  6. Permissions API
#     Returns different values in headless vs real browser.
#     Fix: Override to return normal notification permission state.
# ═══════════════════════════════════════════════════════════════════

ANTI_BOT_SCRIPT = """
    // 1. Hide the automation flag
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

    // 2. Fake plugins
    Object.defineProperty(navigator, 'plugins', {
        get: () => [
            { name: 'Chrome PDF Plugin',     filename: 'internal-pdf-viewer' },
            { name: 'Chrome PDF Viewer',     filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai' },
            { name: 'Native Client',         filename: 'internal-nacl-plugin' },
        ]
    });

    // 3. Fake language
    Object.defineProperty(navigator, 'languages', { get: () => ['en-IN', 'en-US', 'en'] });

    // 4. Fake OS platform
    Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });

    // 5. Fake CPU core count
    Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });

    // 6. Fake device RAM
    Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });

    // 7. Add window.chrome
    window.chrome = {
        runtime:   {},
        loadTimes: function() {},
        csi:       function() {},
        app:       {}
    };

    // 8. Fix Permissions API
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications'
            ? Promise.resolve({ state: Notification.permission })
            : originalQuery(parameters)
    );

    // 9. Spoof WebGL GPU fingerprint
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) return 'Intel Inc.';
        if (parameter === 37446) return 'Intel Iris OpenGL Engine';
        return getParameter.call(this, parameter);
    };

    // 10. Match screen dimensions to viewport
    Object.defineProperty(screen, 'availWidth',  { get: () => window.innerWidth });
    Object.defineProperty(screen, 'availHeight', { get: () => window.innerHeight });
"""


# ─── Alert functions ───────────────────────────────────────────────

def notify(title, message):
    """Desktop popup notification — works on Windows, Mac, Linux."""
    system = platform.system()
    try:
        if system == "Darwin":
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
    """Loud alert sound. Falls back to terminal bell character."""
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
    for _ in range(10):
        print("\a", end="", flush=True)
        time.sleep(0.15)


# ─── Human behaviour simulation ────────────────────────────────────

def human_mouse_movement(page):
    """
    Move mouse to 3-6 random positions on the page.
    Sites track mouse events — zero movement is a strong bot signal.
    """
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
    """
    Scroll down then back up, like a human reading the page.
    Bots that never scroll are easier to detect.
    """
    try:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 3)")
        time.sleep(random.uniform(0.5, 1.2))
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(random.uniform(0.3, 0.8))
        page.evaluate("window.scrollTo(0, 0)")
    except Exception:
        pass


# ─── Core check ────────────────────────────────────────────────────

def check(playwright):
    """
    Open a fresh browser (no proxy), load the target page,
    simulate human behaviour, then read all visible text.

    KEY DESIGN — fresh browser every check:
      New browser instance = no persistent cookies, localStorage,
      or session data. Each check appears as a brand-new first
      visit from a fresh browser. This prevents session-based
      tracking and blocking.

    Returns (status, snippet).
    """
    browser = None
    try:
        browser = playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                # signature: mannkavishwas_rcb_alert_v1
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--window-size=1920,1080",
                "--disable-features=IsolateOrigins,site-per-process",
                "--disable-site-isolation-trials",
            ]
        )

        viewport = random.choice(VIEWPORTS)
        ua       = random.choice(USER_AGENTS)

        context = browser.new_context(
            user_agent=ua,
            viewport=viewport,
            locale="en-IN",
            timezone_id="Asia/Kolkata",  # ← change to your timezone if needed
            color_scheme="light",
            has_touch=False,
            # Full set of HTTP headers real Chrome sends.
            # Missing Sec-Fetch headers are a major bot detection signal.
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

        # Inject anti-bot JS — runs before every page load
        context.add_init_script(ANTI_BOT_SCRIPT)

        page = context.new_page()

        # Random delay before loading — instant navigation is a bot signal
        time.sleep(random.uniform(2.0, 4.5))

        # Load page — wait_until="networkidle" is CRITICAL for JS-rendered
        # sites. It waits until ALL JavaScript and API calls finish,
        # so the page text is fully populated before we read it.
        page.goto(TICKET_URL, wait_until="networkidle", timeout=30000)

        # Extra wait for slow/delayed JS rendering
        page.wait_for_timeout(random.randint(3000, 6000))

        # Simulate human behaviour
        human_mouse_movement(page)
        human_scroll(page)
        time.sleep(random.uniform(0.5, 1.5))

        # Read ALL visible rendered text (this is what makes Playwright
        # better than requests — requests only gets raw HTML before JS runs)
        text = page.inner_text("body").lower().strip()

        if not text:
            return "empty", ""

        snippet = " | ".join(line.strip() for line in text.split("\n") if line.strip())[:300]

        # Check LIVE first — if ANY event has tickets, alert immediately
        # (handles case where page has both "sold out" and "buy tickets" for different events)
        for phrase in LIVE_SIGNALS:
            if phrase in text:
                return "live", f"[matched: '{phrase}'] {snippet}"

        # Only check not-live if no live signal found
        for phrase in NOT_LIVE_SIGNALS:
            if phrase in text:
                return "not_live", f"[matched: '{phrase}'] {snippet}"

        return "unknown", snippet

    except Exception as e:
        return "error", str(e)[:80]

    finally:
        # Always close — prevents memory leaks over long monitoring sessions
        if browser:
            try:
                browser.close()
            except Exception:
                pass


# ─── Main loop ─────────────────────────────────────────────────────

def print_banner():
    print()
    print("=" * 65)
    print("  Ticket Monitor — NO PROXY + MAXIMUM ANTI-BOT EDITION")
    print("=" * 65)
    print(f"  URL     : {TICKET_URL}")
    print("  Proxy   : None (direct connection, your real IP)")
    print("  Anti-bot: 19 techniques (see script header for full list)")
    print("  Checks  : Every 30-50 seconds (randomized)")
    print("  Started : " + datetime.now().strftime("%d %b %Y, %I:%M:%S %p"))
    print("=" * 65)
    print("  Will BEEP + open browser the moment tickets go live!")
    print("  Press Ctrl+C to stop")
    print()


def main():
    print_banner()
    count        = 0
    empty_streak = 0  # tracks consecutive empty pages

    with sync_playwright() as playwright:
        while True:
            count += 1
            now = datetime.now().strftime("%I:%M:%S %p")

            # Smart backoff: 3 empty pages in a row = site is rate-limiting.
            # Wait 90-150s to let the block timer reset before retrying.
            if empty_streak >= 3:
                backoff = random.uniform(90, 150)
                print(f"           Empty 3x in a row — backing off {backoff:.0f}s to let block expire...")
                time.sleep(backoff)
                empty_streak = 0

            status, snippet = check(playwright)

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
                empty_streak = 0
                print(f"[#{count:04d} | {now}]  Not live yet  [DIRECT]")
                print(f"           Page: \"{snippet[:80]}\"")

            elif status == "empty":
                empty_streak += 1
                print(f"[#{count:04d} | {now}]  Empty page (rate-limited?)  streak={empty_streak}")

            elif status == "unknown":
                empty_streak = 0
                print(f"[#{count:04d} | {now}]  Unclear  [DIRECT]")
                print(f"           Page: \"{snippet[:80]}\"")

            else:
                print(f"[#{count:04d} | {now}]  Error: {snippet}")

            wait = random.uniform(CHECK_INTERVAL_MIN, CHECK_INTERVAL_MAX)
            print(f"           Next check in {wait:.0f}s...\n")
            time.sleep(wait)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nMonitor stopped.")
        sys.exit(0)
