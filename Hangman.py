import random 
import os 
import time 
animals = [
    "elephant",
    "giraffe",
    "kangaroo",
    "dolphin",
    "penguin",
    "crocodile",
    "alligator",
    "tiger",
    "leopard",
    "cheetah",
    "rabbit",
    "hamster",
    "squirrel",
    "peacock",
    "ostrich",
    "parrot",
    "flamingo",
    "octopus",
    "jellyfish",
    "butterfly"
]

fruits = [
    "apple",
    "banana",
    "orange",
    "mango",
    "grapes",
    "pineapple",
    "watermelon",
    "papaya",
    "guava",
    "strawberry",
    "blueberry",
    "raspberry",
    "kiwifruit",
    "peach",
    "pear",
    "cherry",
    "apricot",
    "coconut",
    "pomegranate",
    "dragonfruit"
]

countries = [
    "india",
    "canada",
    "brazil",
    "argentina",
    "australia",
    "germany",
    "france",
    "italy",
    "spain",
    "portugal",
    "japan",
    "china",
    "thailand",
    "vietnam",
    "singapore",
    "indonesia",
    "mexico",
    "norway",
    "sweden",
    "finland"
]

sports = [
    "cricket",
    "football",
    "basketball",
    "baseball",
    "volleyball",
    "badminton",
    "tennis",
    "hockey",
    "kabaddi",
    "swimming",
    "cycling",
    "wrestling",
    "gymnastics",
    "archery",
    "boxing",
    "fencing",
    "rowing",
    "surfing",
    "skateboarding",
    "snowboarding"
]
options="""Themes:
1. Animals 
2. Fruits 
3. Countries 
4. Sports 
"""
print(options)
choice = int(input("Enter you're choice: "))
match choice:
    case 1: 
        words = animals 
    case 2:
        words = fruits 
    case 3:
        words = countries
    case _ :
        words = sports 

word = random.sample(words,k=1)[0] #this is to choose random word from list
guess = ["_" for i in word]
drawings = [
# 0. Empty
"""
 
 
 
 
 
 
=========
""",

# 1. Vertical pole
"""
|
|
|
|
|
|
=========
""",

# 2. Vertical + Horizontal pole
"""
+------
|
|
|
|
|
=========
""",

# 3. Add rope
"""
+------
|     |
|
|
|
|
=========
""",

# 4. Add head
"""
+------
|     |
|     O
|
|
|
=========
""",

# 5. Add body
"""
+------
|     |
|     O
|     |
|     |
|
=========
""",

# 6. Add left hand
"""
+------
|     |
|     O
|    /|
|     |
|
=========
""",

# 7. Add right hand
"""
+------
|     |
|     O
|    /|\\
|     |
|
=========
""",

# 8. Add left leg
"""
+------
|     |
|     O
|    /|\\
|     |
|    /
=========
""",

# 9. Add right leg (Game Over)
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
    print("word:"," ".join(guess))
    print(drawings[drawing_count])
    # take a letter as input from user and check if it is in the list or not 
    if game_over:
        print("The man is Dead.\nGame Over...")
        print(f"Word: {word}")
        break 
    if winner:
        print("Congragulations..\nYou have won the Game..")
        break
    print(f"last Guesses: {",".join(letters)}")
    letter = input("Guess a letter: ")
    letters.append(letter)
    if letter in word:
        # print("The given letter is in the word.")
        count = word.count(letter)
        index = -1
        while count >0:
            
            index = word.index(letter,index+1) # this will only return you the 
            # first occurence in the word 
            guess[index] = letter
            if guess.count("_") == 0:
                winner = True 
                continue
            count-=1
    else:
        drawing_count += 1 
        if drawing_count == len(drawings)-1:
            game_over = True 
            
    
    time.sleep(1)
    os.system("clear")
