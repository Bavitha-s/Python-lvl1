details="""+--------------+--------------+
|   Space Expert Chat Bot     |
+--------------+--------------+
|    Version   |    3         |
+--------------+--------------+
|    Made by   |    Bavitha   |
+--------------+--------------+"""
print(details)


question1 = "What is the closest planet to the Sun?"
answer1 = "Mercury"

question2 = "Which planet is known as the Red Planet?"
answer2 = "mars"

question3 = "What is the largest planet in our solar system?"
answer3 = "Jupiter"

question4 ="True or False: Earth is the third planet from the Sun."
answer4 = "True"

question5 = "Which planet is famous for its bright, prominent ring system?"
answer5 = "Saturn"

question6 = "What force keeps the planets in orbit around the Sun?"
answer6 = "Gravity"

question7 = "Is the Moon a planet, a star, or a natural satellite?"
answer7 = " A natural satellite"

question8 = "Which planet is known for being the hottest in the solar system?"
answer8 = "Venus"

question9 = "What object sits at the center of our solar system?"
answer9 = "The sun"

question10 = "Which dwarf planet used to be considered the ninth main planet?"
answer10 = "Pulto"

while True: # never going to end 
    prompt = input("Prompt: ")
    
    if prompt.lower().replace(" ","") in question1.lower().replace(" ",""):
        print("Response:",answer1)
    elif prompt.lower().replace(" ","") in question2.lower().replace(" ",""):
        print("Response:",answer2)
    elif prompt.lower().replace(" ","") in question3.lower().replace(" ",""):
        print("Response:",answer3)
    elif prompt.lower().replace(" ","") in question4.lower().replace(" ",""):
        print("Response:",answer4)
    elif prompt.lower().replace(" ","") in question5.lower().replace(" ",""):
        print("Response:",answer5)
    elif prompt.lower().replace(" ","") in question6.lower().replace(" ",""):
        print("Response:",answer6)
    elif prompt.lower().replace(" ","") in question7.lower().replace(" ",""):
        print("Response:",answer7)
    elif prompt.lower().replace(" ","") in question8.lower().replace(" ",""):
        print("Response:",answer8)
    elif prompt.lower().replace(" ","") in question9.lower().replace(" ",""):
        print("Response:",answer9)
    elif prompt.lower().replace(" ","") in question10.lower().replace(" ",""):
        print("Response:",answer10)
    elif prompt.lower() == "exit" or prompt.lower() == "quit":
        print("Exiting the application....")
        break 
    else:
        print("Response: Sorry I couldn't answer your question.")
    
    print("-"*20)





