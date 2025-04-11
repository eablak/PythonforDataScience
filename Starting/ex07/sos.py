import sys


def encode_to_morse(string):
    """
    Converts a given string into its Morse code equivalent.

    Only uppercase letters A-Z, digits 0-9, and spaces are supported.
    Any other character will raise an AssertionError.
    """
    morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', ' ': '/', }

    morse = []

    for char in string:
        if char not in morse_code:
            raise AssertionError("the arguments are bad")
        morse.append(morse_code[char])

    return " ".join(morse).rstrip()


def main():
    """
    Takes a single command-line argument and prints its Morse code equivalent.
    Raises an AssertionError if input is not alphanumeric or space.
    """
    args = sys.argv

    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        print(encode_to_morse(args[1].upper()))

    except AssertionError as e:
        print(AssertionError.__name__, ": ", e)


if __name__ == "__main__":
    main()
