# 🛒 Price Tracker with Telegram Alerts  
A clean, reliable, Python-powered **Amazon India price tracker** that monitors product prices and sends **real-time Telegram alerts** the moment the price drops below your target.

Built using:
- 🐍 Python 3  
- 🔍 BeautifulSoup  
- 💾 SQLite  
- 🤖 Telegram Bot API  
- ⏱ Scheduler (auto-check every 30 minutes)  

---

# 📸 Screenshots

## 📩 Telegram Price Drop Alert   
![Telegram Alert](assets/alert.png)

## 🖥 Terminal Output  
![Terminal Output](assets/terminal.png)

---

# 🚀 Features

### ✔ Accurate Amazon Price Scraper  
Uses HTML + OpenGraph metadata + JSON + regex fallback to scrape Amazon even when bot-blocked.

### ✔ Instant Telegram Alerts  
Sends beautiful messages directly to your Telegram.

### ✔ Automatic 30-Minute Scheduler  
Runs silently in the background and checks price repeatedly.

### ✔ Price Logging  
Stores all prices in an SQLite database (`prices.db`).

### ✔ Lightweight, No Selenium  
No heavy browsers, no JavaScript rendering — fast and efficient.

---

# 📁 Project Structure

price_tracker/
│
├── tracker/
│ ├── scraper.py # Hybrid Amazon scraper
│ ├── scheduler.py # Auto-check scheduler + alert logic
│ ├── alert.py # Telegram message sender
│ ├── database.py # SQLite logging
│ ├── utils.py # Utility functions
│ └── init.py
│
├── main.py # Entry point (CLI)
├── requirements.txt
└── README.md


---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd price_tracker


# Install dependencies:

pip install -r requirements.txt



# 🤖 Telegram Bot Setup (Very Important)
1. Open Telegram

Search for @BotFather

2. Create a bot
/newbot

3. Copy your bot token

Example (NOT real):

123456:ABC-xyz123-sometoken

4. Start the bot

Open your bot → press Start

5. Send a message (like "hi")
6. Get your chat ID

Open in browser:

https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates


Find:

"chat": { "id": xxxxxxxxxx }


That "xxxxxxxxxx" is your chat ID.



# ▶️ How to Use

Run:

python main.py


You will be asked:

Product URL

Target price

Bot token

Chat ID

Example:
=== PRICE TRACKER ===
Enter product URL: https://www.amazon.in/dp/B0C9YMVX2C
Enter target price (₹): 35000
Enter your Telegram bot token: <TOKEN>
Enter your Telegram chat ID: <CHAT_ID>


If the product is below your target, you instantly receive:

📉 PRICE DROP ALERT!

ZOTAC Gaming RTX 4060 8GB
Current Price: ₹33,389
Your Target: ₹99,99,999

🔗 https://www.amazon.in/dp/B0C9YMVX2C



# 🕸 How the Scraper Works (Short Technical Breakdown)

Amazon blocks simple scrapers heavily, so this script:

Extracts Title From:

<meta property="og:title">

<title>

JSON-LD schema ("name")

Amazon embedded product JSON ("title")

Extracts Price From:

"priceAmount" internal metadata

Fallback ₹ regex (ignores low junk values like ₹29)

This makes the scraper extremely consistent without needing Selenium.

🗄 Database Schema (SQLite)

The project uses a simple SQLite database:

prices.db

Table:

url TEXT
price INTEGER
date TEXT



# 📝 License

MIT License — feel free to modify and reuse.