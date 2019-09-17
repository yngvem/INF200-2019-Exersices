from random import shuffle

__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"


def play_game():
    """Play a single game of modified clock patience.

    Returns
    -------
    win: bool
        True if the game resulted in a win and False otherwise
    """
    cards = create_deck_of_cards()
    shuffle(cards)
    board = create_board()
    while len(cards) > 0:
        cards, board = play_one_round(cards, board)
        if is_winning_state(board):
            return True

    return False


def create_deck_of_cards():
    """Creates a normal deck of 52 playing cards, in form of a list with 2-tuples.
    """
    suits = ["C", "S", "H", "D"]
    deck = [(suit, val) for suit in suits for val in range(1, 14)]
    return deck


def create_board():
    """ Creates a playing board with 13 empty positions in the form of 2-tuples.
    """
    board = [(None, None) for _ in range(13)]
    return board


def play_one_round(cards, board):
    """Play a single round of clock patience.
    For each position, check if that position is locked,
    If it is locked, skip that position (continue),
    Otherwise deal a card.
    """
    for position, board_state in enumerate(board):
        if board_state[1] == position + 1:
            continue
        elif len(cards) == 0:
            break

        board[position] = cards.pop()
    return cards, board


def is_winning_state(board):
    """Returns True if the board is in a winning state and False otherwise.
    """
    for position, board_state in enumerate(board):
        if board_state[1] != position + 1:
            return False
    return True


def game_finished(cards, board):
    """Returns True if the game is over and False otherwise
    """
    return is_winning_state(board) or len(cards) == 0


def play_n_games(n):
    """Returns the number of times won after ``n`` games.
    """
    results = [play_game() for _ in range(n)]
    return (sum(results) / n) * 100


if __name__ == "__main__":
    """Runs the function "play_n_games()" to simulate calling "play_game()" n number of times.
    
    Returns:
    ------------
    Number of times the player won the game out of n tries.
    """
    print(
        "The chance of winning the game is: "
        + str(play_n_games(100000))
        + " percent."
    )
