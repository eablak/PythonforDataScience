import array
import numpy as np
from matplotlib import pyplot as plt


def plotting_and_saving(array, name) -> np.ndarray:
    """
    Displays and saves the given image array with the specified name.

    Args:
        array (np.ndarray): Image data to plot.
        name (str): Name used for the plot title and saved file.

    Returns:
        np.ndarray: The same input array.
    """
    plt.imshow(array)
    plt.title(name)
    plt.savefig(name + "array")
    return array


def ft_invert(array) -> array:
    """
    Invert image colors and save the result.

    Args:
        array (np.ndarray): Input image array.
    """
    inverted_array = 255 - array
    plotting_and_saving(inverted_array, "inverted")


def ft_red(array) -> array:
    """
    Keep only the red channel and save the image.

    Args:
        array (np.ndarray): RGB image array.
    """
    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    plotting_and_saving(red_array, "red")


def ft_green(array) -> array:
    """
    Keep only the green channel and save the image.

    Args:
        array (np.ndarray): RGB image array.
    """
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    plotting_and_saving(green_array, "green")


def ft_blue(array) -> array:
    """
    Keep only the blue channel and save the image.

    Args:
        array (np.ndarray): RGB image array.
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    plotting_and_saving(blue_array, "blue")


def ft_grey(array) -> array:
    """
    Convert image to greyscale and save the result.

    Args:
        array (np.ndarray): RGB image array.
    """
    array = array.copy()
    grey = np.mean(array, axis=2)
    array[:, :, 0] = grey
    array[:, :, 1] = grey
    array[:, :, 2] = grey
    plotting_and_saving(array, "grey")
