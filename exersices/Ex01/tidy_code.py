from random import randint

__author__ = 'Sebastian Kihle'
__email__ = 'sebaskih@nmbu.no'


def guess_bigger_than_0():
    guess = 0
    while guess < 2:
        guess = int(input('Your guess: '))
    return guess


def throw_2_dice():
    return randint(1, 6) + randint(1, 6)


def check_correct(f, g):
    return f == g


if __name__ == '__main__':

    match = False
    guesses = 3
    throw = throw_2_dice()
    while not match and guesses > 0:
        your_guess = guess_bigger_than_0()
        match = check_correct(throw, your_guess)
        if not match:
            print('Wrong, try again!')
            guesses -= 1

    if guesses > 0:
        print('You won {} points.'.format(guesses))
    else:
        print('You lost. Correct answer: {}.'.format(throw))
