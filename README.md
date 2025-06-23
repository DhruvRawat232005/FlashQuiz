# FlashQuiz — Flask-Based Subject Quiz App

FlashQuiz is a modern, responsive web quiz application built using **Flask**, **HTML/CSS/JavaScript**, and **SQLite**. It allows users to take quizzes by selecting a subject, answer multiple-choice questions, and view their scores instantly.

---

## Features

- Subject-based quizzes (Math, Science, History, etc.)
- Multiple choice questions stored in a SQLite database
- Immediate score display upon quiz completion
- Responsive UI with dark/light themes
- Lightweight and easy to deploy

---

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask (Python)
- **Database**: SQLite3
- **Templating Engine**: Jinja2

---

## Preview

> ![Screenshot 2025-06-24 004926](https://github.com/user-attachments/assets/90ac3fdd-c3e4-4e61-8580-daa30ee28c1b)

> ![Screenshot 2025-06-24 004908](https://github.com/user-attachments/assets/5af671a6-3538-4410-8c15-8421b8dffb88)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flashquiz.git
cd flashquiz
```

### 2. Create and Populate the Database

```bash
python models.py
```

### 3. Run the app

```bash
python app.py
```

---

## Future Improvements

- Add user login and registration
- Admin dashboard to manage questions and subjects
- Leaderboard to track top scorers
- Difficulty levels per question
- Support for large datasets with thousands of questions
- Allow teachers or admins to post/upload questions via web interface or CSV import
- Categorize quizzes by subject, topic, and class level
- Support MCQs, true/false, and fill-in-the-blank types
