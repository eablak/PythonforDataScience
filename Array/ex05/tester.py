from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import cv2

array = ft_load("landscape.jpg")
inverted_array = ft_invert(array)
red_array = ft_red(array)
green_array = ft_green(array)
blue_array = ft_blue(array)
grey_array = ft_grey(array)
cv2.imshow('blue_array Image', grey_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(ft_invert.__doc__)