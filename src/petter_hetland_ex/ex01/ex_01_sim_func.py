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


# Draws a random card from the remainder of the deck:
def draw(num_of_cards_dealt):
    random_card = r(0, (52 - num_of_cards_dealt - 1))
    return random_card


# Deals rounds:
def deal_rounds(current_board, num_of_cards_dealt, deck):
    while num_of_cards_dealt < 52:
        try:
            # Deal new round
            for i, value in current_board.items():
                if value != "Complete":
                    current_board[i] = deck[draw(num_of_cards_dealt)]
                    deck.remove(current_board[i])
                    num_of_cards_dealt += 1
                elif value == "Complete":
                    continue
        except ValueError:
            continue
        # Searches for and marks completed positions
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


# Counts the number of complete positions on the board:
def count_completes(num_of_completes, current_board):
    for i, value in current_board.items():
        if current_board[i] == "Complete":
            num_of_completes += 1
        else:
            continue
    return num_of_completes


# Adds a win or loss to the out variables based on result:
def count_wins(num_of_completes, wins, losses):
    if num_of_completes == 12:
        wins += 1
    elif 12 > num_of_completes >= 0:
        losses += 1
    else:
        print("Error")
    return wins, losses


# Calculates the chances of winning and prints the result of the sim:
def sim_result(wins, losses, num_of_sims):
    chance_of_winning = float((wins / losses) * 100)
    print(
        "--- Simulation complete ---\nThe chance of winning is {0:.5f}%".format(
            chance_of_winning
        )
    )
    print("- Based on {:1} simulations".format(num_of_sims))
    print("- Total amount of wins: {}".format(wins))
    print("- Total amount of losses: {}".format(losses))
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
