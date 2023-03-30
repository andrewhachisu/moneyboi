import sqlite3

def create_connection():
    conn = sqlite3.connect("expenses.db")
    return conn

def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category_id INTEGER,
        description TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    """)
    conn.commit()

def initialize_db():
    conn = create_connection()
    create_tables(conn)
    conn.close()

if __name__ == "__main__":
    initialize_db()
