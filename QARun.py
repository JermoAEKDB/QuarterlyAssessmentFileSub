import sqlite3


GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def get_author_data(author):
    conn = sqlite3.connect("QuarterlyAssessmentDB.sql")
    cursor = conn.cursor()

    cursor.execute(f"SELECT question, answer FROM {author}")
    data = cursor.fetchall()

    conn.close()

    return data

def evaluate_responses(author_data, user_responses):
    correct_count = 0
    incorrect_count = 0

    for question, correct_answer in author_data:
        user_answer = input(f"{question}: ").strip().lower()

        if user_answer == correct_answer.lower():
            print(f"{GREEN}Correct!{RESET}")
            correct_count += 1
        else:
            print(f"{RED}Incorrect! Correct answer: {correct_answer}{RESET}")
            incorrect_count += 1

    print("\nQuiz Result:")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")

def simulate_quiz(author_name):
    print(f"Quiz for {author_name}:\n")
    author_data = get_author_data(author_name)
    evaluate_responses(author_data, [])

if __name__ == '__main__':
    authors = ["Crevecouer", "Bradford", "Edwards", "Hawthorne", "Poe"]

    for author in authors:
        simulate_quiz(author)
        print("\n" + "=" * 30 + "\n")
