import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "questions.db")

# Get all quiz questions from the DB
def get_questions(subject=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if subject:
        cursor.execute("SELECT * FROM questions WHERE subject = ?", (subject,))
    else:
        cursor.execute("SELECT * FROM questions")
        
    questions = cursor.fetchall()
    conn.close()
    return questions


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    subject = request.args.get('subject')
    questions = get_questions(subject)
    return render_template('quiz.html', questions=questions, subject=subject)

@app.route('/submit', methods=['POST'])
def submit():
    questions = get_questions()
    score = 0
    total = len(questions)

    for q in questions:
        qid = str(q[0])
        selected = request.form.get(qid)
        if selected and int(selected) == q[6]:  # correct_option is at index 6
            score += 1

    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
