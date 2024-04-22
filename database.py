import sqlite3

DATABASE = 'RetailStore.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Employees (
                            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            type TEXT NOT NULL,
                            years_worked INTEGER NOT NULL,
                            total_purchased REAL DEFAULT 0,
                            total_discounts REAL DEFAULT 0,
                            discount_number INTEGER UNIQUE NOT NULL)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Items (
                            item_number INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            cost REAL NOT NULL)''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table()