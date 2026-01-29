import time
import schedule
from tracker.scraper import get_amazon_price
from tracker.alert import send_telegram_message
from tracker.database import save_price


def run_price_check(url, target_price, bot_token, chat_id):
    print("\n[DEBUG] run_price_check() called")
    print(f"[DEBUG] Target price: {target_price}")

    data = get_amazon_price(url)
    print("[DEBUG] Scraper returned:", data)

    if not data:
        print("[ERROR] Scraper returned None. Skipping.")
        return

    title = data["title"]
    price = data["price"]

    # Save price to DB
    save_price(url, price)

    # Alert condition
    if price <= target_price:
        msg = (
            f"📉 PRICE DROP ALERT!\n\n"
            f"{title}\n"
            f"Current Price: ₹{price}\n"
            f"Your Target: ₹{target_price}\n\n"
            f"🔗 {url}"
        )
        send_telegram_message(msg, bot_token, chat_id)
        print("[INFO] Alert sent!")
    else:
        print(f"[INFO] No alert. Current price ₹{price} is above target ₹{target_price}.")


def start_scheduler(url, target_price, bot_token, chat_id):
    print("[INFO] Scheduler started. Running every 30 minutes...")

    # Run immediately once
    run_price_check(url, target_price, bot_token, chat_id)

    # Then schedule every 30 minutes
    schedule.every(30).minutes.do(
        run_price_check, url, target_price, bot_token, chat_id
    )

    while True:
        schedule.run_pending()
        time.sleep(1)
