import sqlite3

import os

DB_PATH = os.getenv("FEATURE_DB", "features.db")



def get_user_interactions(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT item_id, count
        FROM user_features
        WHERE user_id = ?
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return {item: count for item, count in rows}
