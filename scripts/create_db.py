import sqlite3


def create_db():
    conn = sqlite3.connect("apollo.db")
    conn.close()

    print("Database created")
