import cv2
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    Load a JPEG image from the given path and convert it to RGB format.

    :param path: Path to the image file.
    :return: Numpy array of the image in RGB format,
    or an empty string on error.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith((".jpeg", ".jpg")):
            raise AssertionError("Only jpeg or jpg supported")
        img = cv2.imread(path)
        rgb_format = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return (np.array(rgb_format))
    except AssertionError as e:
        print(e)
        return ""
