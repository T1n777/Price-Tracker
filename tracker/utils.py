import sqlite3
import matplotlib.pyplot as plt
from tracker.database import DB_PATH


def plot_price_history(url: str):
    """
    Plot a price history graph for a given product URL
    using data stored in prices.db.
    """

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

    if not rows:
        print("[ERROR] No price history found for this URL.")
        return

    dates = [row[0][:10] for row in rows]  # YYYY-MM-DD
    prices = [row[1] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o")
    plt.title("Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
