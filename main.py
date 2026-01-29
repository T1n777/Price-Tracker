from tracker.database import init_db
from tracker.scheduler import start_scheduler


def main():
    print("=== PRICE TRACKER ===")

    # ---- USER INPUTS ----
    url = input("Enter product URL: ").strip()
    target_price = int(input("Enter target price (₹): ").strip())
    bot_token = input("Enter your Telegram bot token: ").strip()
    chat_id = input("Enter your Telegram chat ID: ").strip()

    # ---- SETUP DATABASE ----
    print("[INFO] Initializing database...")
    init_db()

    # ---- START TRACKING ----
    print("[INFO] Starting price tracker...")
    start_scheduler(url, target_price, bot_token, chat_id)


if __name__ == "__main__":
    main()
