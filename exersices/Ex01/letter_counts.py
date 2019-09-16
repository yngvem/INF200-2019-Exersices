def letter_freq(txt):
    liten = txt.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?',
             '!']
    result = {}
    for i in range(0, 31):
        if liten.count(alpha[i]) != 0:
            result[alpha[i]] = liten.count(alpha[i])
    print(result)

    return result


letter_freq('BiggerAndLower')


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
