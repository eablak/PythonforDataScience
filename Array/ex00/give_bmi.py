def calculate_bmi(height, weight):
    return weight / (height * height)


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:

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
    results = [True if bmi[i] < limit else False for i in range(len(bmi))]
    return results
