def callLimit(limit: int):
    """
    A decorator factory that limits the
    number of times a function can be called.

    Parameters: limit (int): The maximum number of allowed calls.
    Returns: function: A decorator that enforces the call limit.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call to many times")
            else:
                return function(*args, **kwds)
        return limit_function
    return callLimiter
