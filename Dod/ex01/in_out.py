def square(x: int | float) -> int | float:
    """
    Return the square of x.

    Parameters:
    x (int | float): The number to square.

    Returns:
    int | float: The squared result.
    """
    return x*x


def pow(x: int | float) -> int | float:
    """
    Return x raised to the power of x.

    Parameters:
    x (int | float): The base and exponent.

    Returns:
    int | float: The result of x^x.
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Return a closure that applies the given function to x,
    using the previous result for subsequent calls.

    Parameters:
    x (int | float): The initial value.
    function (callable): The function to apply.

    Returns:
    function: A closure that applies the function and updates the result.
    """
    count = 0

    def inner() -> float:
        """
        Apply the function to x or the previous result.

        Returns:
        float: The result of applying the function.
        """
        nonlocal count
        if count == 0:
            result = function(x)
        else:
            result = function(inner.previus_result)
        inner.previus_result = result
        count += 1
        return result

    return inner
