__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"


# TASK A
SUITS = ("C", "S", "H", "D")
VALUES = range(1, 14)


def deck_loop():  # Problem solved using loops
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():  # Problem solved using loops
    deck_by_comp = [(suit, val) for suit in SUITS for val in VALUES]
    return deck_by_comp
