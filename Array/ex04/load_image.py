import cv2
import numpy as np
import os


def ft_load(path: str) -> np.array:

    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith((".jpeg", ".jpg")):
            raise AssertionError("Only jpeg or jpg supported")
        return (cv2.imread(path))
    except AssertionError as e:
        print(e)
        return ""
