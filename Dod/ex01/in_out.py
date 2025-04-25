def square(x: int | float) -> int | float:
    """
    Return the square of x.

    Parameters: x (int | float): The number to square.
    Returns: int | float: The squared result.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Return x raised to the power of x.

    Parameters: x (int | float): The base and exponent.
    Returns: int | float: The result of x^x.
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Returns a closure that repeatedly applies a function to a value,
    updating the value with each call.

    Parameters:
    x (int | float): Initial value.
    function (callable): Function to apply.

    Returns:
    function: A closure that applies the function and updates the value.
    """
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner
