'''
Number Guessing Game: 
1. It will randomly generate a number between 1 to 100 
2. It will ask the user to guess the number 
3. if it is greater than the actual value the it will print 
"Too Big, Try a small number."
4. if it is samaller than the actual value then it will print 
"Too Small, Try a bigger number."
5. if your guess is correct it will print "Your guess is correct."

'''
import random 
number = random.randint(1,100) # this will generate random number between 1 to 100 

while True: # infinite loop it never ends 
    # here we need to take the number as input 
    guess = int(input("Guess the number: "))
    if guess > number: 
        print("Too Big, Try a smaller number.")
    elif guess < number: 
        print("Too Small, Try a bigger number.")
    else:
        print("Your guess is correct")
        # control statements -> break , continue 
        break 
print("Game End...")
    
    
