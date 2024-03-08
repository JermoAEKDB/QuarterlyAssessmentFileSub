import sqlite3
import random

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

sql_script = """
-- Paste the entire SQL script here
"""

cursor.executescript(sql_script)

def run_random_quiz():
    cursor.execute("SELECT CategoryName FROM Categories")
    authors = [author[0] for author in cursor.fetchall()]
    random_author = random.choice(authors)

    cursor.execute(f"SELECT * FROM {random_author.replace(' ', '')}")
    questions = cursor.fetchall()

    score = 0
    total_questions = len(questions)

    print(f"\nAuthor: {random_author}\n")

    for question in questions:
        print("Question:", question[1])
        print("Options:")
        cursor.execute(f"SELECT AnswerText, IsCorrect FROM {random_author.replace(' ', '')} WHERE QuestionID = ?", (question[0],))
        options = cursor.fetchall()

        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option[0]}")

        user_answer = input("Your answer (enter the option number): ")
        correct_answer = next(option[0] for option in options if option[1])

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    print(f"You scored {score}/{total_questions} in the {random_author} quiz.\n")

for _ in range(5):
    run_random_quiz()

conn.close()
