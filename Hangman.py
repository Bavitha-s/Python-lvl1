import random
import os
import time

animals = [
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin",
    "crocodile", "alligator", "tiger", "leopard", "cheetah",
    "rabbit", "hamster", "squirrel", "peacock", "ostrich",
    "parrot", "flamingo", "octopus", "jellyfish", "butterfly"
]

fruits = [
    "apple", "banana", "orange", "mango", "grapes",
    "pineapple", "watermelon", "papaya", "guava", "strawberry",
    "blueberry", "raspberry", "kiwifruit", "peach", "pear",
    "cherry", "apricot", "coconut", "pomegranate", "dragonfruit"
]

countries = [
    "india", "canada", "brazil", "argentina", "australia",
    "germany", "france", "italy", "spain", "portugal",
    "japan", "china", "thailand", "vietnam", "singapore",
    "indonesia", "mexico", "norway", "sweden", "finland"
]

sports = [
    "cricket", "football", "basketball", "baseball", "volleyball",
    "badminton", "tennis", "hockey", "kabaddi", "swimming",
    "cycling", "wrestling", "gymnastics", "archery", "boxing",
    "fencing", "rowing", "surfing", "skateboarding", "snowboarding"
]

score = 0

while True:

    print("""
Themes:
1. Animals
2. Fruits
3. Countries
4. Sports
""")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            words = animals
        case 2:
            words = fruits
        case 3:
            words = countries
        case _:
            words = sports

    print("""
Difficulty:
1. Easy (10 tries)
2. Medium (6 tries)
3. Hard (3 tries)
""")

    difficulty = int(input("Choose difficulty: "))

    if difficulty == 1:
        max_tries = 10
        points = 10
    elif difficulty == 2:
        max_tries = 6
        points = 20
    else:
        max_tries = 3
        points = 30

    word = random.choice(words)

    guess = ["_" for i in word]

    drawings = [
"""
 
 
 
 
 
 
=========
""",
"""
|
|
|
|
|
|
=========
""",
"""
+------
|
|
|
|
|
=========
""",
"""
+------
|     |
|
|
|
|
=========
""",
"""
+------
|     |
|     O
|
|
|
=========
""",
"""
+------
|     |
|     O
|     |
|     |
|
=========
""",
"""
+------
|     |
|     O
|    /|
|     |
|
=========
""",
"""
+------
|     |
|     O
|    /|\\
|     |
|
=========
""",
"""
+------
|     |
|     O
|    /|\\
|     |
|    /
=========
""",
"""
+------
|     |
|     O
|    /|\\
|     |
|    / \\
=========
"""
]

    drawing_count = 0
    game_over = False
    winner = False
    letters = []

    while True:

        print("Hangman:")
        print("Word:", " ".join(guess))

        drawing_index = min(
            int((drawing_count / max_tries) * (len(drawings) - 1)),
            len(drawings) - 1
        )

        print(drawings[drawing_index])

        if game_over:
            print("The man is dead.")
            print("Game Over!")
            print("Word:", word)
            break

        if winner:
            score += points
            print("Congratulations! You won!")
            print(f"You earned {points} points.")
            print(f"Total Score: {score}")
            break

        print(f"Previous guesses: {', '.join(letters)}")

        letter = input("Guess a letter: ").lower()

        if letter in letters:
            print("You already guessed that letter!")
            time.sleep(1)
            os.system("clear")
            continue

        letters.append(letter)

        if letter in word:

            count = word.count(letter)
            index = -1

            while count > 0:
                index = word.index(letter, index + 1)
                guess[index] = letter
                count -= 1

            if "_" not in guess:
                winner = True

        else:
            drawing_count += 1

            tries_left = max_tries - drawing_count

            print(f"Wrong guess! Tries remaining: {tries_left} / {max_tries}")

            if tries_left == 1:
                print("Careful - almost out of tries!")

            if drawing_count >= max_tries:
                game_over = True

        time.sleep(1)
        os.system("clear")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != "y":
        print(f"Final Score: {score}")
        print("Thanks for playing!")
        break
