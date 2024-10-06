import sys

args = sys.argv
largs = len(args)

try:
    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    if len(args) == 2:
        assert isinstance(int(args[1]), int)
        if int(args[1])%2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("AssertionError: argument is not an integer")