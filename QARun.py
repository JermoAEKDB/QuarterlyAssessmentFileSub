import sqlite3
import random

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def get_random_questions():
    conn = sqlite3.connect("QuarterlyAssessmentDB.sql")
    cursor = conn.cursor()

    all_questions = []

    for author in ["Crevecouer", "Bradford", "Edwards", "Hawthorne", "Poe"]:
        cursor.execute(f"SELECT question, answer FROM {author}")
        author_data = cursor.fetchall()
        all_questions.extend([(question, answer, author) for question, answer in author_data])

    conn.close()

    random.shuffle(all_questions)
    return all_questions[:10]

def evaluate_responses(questions):
    correct_count = 0
    incorrect_count = 0

    for question, correct_answer, category in questions:
        user_answer = input(f"{category} - {question}: ").strip().lower()

        if user_answer == correct_answer.lower():
            print(f"{GREEN}Correct!{RESET}")
            correct_count += 1
        else:
            print(f"{RED}Incorrect! Correct answer: {correct_answer}{RESET}")
            incorrect_count += 1

    return correct_count, incorrect_count

def display_scoreboard(correct_count, incorrect_count):
    print("\nQuiz Result:")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")

def simulate_quiz():
    print("Welcome to the Quiz Bowl! , This Quiz Bowl is primarily based on authors from American Literature.")
    while True:
        play_again = input("Would you like to play? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing my Quiz Bowl!")
            break

        questions = get_random_questions()
        print("\nLet's get started!:\n")
        correct, incorrect = evaluate_responses(questions)
        display_scoreboard(correct, incorrect)

if __name__ == '__main__':
    simulate_quiz()
