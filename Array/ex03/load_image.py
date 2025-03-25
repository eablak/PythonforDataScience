import cv2
import numpy as np
import os


def ft_load(path: str) -> np.array:

    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith((".jpeg", ".jpg")):
            raise AssertionError("Only jpeg or jpg supported")
        img = cv2.imread(path)  # read as a blue gran red
        print(f"The shape of image is: {img.shape}")
        rgb_format = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert to rgb
        return (np.array(rgb_format))
    except AssertionError as e:
        print(e)
        return ""
