import sys


def analyze(text):
    """

    This script analyzes given text and prints statistic about:

    - Total lenght for text
    - Number of total uppercase letter
    - Number of total lowercase letter
    - Number of total punctuation marks
    - Number of total spaces
    - Number of total digits
    """
    len_text = len(text)
    c_upper = sum(1 for letter in text if letter.isupper())
    c_lower = sum(1 for letter in text if letter.islower())
    c_space = sum(1 for letter in text if letter.isspace())
    c_digit = sum(1 for letter in text if letter.isdigit())
    c_punctuation = sum(
        1 for letter in text
        if not (letter.isupper() or letter.islower()
                or letter.isspace() or letter.isdigit())
    )
    print(
        f"The text contains {len_text} characters:\n"
        f"{c_upper} upper letters\n"
        f"{c_lower} lower letters\n"
        f"{c_punctuation} punctuation marks\n"
        f"{c_space} spaces\n{c_digit} digits"
    )


def main():

    """
Analyzes the given text and print it.
If string have lower letters, upper letters,
punctuation marks, spaces and digits.
This program analyzes and show them.
    """

    args = sys.argv

    try:
        if (len(args) == 1):
            text = ""
            try:
                while text == "":
                    text = input("What is the text to count?\n")
                    text += "\n"
                analyze(text)
            except EOFError:
                pass
        elif (len(args) == 2):
            analyze(args[1])
        elif (len(args) > 2):
            raise AssertionError("Too many arguments provided")
    except AssertionError as e:
        print(AssertionError.__name__, ":", e)


if __name__ == "__main__":
    main()
