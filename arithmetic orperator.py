"""
what is 99 + 54 = 10 
Yes, You are correct. 
No, It is 
Do you want to solve more questions? y / n 
Bugs: 
1. When ever there is a division operation it expects us to enter all the 
decimal points 
"""
import random

score = 0
lives = 3

while lives > 0:

    operators = ["+", "-", "*", "/"]

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    operator = random.choice(operators)

    question = f"Solve: {num1} {operator} {num2} = "
    answer = float(input(question))

    result = -1

    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2

    if answer == result:
        print("You're correct!")
        score += 10
    else:
        print(f"You're wrong. The correct answer is {result}")
        score -= 2
        lives -= 1


    if lives == 0:
        print("Game Over!")
        break

    choice = input("Do you want to solve one more question? (y/n): ")

    if choice.lower() != "y":
        break

print(f"Final Score: {score}")

