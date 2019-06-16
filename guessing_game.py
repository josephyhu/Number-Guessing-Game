# I'm going for "Exceeds Expectations" grade, but I'm fine with "Meets Expectations" grade.

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random

print("Welcome to the number guessing game!")

def get_input():
    user_input = input("Choose a number between 1 and 10. ")
    try:
        user_input = int(user_input)
        if user_input < 1 or user_input > 10:
            raise ValueError("The number is outside the range.")
    except ValueError as err:
        print("Invalid input. Please try again.")
        print("({})".format(err))
    else:
        return user_input

def start_game():
    number = random.randint(1, 10)
    high_score = 0
    tries = 0
    while True:
        guess = get_input()
        if type(guess) != int:
            continue
        else:
            tries += 1
            if guess > number:
                print("It's lower.")
            elif guess < number:
                print("It's higher.")
            else:
                print("You've guessed the correct number in {} tries!".format(tries))
                break
    restart_game()

def restart_game():
    restart = input("Would you like to play again? (y/n) ")
    while restart.lower() != 'y' and restart.lower() != 'n':
        print("Invalid input. Please try again.")
        restart = input("Would you like to play again? (y/n) ")
    if restart.lower() == 'y':
        start_game()
    else:
        print("Goodbye!")
        exit()


if __name__ == '__main__':
    start_game()
