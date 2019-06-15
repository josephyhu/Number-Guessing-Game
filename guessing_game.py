# I'm going for "Exceeds Expectations" grade, but I'm fine with "Meets Expectations" grade.

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

high_score = []
print("Welcome to the number guessing game!")
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
    tries = 0
    while True:
        guess = input("Choose a number between 1 and 10. ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if guess < 1 or guess > 10:
                print("The number is outside the range. Please try again.")
            elif guess < number:
                print("It's higher.")
                tries += 1
            elif guess > number:
                print("It's lower.")
                tries += 1
            else:
                tries += 1
                break
    high_score.append(tries)
    print("You've guessed the correct number in {} tries!".format(tries))
    restart = input("Would you like to play again? (y/n) ")
    while restart.lower() != 'y' and restart.lower() != 'n':
        print("Invalid input. Please try again.")
        restart = input("Would you like to play again? (y/n) ")
    if restart.lower() == 'y':
        i = 0
        while i <= len(high_score) - 1:
            if high_score[i] <= high_score[i - 1]:
                print("The current high score is {}.".format(high_score[i]))
                start_game()
            else:
                print("The current high score is {}.".format(high_score[i - 1]))
                start_game()
            i += 1
    else:
        print("Goodbye!")
        exit()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
