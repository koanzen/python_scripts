# this a guess a number game

from random import randint

name = input("What is your name: ")

secretNum = randint(1,20)

print(f"Well {name} I'm thinking a number between 1 and 20")


for i in range(1,7):
    guess = int(input("Guess a number: "))
    if guess < secretNum:
        print("Your number is lower than my number.")
    elif guess > secretNum:
        print("Your number is greater than my number.")
    else:
        break

if guess == secretNum:
    print(f"{name} You guess my number in {i} guesses.")
else:
    print(f"The number I was thinking is {secretNum}")
