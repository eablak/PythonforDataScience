from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    """
    Loads an image and extracts a 400x400 region from the center
    (red channel only).
    Saves the cropped region as 'zoomed.jpeg' and prints the new shape.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise AssertionError("Loading the image failed")
        print(img)
        zoomed_img = img[184:584, 312:712, 0]
        plt.imshow(zoomed_img)
        plt.savefig("zoomed.jpeg")
        print(f"New shape after slicing: {zoomed_img.shape}")
        print(zoomed_img)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
