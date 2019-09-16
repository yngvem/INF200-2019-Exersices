""" Task C: Counting letters"""


def letter_freq(txt):

    txt_lower = txt.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '?', ',',
                '.', '+', '-', '_', '&', '%', '(', ')', '"', ':']

    txt_dictionary = {}

    for letter in range(len(alphabet)):
        if txt_lower(alphabet[letter]) != 0:
            txt_dictionary[alphabet[letter]] = [txt_lower.count[letter]]

    return txt_dictionary


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
