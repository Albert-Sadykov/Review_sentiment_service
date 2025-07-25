import sqlite3
from datetime import datetime, timezone

class Database:
    def __init__(self, db_path="reviews.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    sentiment TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            conn.commit()

    def insert_review(self, text: str, sentiment: str) -> dict:
        created_at = datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
                (text, sentiment, created_at)
            )
            review_id = cursor.lastrowid
        return {
            "id": review_id,
            "text": text,
            "sentiment": sentiment,
            "created_at": created_at
        }

    def get_reviews(self, sentiment_filter: str = None):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if sentiment_filter:
                cursor.execute("SELECT * FROM reviews WHERE sentiment = ? ORDER BY id", (sentiment_filter,))
            else:
                cursor.execute("SELECT * FROM reviews ORDER BY id")
            return cursor.fetchall()