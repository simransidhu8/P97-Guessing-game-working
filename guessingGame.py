import random
randomNumber = random.randint(0, 10)
chances = 0
while chances < 5 :
    guess = input("Guess a number between 1-9: ")
    if guess == randomNumber :
        print("YOU WON!!!")
    else:
        print("Wrong! Guess again!")
        chances = chances + 1
if chances == 5 :
    print("You lost! The number was : ", randomNumber)