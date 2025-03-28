import array
import numpy as np


def ft_invert(array) -> array:
    inverted_array = 255 - array
    return inverted_array


def ft_red(array) -> array:
    red_array = array.copy()
    red_array[:, :, 0] = 0
    red_array[:, :, 1] = 0
    return red_array


def ft_green(array) -> array:
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    return green_array


def ft_blue(array) -> array:
    blue_array = array.copy()
    blue_array[:, :, 1] = 0
    blue_array[:, :, 2] = 0
    return blue_array


def ft_grey(array) -> array:
    array = array.copy()
    grey = np.mean(array, axis=2)
    array[:, :, 0] = grey
    array[:, :, 1] = grey
    array[:, :, 2] = grey
    return array
