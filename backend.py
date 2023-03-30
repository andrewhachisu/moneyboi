from database import create_connection

def add_expense(category_id, description, amount, date):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (category_id, description, amount, date) VALUES (?, ?, ?, ?)", (category_id, description, amount, date))
    conn.commit()
    conn.close()

def view_expenses():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_category(name):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_categories():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM categories")
    rows = cur.fetchall()
    conn.close()
    return rows
