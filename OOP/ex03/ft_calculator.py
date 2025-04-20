class calculator:

    def __init__(self, object: list):
        """Initialize with a list of numbers."""
        self.object = object

    def __add__(self, object) -> None:
        """
        Add a number to each element of the list.

        :param object: The number to add (int or float).
        """
        self.object = [i+object for i in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """
        Subtract a number from each element of the list.

        :param object: The number to subtract (int or float).
        """
        self.object = [i-object for i in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """
        Multiply each element of the list by a number.

        :param object: The number to multiply with (int or float).
        """
        self.object = [i*object for i in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """
        Divide each element of the list by a number.

        :param object: The number to divide by (int or float).
        """
        try:
            self.object = [i // object for i in self.object]
        except ZeroDivisionError:
            print("You cant divide zero")
