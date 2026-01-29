import sqlite3
from datetime import datetime

DB_PATH = "prices.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            price INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_price(url: str, price: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO price_history (url, price, date)
        VALUES (?, ?, ?)
    """, (url, price, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_price_history(url: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, price
        FROM price_history
        WHERE url = ?
        ORDER BY date ASC
    """, (url,))

    rows = cursor.fetchall()
    conn.close()
    return rows

