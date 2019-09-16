# Imports
from random import randint as r

__author__ = "Petter Hetland"
__email__ = "pehe@nmbu.no"


# Creates a normal deck of 52 cards:
def create_deck_of_cards():
    SUITS = ["C", "S", "H", "D"]
    VALUES = range(1, 14)
    deck = [(suit, val) for suit in SUITS for val in VALUES]
    return deck


# Creates the playing board with 13 positions:
def create_board():
    current_board = {}
    positions = range(1, 14)
    for position in positions:
        current_board[position] = "Blank"
    return current_board


# Deal new round
def deal_rounds(current_board, num_of_cards_dealt, deck):
    while num_of_cards_dealt < 52:
        try:
            # Deal new round:
            for i, value in current_board.items():
                if value != "Complete":
                    current_board[i] = deck[draw(num_of_cards_dealt)]
                    deck.remove(current_board[i])
                    num_of_cards_dealt += 1
                elif value == "Complete":
                    continue
            # Prints the state of the playing board:
            print_board(current_board, num_of_cards_dealt)
            # Prompt the user to deal new round:
            prompt_continue()
        except ValueError:  # Allows cards to be dealt when len(deck) < 13
            continue
        # Searches for and marks completed positions:
        for i, value in current_board.items():
            if (
                value == ("D", i)
                or value == ("C", i)
                or value == ("S", i)
                or value == ("H", i)
            ) and i != 13:
                current_board[i] = "Complete"
            else:
                pass
    # Prints the state of the playing board:
    print_board(current_board, num_of_cards_dealt)


# Searches for - and marks - completed positions:
def mark_complete(current_board):
    for i, value in current_board.items():
        if (
            value == ("D", i)
            or value == ("C", i)
            or value == ("S", i)
            or value == ("H", i)
        ) and i != 13:
            current_board[i] = "Complete"
        else:
            pass


# Draws a random card from the remainder of the deck:
def draw(num_of_cards_dealt):
    random_card = r(0, (52 - num_of_cards_dealt - 1))
    return random_card


# Count num of completes:
def count_completes(current_board):
    num_of_completes = 0
    for i, value in current_board.items():
        if current_board[i] == "Complete":
            num_of_completes += 1
        else:
            continue
    print("Number of completes: {}".format(num_of_completes))
    return num_of_completes


# Prints the state of the playing board:
def print_board(current_board, num_of_cards_dealt):
    separator("long")
    for i, value in current_board.items():
        print("{}: {}".format(i, value))
    print("\nCards dealt: {}".format(num_of_cards_dealt))


# Starts the game on press enter:
def prompt_start():
    prompt = True
    separator("d_long")
    while prompt:
        press = input("Press enter to start the game")
        if press == "":
            prompt = False
        else:
            print("Please press enter")


# Pauses the game until the player continues:
def prompt_continue():
    prompt = True
    separator("short")
    while prompt:
        press = input("Press enter to continue")
        if press == "":
            prompt = False
        else:
            print("Please press enter to continue")


# Prompts the player to play again or not:
def play_again(play):
    prompt = True
    while prompt:
        ask = input("Do you want to play again? \n")
        separator("short")
        if ask == "y":
            play = True
            prompt = False
        elif ask == "n":
            play = False
            prompt = False
        else:
            print("\nPlease enter y or n\n")
    return play


# Prints end statement:
def end_game(num_of_completes):
    print(
        "The game is done! Your score was {}/12 points.".format(
            num_of_completes
        )
    )
    separator("d_long")


# Aesthetic separators:
def separator(length):
    if length == "long":
        print("\n-----------------\n")
    elif length == "short":
        print("\n--------\n")
    elif length == "d_long":
        print("\n-----------------")
        print("-----------------\n")
