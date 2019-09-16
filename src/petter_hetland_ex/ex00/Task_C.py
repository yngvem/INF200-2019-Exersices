__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"

# TASK C
# The script returns a count of each letter in the given word in an alphabetical order
letter_count = {}


def letter_freq(txt):
    letters = list(txt.lower())
    letters.sort()

    for item in letters:
        letter_count[item] = letters.count(letter)
    return letter_count


if __name__ == "__main__":
    text = input("Please enter text to analyse: ")
    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print("{:3}{:10}".format(letter, count))
