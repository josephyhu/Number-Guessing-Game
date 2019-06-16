# I'm only going for the "Exceeds Expectations" grade.

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random

highscore = []

print("Welcome to the number guessing game!")

def get_input():
    try:
        user_input = input("Choose a number between 1 and 10. ")
        if user_input.isdigit() == True:
            user_input = int(user_input)
            if user_input < 1 or user_input > 10:
                raise ValueError("The number is outside the range. It must be in between 1 and 10.")
        else:
            raise ValueError("It must be an integer between 1 and 10.")
    except ValueError as err:
        print("Invalid input. Please try again.")
        print("({})".format(err))
    else:
        return user_input

def start_game():
    number = random.randint(1, 10)
    tries = 0
    while True:
        guess = get_input()
        # The program gives me an error unless I put this if statement in.
        if type(guess) != int:
            continue
        tries += 1
        if guess < number:
            print("It's higher.")
        elif guess > number:
            print("It's lower.")
        else:
            print("You've guessed the correct number in {} tries!".format(tries))
            break
    if game_end() == False:
        highscore.append(tries)
        highscore.sort()
        print("The current high score is {}.".format(highscore[0]))
        start_game()
    else:
        print("Goodbye!")

def game_end():
    restart = input("Would you like to play again? (y/n) ")
    while restart.lower() != 'y' and restart.lower() != 'n':
        print("Invalid input. Please try again.")
        restart = input("Would you like to play again? (y/n) ")
    if restart.lower() == 'y':
        return False
    else:
        return True

if __name__ == '__main__':
    start_game()
