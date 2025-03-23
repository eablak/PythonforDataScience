import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        if not (
            isinstance(family, list) or
            not all(isinstance(row, list) for row in family)
        ):
            raise AssertionError("Family must be list of list")
        if any(len(family[0]) != len(row) for row in family):
            raise AssertionError("List size must be same")

        print("My shape is :", np.array(family).shape)
        print("My new shape is :", np.array(family)[start:end].shape)
        return np.array(family)[start:end].tolist()
    except AssertionError as e:
        print(e)
