# I'm going for "Exceeds Expectations" grade, but I'm fine with "Meets Expectations" grade.

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

print("Welcome to the number guessing game!")

def get_input():
    user_input = input("Choose a number between 1 and 10. ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please try again.")
    else:
        if user_input < 1 or user_input > 10:
            print("The number is outside the range. Please try again.")
        else:
            return user_input

def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    number = random.randint(1, 10)
    high_score = 0
    tries = 0
    while True:
        guess = get_input()
        # The program gives me an error unless I put this first if statement in.
        if type(guess) != int:
            continue
        elif guess > number:
            print("It's lower.")
        elif guess < number:
            print("It's higher.")
        else:
            tries += 1
            break
        tries += 1
    print("You've guessed the correct number in {} tries!".format(tries))
    restart = input("Would you like to play again? (y/n) ")
    while restart.lower() != 'y' and restart.lower() != 'n':
        print("Invalid input. Please try again.")
        restart = input("Would you like to play again? (y/n) ")
    if restart.lower() == 'y':
        if high_score == 0 or tries < high_score:
            high_score = tries
            print("The current high score is {}.".format(high_score))
        start_game()
    else:
        print("Goodbye!")
        exit()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
