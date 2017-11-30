"Rock Paper Scissors"

# add plau again feature
# add scores for both the computer and the player
# add main menu
import random
import time
import sys


def randNum():
    choice = random.randint(1, 3)
    if choice == 1:
        time.sleep(1)
        print("Computer plays Rock")
    elif choice == 2:
        time.sleep(1)
        print("Computer plays Paper")
    elif choice == 3:
        time.sleep(1)
        print("Computer plays Scissors")
    return choice


def whoWins(userChoice, aiChoice):
    states = ["You win", "You lose", "Draw!"]
    if userChoice == aiChoice:
        time.sleep(1)
        return states[2]
    elif userChoice == 1 and aiChoice == 2:
        time.sleep(1)
        print("Rock beats Paper")
        time.sleep(1)
        return states[0]
    elif userChoice == 1 and aiChoice == 3:
        time.sleep(1)
        print("Rock beats Scissors")
        return states[0]
    elif userChoice == 2 and aiChoice == 1:
        time.sleep(1)
        print("Paper beats Rock")
        return states[0]
    elif userChoice == 2 and aiChoice == 3:
        time.sleep(1)
        print("Scissors beats Paper")
        return states[1]
    elif userChoice == 3 and aiChoice == 1:
        time.sleep(1)
        print("Rock beats Scissors")
        return states[1]
    elif userChoice == 3 and aiChoice == 2:
        time.sleep(1)
        print("Scissors beats Paper")
        return states[0]


def userPlayed(userChoice):
    if userChoice == 1:
        time.sleep(1)
        print("You played Rock!")
        return
    elif userChoice == 2:
        time.sleep(1)
        print("You played Paper!")
        return
    elif userChoice == 3:
        time.sleep(1)
        print("You played Scissors!")
        return


def userInput():
    userChoice = int(input("Please enter your choice: "))
    return userChoice


def main():
    userIn = userInput()
    userPlayed(userIn)
    compChoice = randNum()
    print(whoWins(userIn, compChoice))


main()

