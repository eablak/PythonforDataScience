import sys
from ft_filter import ft_filter


def main():
    """
Processes command-line arguments and filters words based on length.

Expects exactly two arguments:
- A string of alphabetic words (space-separated)
- An integer 'n'

The function filters and prints words from the string
that are longer than 'n' characters.
    """

    args = sys.argv

    try:
        if (len(args) != 3):
            raise AssertionError("Bad argument count")
        else:
            text = args[1]
            n = int(args[2])

            if not isinstance(text, str) or not isinstance(n, int):
                raise AssertionError("Incompatible argument")
            if any(not word.isalpha() for word in text.split()):
                raise AssertionError("Bad argument for string")
            result = list(ft_filter(lambda text: len(text) > n, text.split()))
            print(result)

    except ValueError as v:
        print(ValueError.__name__, ":", v)
    except AssertionError as e:
        print(AssertionError.__name__, ":", e)


if __name__ == "__main__":
    print(filter.__doc__)
    print(ft_filter.__doc__)
    main()
