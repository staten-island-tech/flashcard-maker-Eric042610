import json
import os
FILE = "flashy.json"

def load_cards():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_cards(cards):
    with open(FILE, "w") as f:
        json.dump(cards, f, indent=2)

def teacher_mode():
    cards = load_cards()
    print("Type 'q' to quit.")
    while True:
        question = input("Enter a word or phrase: ")
        if question.lower() == 'q':
            break
        answer = input("Enter the answer: ")
        if answer.lower() == 'q':
            break
        cards[question] = answer
        print(f"Saved: {question} → {answer}")
    save_cards(cards)
    print("All flashcards saved")

def student_mode():
    cards = load_cards()
    if not cards:
        print("No flashcards yet. Use Teacher Mode first.")
        return

    score = 0
    for q, a in cards.items():
        print("\nQuestion:", q)
        guess = input("Your answer: ")
        if guess.strip().lower() == a.strip().lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"Wrong Correct answer: {a}")
    print(f"\nYou got {score} out of {len(cards)} right.")

def main():
    mode = input("Choose mode (teacher/student): ").lower()
    if mode == "teacher":
        teacher_mode()
    elif mode == "student":
        student_mode()
    else:
        print("Please enter 'teacher' or 'student'.")
if __name__ == "__main__":
    main()


