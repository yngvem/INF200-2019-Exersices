__author__ = "petter hetland"
__email__ = "pehe@nmbu.no"


def char_counts(textfilename):
    result = []
    infile = str(open(textfilename, "r"))
    for letter in infile:
        result[letter] = infile.count(letter)
    return infile


if __name__ == "__main__":

    filename = "file_stats.py"
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            print(
                "{:3}{:>4}{:6}".format(
                    code, chr(code) if code >= 32 else "", frequencies[code]
                )
            )
