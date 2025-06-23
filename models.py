# models.py

import sqlite3

def create_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Drop old table (optional if already exists)
    cursor.execute('DROP TABLE IF EXISTS questions')

    # Create new table with subject
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL CHECK (correct_option BETWEEN 1 AND 4),
            subject TEXT NOT NULL
        )
    ''')

    # Sample questions
    sample_questions = [
        ("What is 2 + 2?", "1", "3", "4", "5", 3, "Math"),
        ("What planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2, "Science"),
        ("Who discovered gravity?", "Einstein", "Newton", "Tesla", "Edison", 2, "Science"),
        ("When did WW2 end?", "1942", "1945", "1948", "1939", 2, "History"),
        ("What is 9 * 3?", "27", "18", "36", "21", 1, "Math"),
        ("Who was the first PM of India?", "Modi", "Nehru", "Gandhi", "Bose", 2, "History")
    ]

    cursor.executemany('''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option, subject)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_questions)

    conn.commit()
    conn.close()
    print("✅ Database created and populated successfully!")

if __name__ == "__main__":
    create_database()
