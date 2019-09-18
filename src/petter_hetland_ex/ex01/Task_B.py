__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"


# TASK B
def squares_by_comp(n):  # Problem solved using list comprehension
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):  # Problem solves using loops
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares
