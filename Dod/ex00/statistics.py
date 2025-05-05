def calculate_mean(numbers:  list):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list of int|float): The numbers to average.

    Returns:
        float: The mean value.
    """
    return sum(numbers) / len(numbers)


def calculate_median(numbers: list):
    """
    Find the median (middle) value of a list of numbers.
    If there is an even number of items,
    returns the sum of the two middle values.

    Args:
        numbers (list of int|float): The numbers to check.

    Returns:
        float: The median or sum of middle values.
    """
    numbers.sort()
    median = 0
    n = len(numbers)

    if len(numbers) % 2 != 0:
        median = numbers[(n - 1) // 2]
    else:
        median = (numbers[(n - 1) // 2] + numbers[n // 2]) / 2
    return median


def calculate_quartile(numbers: list):
    """
    Get the first (Q1) and third (Q3) quartiles of a list.

    Args:
        numbers (list of int|float): The data list.

    Returns:
        list of float: [Q1, Q3].
    """
    numbers.sort()
    n = len(numbers)

    q = []
    q1_index = n * 0.25
    q3_index = n * 0.75

    if q1_index.is_integer():
        q1_index = int(q1_index)
        q.append(float((numbers[q1_index - 1] + numbers[q1_index]) / 2))
    else:
        q.append(float(numbers[int(q1_index)]))

    if q3_index.is_integer():
        q3_index = int(q3_index)
        q.append(float((numbers[q3_index - 1] + numbers[q3_index]) / 2))
    else:
        q.append(float(numbers[int(q3_index)]))

    return q


def calculate_std(numbers: list):
    """
    Compute the population standard deviation of a list.

    Args:
        numbers (list of int|float): The data list.

    Returns:
        float: Standard deviation.
    """
    mean_value = calculate_mean(numbers)
    variance = sum([(i - mean_value) ** 2 for i in numbers])
    return (variance / len(numbers)) ** (1/2)


def calculate_var(numbers: list):
    """
    Compute the population variance of a list.

    Args:
        numbers (list of int|float): The data list.

    Returns:
        float: Variance.
    """
    mean = calculate_mean(numbers)
    variance = sum([(i - mean) ** 2 for i in numbers])
    return (variance / len(numbers))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Print requested stats (mean, median, quartile, std, var) for given numbers.

    Usage:
        ft_statistics(1, 2, 3, mean="mean", var="var")

    Args:
        *args: Numbers to process.
        **kwargs: Keys matching stats names:
            mean, median, quartile, std, var

    Returns:
        None
    """
    if args:
        for k, val in kwargs.items():
            if val == "mean":
                print("mean : ", calculate_mean(list(args)))
            elif val == "median":
                print("median : ", calculate_median(list(args)))
            elif val == "quartile":
                print("quartile : ", calculate_quartile(list(args)))
            elif val == "std":
                print("std : ", calculate_std(list(args)))
            elif val == "var":
                print("var : ", calculate_var(list(args)))
            else:
                break
    else:
        print("ERROR\n" * len(kwargs.items()))
