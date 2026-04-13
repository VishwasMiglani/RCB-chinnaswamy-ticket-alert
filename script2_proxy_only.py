"""
RCB Chinnaswamy Ticket Alert

Author: mannkavishwas
GitHub: https://github.com/VishwasMiglani/RCB-chinnaswamy-ticket-alert

Note: Please give proper credit if you reuse this code.
"""
"""
╔══════════════════════════════════════════════════════════════════╗
║         SCRIPT 2 — PROXY ROTATION EDITION                       ║
║         Rotating Proxies + Basic Anti-Bot                       ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHAT PROBLEM DOES THIS SOLVE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Same core problem as Script 1: high-demand ticket/product pages
 sell out in seconds and you need automated monitoring to catch
 the exact moment they go live.

 This script focuses specifically on the IP-blocking problem:
   - Websites block IPs that make too many requests too fast
   - Proxies rotate your IP so each request looks like a
     different person visiting the page
   - If one proxy fails, it automatically tries the next one
   - If ALL proxies fail, it falls back to your real IP so
     monitoring never fully stops

 It uses BASIC anti-bot protection (only hides the webdriver flag
 and rotates user-agent). It does NOT simulate mouse/scroll or
 spoof WebGL/hardware fingerprints like Script 1 does.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW IS THIS DIFFERENT FROM SCRIPT 1 (ULTIMATE)?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Script 1 = Proxies + EVERYTHING (WebGL spoof, plugins, mouse
            simulation, scroll simulation, full HTTP headers,
            hardware faking, permissions API fix)

 Script 2 = Proxies + BASICS ONLY (hides webdriver flag,
            rotates user-agent, randomized viewport)

 Think of Script 2 as a lighter, faster version of Script 1.
 Each check runs slightly faster because there is no mouse/scroll
 simulation overhead. Use this when you want proxy rotation but
 don't need the full anti-bot arsenal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW IS THIS DIFFERENT FROM SCRIPT 3 (NO PROXY)?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Script 3 = No proxies + EVERYTHING (all anti-bot techniques,
            but same IP every time)

 Script 2 = Proxies + BASICS (different IP every check, but
            fewer anti-bot techniques applied per check)

 Script 2 solves the IP-ban problem.
 Script 3 solves the browser fingerprint detection problem.
 Script 1 solves BOTH simultaneously.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROS AND CONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 ✅ PROS:
   + Different IP every check — site never sees same IP twice
   + Simpler and slightly faster than Script 1 (no simulation overhead)
   + Tries both HTTP and SOCKS5 format for each proxy automatically
   + 3-layer fallback: proxy 1 → proxy 2 → direct connection
     (monitoring never fully stops even if all proxies fail)
   + Rotates user-agent (looks like different browser each check)
   + Randomizes viewport size each check
   + Fresh browser session every check (no tracking cookies)
   + Randomized check intervals (25-40s) to avoid fixed bot patterns
   + Easier to read and modify than Script 1
   + Works on Windows, Mac, Linux

 ❌ CONS:
   - Requires a paid proxy account
   - Basic anti-bot only — advanced sites with deep fingerprinting
     (WebGL checks, hardware probing, mouse tracking) may still
     detect and block this script
   - No mouse movement or scroll simulation
   - No WebGL GPU spoofing
   - No full realistic HTTP header set (Sec-Fetch headers missing)
   - No hardware fingerprint faking (CPU cores, RAM)
   - No smart backoff on repeated empty pages (unlike Script 1 & 3)
   - Proxy costs money

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 WHEN TO USE THIS SCRIPT (vs Script 1 or 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 USE Script 2 (this) when:
   → You have working proxies
   → The target site blocks by IP but doesn't do deep fingerprinting
   → You want simpler, faster code than Script 1
   → You're comfortable the basic anti-bot is enough for your target

 USE Script 1 instead when:
   → The site has aggressive bot protection (Cloudflare, Akamai)
   → Script 2 is getting blocked even with proxy rotation
   → You want the strongest possible protection

 USE Script 3 instead when:
   → Your proxies are failing / you don't have proxies
   → The site doesn't aggressively block by IP
   → You want maximum anti-bot without proxy complexity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SETUP (one time only):
   pip install playwright
   python -m playwright install chromium

 RUN:
   python script2_proxy_only.py
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
#  PROXY SETTINGS
#  ─────────────────────────────────────────────────────────────────
#  Replace with your own proxy credentials.
#  Get proxies from: Webshare.io, Bright Data, Oxylabs, etc.
#  Format of each entry in RAW_PROXIES: "IP_ADDRESS:PORT"
# ═══════════════════════════════════════════════════════════════════

PROXY_USER = "YOUR_PROXY_USERNAME"   # ← replace
PROXY_PASS = "YOUR_PROXY_PASSWORD"   # ← replace

RAW_PROXIES = [
    "IP_1:PORT_1",   # ← replace with your proxy IP:PORT pairs
    "IP_2:PORT_2",
    "IP_3:PORT_3",
    # add more proxies here
]

# Build both HTTP and SOCKS5 variants for each proxy.
# Script tries HTTP first, then SOCKS5 if HTTP fails.
PROXIES = []
for p in RAW_PROXIES:
    PROXIES.append({"server": f"http://{p}",   "username": PROXY_USER, "password": PROXY_PASS})
    PROXIES.append({"server": f"socks5://{p}", "username": PROXY_USER, "password": PROXY_PASS})


# ═══════════════════════════════════════════════════════════════════
#  MAIN CONFIG
# ═══════════════════════════════════════════════════════════════════

TICKET_URL         = "https://shop.royalchallengers.com/ticket"  # ← replace with target URL
CHECK_INTERVAL_MIN = 25    # minimum seconds between checks
CHECK_INTERVAL_MAX = 40    # maximum seconds between checks
OPEN_BROWSER       = True  # auto-open browser when live


# ═══════════════════════════════════════════════════════════════════
#  KEYWORD LISTS
#  ─────────────────────────────────────────────────────────────────
#  Edit these to match what your target page actually shows.
#  TIP: Run the script once and read the "Page:" log line to see
#       exactly what text the page is currently showing.
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

# Rotating user agents — makes each check look like a different browser
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

# Internal proxy cursor
proxy_index = 0

def get_next_proxy():
    """Returns the next proxy, cycling back when list is exhausted."""
    global proxy_index
    proxy = PROXIES[proxy_index % len(PROXIES)]
    proxy_index += 1
    return proxy


# ─── Alert functions ───────────────────────────────────────────────

def notify(title, message):
    """Desktop popup notification — cross-platform."""
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
    """Play alert sound. Falls back to terminal bell."""
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


# ─── Core page check ───────────────────────────────────────────────

def try_check_with_proxy(playwright, proxy):
    """
    Load the target page through a specific proxy.
    Returns (status, snippet).

    Basic anti-bot applied:
      - Hides navigator.webdriver (most important flag)
      - Rotates user-agent and viewport
      - Fresh browser session every call (no tracking cookies)
    """
    browser = None
    try:
        browser = playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
        )

        context = browser.new_context(
            proxy={
                "server":   proxy["server"],
                "username": proxy["username"],
                "password": proxy["password"],
            },
            user_agent=random.choice(USER_AGENTS),
            viewport={"width": random.randint(1280, 1920), "height": random.randint(768, 1080)},
            locale="en-IN",
            timezone_id="Asia/Kolkata",
            extra_http_headers={
                "Accept-Language": "en-IN,en;q=0.9",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Cache-Control": "no-cache",
            }
        )

        # Basic anti-bot JS — hides automation flag and fakes core properties
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            Object.defineProperty(navigator, 'plugins',   { get: () => [1, 2, 3, 4, 5] });
            Object.defineProperty(navigator, 'languages', { get: () => ['en-IN', 'en'] });
            Object.defineProperty(navigator, 'platform',  { get: () => 'Win32' });
            window.chrome = { runtime: {} };
        """)

        page = context.new_page()
        time.sleep(random.uniform(1.0, 2.5))

        page.goto(TICKET_URL, wait_until="networkidle", timeout=20000)
        page.wait_for_timeout(random.randint(2500, 4500))

        text = page.inner_text("body").lower().strip()

        if not text:
            return "empty", ""

        snippet = " | ".join(line.strip() for line in text.split("\n") if line.strip())[:100]

        # Check LIVE first — if ANY event has tickets, alert immediately
        for phrase in LIVE_SIGNALS:
            if phrase in text:
                return "live", snippet
            # signature: mannkavishwas_rcb_alert_v1

        # Only check not-live if no live signal found
        for phrase in NOT_LIVE_SIGNALS:
            if phrase in text:
                return "not_live", snippet

        return "unknown", snippet

    except Exception as e:
        err = str(e)
        if any(x in err.lower() for x in ["proxy", "407", "connection", "timeout", "refused"]):
            return "proxy_fail", err[:60]
        return "error", err[:60]

    finally:
        if browser:
            try:
                browser.close()
            except Exception:
                pass


def try_check_direct(playwright):
    """
    Fallback: load page without any proxy (uses your real IP).
    Called only when all proxy attempts fail.
    """
    browser = None
    try:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        context = browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            locale="en-IN",
            timezone_id="Asia/Kolkata",
        )
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            window.chrome = { runtime: {} };
        """)
        page = context.new_page()
        page.goto(TICKET_URL, wait_until="networkidle", timeout=20000)
        page.wait_for_timeout(3000)

        text = page.inner_text("body").lower().strip()
        if not text:
            return "empty", ""

        snippet = " | ".join(line.strip() for line in text.split("\n") if line.strip())[:100]

        for phrase in LIVE_SIGNALS:
            if phrase in text:
                return "live", snippet
        for phrase in NOT_LIVE_SIGNALS:
            if phrase in text:
                return "not_live", snippet

        return "unknown", snippet

    except Exception as e:
        return "error", str(e)[:60]

    finally:
        if browser:
            try:
                browser.close()
            except Exception:
                pass


def check(playwright):
    """
    3-layer fallback system:
      Layer 1: Try current proxy
      Layer 2: If fails → try a different proxy
      Layer 3: If both fail → use direct connection (your real IP)
    Returns (status, ip_label, snippet).
    """
    # Layer 1
    proxy = get_next_proxy()
    proxy_label = proxy["server"].replace("http://", "").replace("socks5://", "")
    status, snippet = try_check_with_proxy(playwright, proxy)

    if status == "proxy_fail":
        # Layer 2
        print(f"           Proxy {proxy_label} failed → trying next proxy...")
        proxy2 = get_next_proxy()
        proxy_label = proxy2["server"].replace("http://", "").replace("socks5://", "")
        status, snippet = try_check_with_proxy(playwright, proxy2)

    if status == "proxy_fail":
        # Layer 3
        print(f"           Both proxies failed → falling back to DIRECT...")
        status, snippet = try_check_direct(playwright)
        return status, "DIRECT (no proxy)", snippet

    proto = proxy["server"].split("://")[0].upper()
    return status, f"{proto} {proxy_label}", snippet


# ─── Main loop ─────────────────────────────────────────────────────

def print_banner():
    print()
    print("=" * 65)
    print("  Ticket Monitor — PROXY EDITION")
    print("=" * 65)
    print(f"  URL     : {TICKET_URL}")
    print(f"  Proxies : {len(RAW_PROXIES)} proxies (HTTP + SOCKS5 = {len(PROXIES)} variants)")
    print("  Fallback: Direct connection if all proxies fail")
    print("  Checks  : Every 25-40 seconds (randomized)")
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
            status, ip_label, snippet = check(playwright)

            if status == "live":
                print("\n" + "!" * 65)
                print()
                print("   *** TICKETS / PRODUCT IS LIVE RIGHT NOW! ***")
                print(f"   >>> {TICKET_URL}")
                print(f"   Page: {snippet}")
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
                print(f"[#{count:04d} | {now}]  Not live yet  [{ip_label}]")
                print(f"           Page: \"{snippet[:70]}\"")

            elif status == "empty":
                print(f"[#{count:04d} | {now}]  Empty page    [{ip_label}] — rotating proxy...")
                time.sleep(8)
                continue

            elif status == "unknown":
                print(f"[#{count:04d} | {now}]  Unclear       [{ip_label}]")
                print(f"           Page: \"{snippet[:70]}\"")

            else:
                print(f"[#{count:04d} | {now}]  {status.upper():<10} [{ip_label}]  {snippet[:50]}")

            wait = random.uniform(CHECK_INTERVAL_MIN, CHECK_INTERVAL_MAX)
            print(f"           Next check in {wait:.0f}s...\n")
            time.sleep(wait)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nMonitor stopped.")
        sys.exit(0)
