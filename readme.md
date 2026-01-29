<p align="center">

  <!-- Python version -->
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python Version">

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">

  <!-- Stars -->
  <img src="https://img.shields.io/github/stars/T1n777/Price-Tracker?style=social" alt="GitHub Stars">

  <!-- Forks -->
  <img src="https://img.shields.io/github/forks/T1n777/Price-Tracker?style=social" alt="GitHub Forks">

  <!-- Issues -->
  <img src="https://img.shields.io/github/issues/T1n777/Price-Tracker" alt="GitHub Issues">

  <!-- Last commit -->
  <img src="https://img.shields.io/github/last-commit/T1n777/Price-Tracker" alt="Last Commit">

  <!-- Repo size -->
  <img src="https://img.shields.io/github/repo-size/T1n777/Price-Tracker" alt="Repo Size">

</p>

# 🛒 Price Tracker with Telegram Alerts  
A clean, reliable, Python-powered **Amazon India price tracker** that monitors product prices and sends **real-time Telegram alerts** the moment the price drops below your target.

Built using:
- Python 3  
- BeautifulSoup  
- SQLite  
- Telegram Bot API  
- schedule  

---

# 📸 Screenshots

## Telegram Price Drop Alert  
![Telegram Alert](assets/alert.png)

## Terminal Output  
![Terminal Output](assets/terminal.png)

---

# 🚀 Features

- Accurate Amazon price scraping  
- Real-time Telegram alerts  
- 30-minute automated checking  
- SQLite price history logging  
- No Selenium / No browsers  
- Lightweight and fast  

---

# ⚙️ Installation

## 1. Clone the repository

```
git clone https://github.com/T1n777/Price-Tracker.git
cd Price-Tracker
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

---

# 🤖 Telegram Bot Setup

## 1. Open Telegram  
Search **@BotFather**

## 2. Create a new bot  
Send:

```
/newbot
```

BotFather will give you a **bot token** like:

```
123456789:ABCdefGhijKLMNOPqrs_tuvWXyz
```

## 3. Start your bot  
Open your bot → press **Start**

## 4. Send a message  
Write anything:

```
hi
```

## 5. Get your Telegram Chat ID  
Paste this in your browser:

```
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

You will see something like:

```
"chat": { "id": xxxxxxxxxx }
```

That number 'xxxxxxxxxx' is your **chat ID**.

---

# ▶️ Running the Tracker

Run the script:

```
python main.py
```

You will be asked for:

- Product URL  
- Target price  
- Bot token  
- Chat ID  

### Example:

```
=== PRICE TRACKER ===
Enter product URL: https://www.amazon.in/dp/B0C9YMVX2C
Enter target price (₹): 35000
Enter your Telegram bot token: <TOKEN>
Enter your Telegram chat ID: 8223377100
```

### Example Telegram alert:

```
📉 PRICE DROP ALERT!

ZOTAC Gaming RTX 4060 8GB  
Current Price: ₹33,389  
Your Target: ₹35,000  

🔗 https://www.amazon.in/dp/B0C9YMVX2C
```

---

# 📁 Project Structure

```
price_tracker/
│
├── tracker/
│   ├── scraper.py
│   ├── scheduler.py
│   ├── alert.py
│   ├── database.py
│   ├── utils.py
│   └── __init__.py
│
├── assets/
│   ├── alert.png
│   └── terminal.png
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# 🕸 How the Scraper Works

Amazon uses dynamic HTML based on region, device, and anti-bot checks.

To ensure reliability, the scraper extracts:

### Title from:
- `og:title`  
- `<title>`  
- JSON-LD schema `"name"`  
- Amazon internal JSON structures  

### Price from:
- `"priceAmount"` metadata  
- Fallback regex to match ₹ values  
- Filters out invalid prices (like ₹29 from hidden tags)  

No Selenium required → faster and lightweight.

---

# 🗄 Database Schema

SQLite file: `prices.db`

```
url   TEXT
price INTEGER
date  TEXT
```

---

# 📝 License  
MIT License — free to modify and reuse.

---

# ⭐ Support  
If you like this project, please **star the repo**!
