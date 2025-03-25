import json
import random

def student_mode():
    with open("FlashCards.json", "r") as file:
        flashcards = json.load(file)

    score = 0
    streak = 0
    max_streak = 0

    flashcard_items = list(flashcards.items())
    random.shuffle(flashcard_items)  # Shuffle the order for variety
    
    for word, correct_answer in flashcard_items:
        print(f"Question: {word}")
        student_answer = input("Your answer: ").strip()

        if student_answer.lower() == correct_answer.lower():
            score += 1
            streak += 1
            if streak > max_streak:
                max_streak = streak
            print("Correct!")
        else:
            streak = 0
            print(f"Incorrect! The correct answer is: {correct_answer}")

        print(f"Current Score: {score} | Current Streak: {streak}")

    print(f"\nFinal Score: {score}")
    print(f"Longest Streak: {max_streak}")
