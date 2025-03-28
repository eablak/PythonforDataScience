from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def rotate_img(img):

    height, weight = len(img), len(img[0])
    new_matris = np.array([[0] * height for _ in range(weight)])

    for i in range(height):
        for j in range(weight):
            new_matris[weight-j-1][i] = img[i][j]
    return new_matris


def rotate():
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise AssertionError("Loading the image failes")
        zoomed_img = img[680:1080, 1150:1550, 0]
        print(f"New shape after slicing: {zoomed_img.shape}")
        print(zoomed_img)

        rotated_img = rotate_img(zoomed_img)
        print(f"New shape after slicing: {rotated_img.shape}")
        print(rotated_img)
        plt.imshow(rotated_img, cmap="gray")
        plt.title("Rotated Image")
        plt.savefig("rotated.jpeg")
    except AssertionError as e:
        print(e)


def main():
    rotate()


if __name__ == "__main__":
    main()
