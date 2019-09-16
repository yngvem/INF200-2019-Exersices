import ex_01_sim_func as f
from random import randint as r

__author__ = "Petter Hetland"
__email__ = "pehe@nmbu.no"


# Runs the script with functions from ex_01_functions
if __name__ == "__main__":
    # Variables for full sim
    num_of_sims = 0
    wins = 0
    losses = 0

    while num_of_sims < 100000:  # Select number of simulations with a maximum of 500k
        # Variables for each sim
        num_of_cards_dealt = 0
        num_of_completes = 0

        # Create a basic deck of cards
        deck = f.create_deck_of_cards()

        # Create playing board
        current_board = f.create_board()

        # Deals the following rounds and marks completed positions
        f.deal_rounds(current_board, num_of_cards_dealt, deck)

        # Count completed positions
        num_of_completes = f.count_completes(num_of_completes, current_board)

        # Check board for result
        wins, losses = f.count_wins(num_of_completes, wins, losses)

        num_of_sims += 1

    # Print simulation result
    f.sim_result(wins, losses, num_of_sims)
