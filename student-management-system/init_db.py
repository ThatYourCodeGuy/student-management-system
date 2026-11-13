import sqlite3
import os
from models.student import Student

# The original data to migrate
raw_students_data = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Samuel", "score": 67},
    {"name": "Grace", "score": 91},
]

def migrate_data():
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score REAL NOT NULL
        )
    ''')

    # Clear existing data for a fresh migration
    cursor.execute('DELETE FROM students')

    # Migrate data
    for data in raw_students_data:
        try:
            student = Student(**data)
            cursor.execute(
                "INSERT INTO students (name, score) VALUES (?, ?)",
                (student.name, student.score)
            )
        except Exception as e:
            print(f"Error migrating {data}: {e}")

    conn.commit()
    conn.close()
    print("Data migration to SQLite completed.")

if __name__ == "__main__":
    migrate_data()