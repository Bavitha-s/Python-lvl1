"""
length: 
1. up 
2. down 
3. left 
4. right 
Enter a direction: 3 (food/empty/wall/bomb)
"""

import random 
import os # clear the screen 
import time # adding delay 

directions = [2, 0, -1, -2]

score = 0 
hints_left = 3

options = """Directions:
1. Up 
2. Down 
3. Left 
4. Right
5. Get a Hint
"""

hint = False 
turn = True

while True: 
    print(f"Score: {score}")
    print(f"Hints remaining: {hints_left}")
    print(options)

    if turn: 
        random.shuffle(directions)

    direction = int(input("Choose your direction: "))

    if direction == 5:
        if hints_left > 0:
            hint = True
            hints_left -= 1
            turn = False 

            danger = []

            for i in range(4):
                if directions[i] == -1 or directions[i] == -2:
                    danger.append(i + 1)

            print(f"Danger: {danger[0]}, {danger[1]}")
            print(f"Hints left: {hints_left}")

        else:
            print("No hints left!")

    else:
        reward = directions[direction - 1]

        match reward:
            case -1:
                print("Hit a wall")
                print("Game End..")
                print(f"Your final Score: {score}")
                break 

            case -2:
                print("Hit a bomb")
                print("Game End..")
                print(f"Your final Score: {score}")
                break

            case 0: 
                print("No food")

            case 2:
                print("Received Food")

                if hint:
                    score += 1
                    hint = False 
                else:
                    score += 2 

        turn = True 

    time.sleep(2)
    os.system("clear")

