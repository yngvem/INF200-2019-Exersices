""" Task D: Tidy code"""

from random import randint

__author__ = ''
__email__ = '@nmbu.no'


def your_guess():
    guess = 0
    while guess < 2:
        guess = int(input('Your guess: '))
    return guess


def throw_dices():
    return randint(1, 6) + randint(1, 6)


def test_guess(dices, guess):
    return dices == guess


if __name__ == '__main__':

    matching_eyes = False
    points = 3
    dices = throw_dices()

    while not matching_eyes and points > 0:
        guess = your_guess()
        matching_eyes = test_guess(dices, guess)

        if not matching_eyes:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(dices))