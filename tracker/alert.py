import requests


def send_telegram_message(message: str, bot_token: str, chat_id: str):
    """
    Sends a message to a Telegram chat using your bot.
    """
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }

        response = requests.post(url, data=data, timeout=10)

        if response.status_code != 200:
            print(f"[ERROR] Telegram API returned {response.status_code}: {response.text}")
        else:
            print("[INFO] Alert sent to Telegram.")

    except Exception as e:
        print(f"[EXCEPTION] Failed to send Telegram message: {e}")
