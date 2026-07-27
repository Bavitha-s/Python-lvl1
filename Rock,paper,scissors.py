import random

user_score = 0
computer_score = 0

wins = 0
losses = 0
draws = 0

user1 = input("Enter your name: ")
user2 = "Computer"

while True:

    print("Options: ")
    print("1. Rock\n2. Paper\n3. Scissors")

    user_choice = int(input("Enter your Choice (1-3): "))
    program_choice = random.randint(1, 3)

    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    elif user_choice == 3:
        user_choice = "Scissors"
    else:
        print("Invalid choice, using Rock as a default choice.")
        user_choice = "Rock"

    if program_choice == 1:
        program_choice = "Rock"
    elif program_choice == 2:
        program_choice = "Paper"
    elif program_choice == 3:
        program_choice = "Scissors"

    print("\nYou chose:", user_choice)
    print("Computer chose:", program_choice)

    if user_choice == program_choice:
        print("It's a draw!")
        draws += 1

    elif user_choice == "Rock" and program_choice == "Scissors":
        print(user1, "wins! Rock beats Scissors")
        user_score += 1
        wins += 1

    elif user_choice == "Paper" and program_choice == "Rock":
        print(user1, "wins! Paper beats Rock")
        user_score += 1
        wins += 1

    elif user_choice == "Scissors" and program_choice == "Paper":
        print(user1, "wins! Scissors beats Paper")
        user_score += 1
        wins += 1

    else:
        print(user2, "wins! Better luck next time")
        computer_score += 1
        losses += 1

    print("\nScore:")
    print(user1, ":", user_score)
    print(user2, ":", computer_score)

    again = input("\nDo you want to play again? (y/n): ")

    if again.lower() != "y":
        print("\nFinal Score:")
        print(user1, ":", user_score)
        print(user2, ":", computer_score)

        print("\nSession Totals:")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Draws:", draws)

        if wins > losses and wins > draws:
            print("Most common result: Win")
        elif losses > wins and losses > draws:
            print("Most common result: Loss")
        elif draws > wins and draws > losses:
            print("Most common result: Draw")
        else:
            print("Most common result: Tie between two or more results")

        print("Thanks for playing!")
        break
