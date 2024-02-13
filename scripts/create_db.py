import os
import sqlite3


def create_db() -> None:
    db_path = "apollo.db"

    if os.path.exists(db_path):
        print("Database already exists")
    else:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created")
