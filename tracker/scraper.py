import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/13.1.1 Mobile/15E148 Safari/604.1"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}


# ------------------------------------------------------------
# HELPER: Extract ASIN
# ------------------------------------------------------------
def get_asin(url: str) -> str:
    """Extract ASIN from Amazon URL."""
    if "/dp/" in url:
        return url.split("/dp/")[1].split("/")[0]
    elif "/gp/" in url:
        for part in url.split("/"):
            if len(part) == 10:
                return part
    return None


# ------------------------------------------------------------
# HELPER: Extract Title from multiple sources
# ------------------------------------------------------------
def extract_title(html: str):
    title = None

    # 1. OG meta tag
    og = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    if og:
        title = og.group(1).strip()

    # 2. <title> tag
    if not title:
        t_match = re.search(r'<title>([^<]+)</title>', html)
        if t_match:
            t_raw = t_match.group(1).strip()
            # Remove Amazon formatting
            t_raw = t_raw.replace("Amazon.in:", "").replace("Buy", "").strip()
            title = t_raw

    # 3. Schema JSON-LD
    if not title:
        schema = re.search(r'"name"\s*:\s*"([^"]+)"', html)
        if schema:
            title = schema.group(1).strip()

    # 4. Amazon JSON block fallback
    if not title:
        json_title = re.search(r'"title"\s*:\s*"([^"]+)"', html)
        if json_title:
            title = json_title.group(1).strip()

    return title


# ------------------------------------------------------------
# HELPER: Extract Price (most reliable)
# ------------------------------------------------------------
def extract_price(html: str):
    # 1. Direct JSON price
    match = re.search(r'"priceAmount"\s*:\s*([0-9]+)', html)
    if match:
        return int(match.group(1))

    # 2. Search all ₹ prices, pick the largest valid one
    all_prices = re.findall(r"₹\s?([\d,]+)", html)
    cleaned = []

    for p in all_prices:
        value = int(p.replace(",", ""))
        if value > 999:  # ignore tiny ₹29, ₹99, ₹10 fees
            cleaned.append(value)

    if cleaned:
        return max(cleaned)  # highest price is usually the actual GPU price

    return None


# ------------------------------------------------------------
# MAIN FUNCTION — Scrape Amazon product
# ------------------------------------------------------------
def get_amazon_price(url: str):
    asin = get_asin(url)
    if not asin:
        print("[ERROR] Could not extract ASIN from URL.")
        return None

    product_url = f"https://www.amazon.in/dp/{asin}"

    try:
        resp = requests.get(product_url, headers=HEADERS, timeout=10)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Extract Title -----
        title = extract_title(html)

        # ----- Extract Price -----
        price = extract_price(html)

        if not title:
            print("[ERROR] Could not extract product title.")
            return None

        if not price:
            print("[ERROR] Could not extract product price.")
            return None

        return {"title": title, "price": price}

    except Exception as e:
        print("[EXCEPTION]", e)
        return None

