from load_image import ft_load
from matplotlib import pyplot as plt


def zoom():
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise AssertionError("Loading the image failed")
        print(img)
        zoomed_img = img[680:1080, 1150:1550, 0]
        plt.imshow(zoomed_img)
        plt.savefig("zoomed.jpeg")
        print(f"New shape after slicing: {zoomed_img.shape}")
        print(zoomed_img)
    except AssertionError as e:
        print(e)


def main():
    zoom()


if __name__ == "__main__":
    main()
