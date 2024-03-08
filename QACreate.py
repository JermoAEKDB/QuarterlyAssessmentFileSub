import sqlite3

def create_tables():
    conn = sqlite3.connect("QuarterlyAssessmentDB.sql")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Crevecouer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bradford (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Edwards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Hawthorne (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Poe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
