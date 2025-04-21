def calculate_bmi(height, weight):
    """
    Calculate BMI using height and weight.

    :param height: Height in meters (float or int).
    :param weight: Weight in kilograms (float or int).
    :return: Calculated BMI value (float).
    """
    return weight / (height * height)


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI for each pair in height and weight lists.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """
    bmi_values = []
    try:
        if (len(height) != len(weight)):
            raise ValueError("List size are not same")
        if not all(isinstance(value, (int, float)) for value in height):
            raise AssertionError("Height list must be int or float")
        if not all(isinstance(value, (int, float)) for value in weight):
            raise AssertionError("Weight list must be int or float")

        for i in range(len(height)):
            bmi_values.append(calculate_bmi(height[i], weight[i]))
    except ValueError as e:
        print(e)

    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values with a limit and return boolean results.

    :param bmi: List of BMI values.
    :param limit: Limit value for comparison.
    :return: List of booleans where True means BMI is below the limit.
    """
    results = [True if bmi[i] < limit else False for i in range(len(bmi))]
    return results
