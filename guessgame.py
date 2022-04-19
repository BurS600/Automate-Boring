# This is a guess the number game.

import random

print("Hello, what is your name?")

name = input()

print( "Thats a shit name. Well, " + name + ", I am thinking of a number between 1 and 100. Let's Play")


secretNumber = random.randint(1,100)



for guessesTaken in range(1,7):
    print( "Take a guess, " + name)
    playerGuess = int(input())
    
    if playerGuess > secretNumber:
        print("Nope, your guess is too high")
    elif playerGuess < secretNumber:
        print("Nope, your guess is too low")
    else:
        break # This condition is for the correct guess!

if playerGuess == secretNumber:
    print("Good job " + name + "! You guessed my number in " + str(guessesTaken) + " guesses.")
else:
    print ("Better luck next time, the number I was thinking of was .." + str(secretNumber) + " !")
