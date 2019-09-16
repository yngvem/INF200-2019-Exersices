import ex_01_play_func as f

# Runs the script with functions from ex_01_functions
if __name__ == "__main__":
    play = True
    while play:
        num_of_cards_dealt = 0

        # Creates a normal deck of 52 playing cards:
        deck = f.create_deck_of_cards()

        # Creates the playing board:
        current_board = f.create_board()

        # Prompts the player to start the game:
        f.prompt_start()

        # Deal the rounds
        f.deal_rounds(current_board, num_of_cards_dealt, deck)

        # Count the number of completes for the round
        num_of_completes = f.count_completes(current_board)

        play = f.play_again(play)

    # End of game
    f.end_game(num_of_completes)
