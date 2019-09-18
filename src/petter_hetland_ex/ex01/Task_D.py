from random import randint as r

__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"


# TASK D
# Functions for task D:
def your_guess():  # Let's the player enter a guess
    prompt_guess = True
    while prompt_guess:
        player_guess = int(input("Your guess:\n"))
        if type(player_guess) == int and player_guess < 13:
            prompt_guess = False
        elif type(player_guess) != int:
            print("Please enter a valid number between 2 and 12")
        else:
            print("Error. Please try again.")
    return player_guess


def random_num():  # Generates a target number between 2 and 12
    random = r(1, 6) + r(1, 6)
    return random


def result(target_number, guess):  # Checks whether the guess is correct
    return target_number == guess


def start_message():
    print("---------------")
    print("Enter a valid number between 2 and 12.")


if __name__ == "__main__":
    play = True
    points = 0
    ask = 0
    while play:  # Loop that allows the player to retry the game
        # Starting values
        success = False
        tries_left = 3
        attempts = 0
        target_num = random_num()
        start_message()
        # Checks the result and tracks number of attempts
        while not success and tries_left > 0:
            guess = your_guess()  # Runs input code
            success = result(target_num, guess)  # Checks result
            if not success:  # Gives feedback and subtracts an attempt
                print("Wrong, try again!")
                print("-------")
                tries_left -= 1
                attempts += 1
            else:  # Except statement handles a blank input
                continue

        if (
            tries_left > 0
        ):
            points += tries_left  # Adds points
            # Success message
            print("---------------")
            print("You guessed correctly!)")
            print(
                f"You made {attempts} attempt(s)",
                f"and won {tries_left} point(s)."
                )
            print("You now have {} point(s).".format(points))
            print("---------------")
        else:
            # Failure message
            print("---------------")
            print("You lost. Correct answer: {}.".format(target_num))
            print("---------------")

        prompt_play_again = True
        while prompt_play_again:
            answer = input("Would you like to try again? [y/n]\n")
            if answer == "y":
                prompt_play_again = False
                continue
            elif answer == "n":
                prompt_play_again = False
                play = False
            else:
                print("Please enter 'y' or 'n'.")
                prompt_play_again = True

    # Exit statement
    print("---------------")
    print("Thank you for playing! Your final score was {}.".format(points))
    print("---------------")
