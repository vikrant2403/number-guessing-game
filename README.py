# number-guessing-game
import random
the_number = random.randint(1,100)
while True:
    try:
        guess = int(input("guess the number between 1 and 100: "))
        if (guess>the_number):
            print("too large number")
        elif (guess<the_number):
            print("too small number")
        else:
            print("number matched")
            break
    except ValueError:
        print("enter a valid number")

