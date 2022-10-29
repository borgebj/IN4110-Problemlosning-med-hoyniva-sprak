"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale
    Uses pure python with to grayscale image and numpy to store the image in an array
    Includes the use of double for loops to access the "height" and "width" of the image via indexing,
    then choosing manually the "depth" of the image, aka the color channels.

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    height = image.shape[0]
    width = image.shape[1]
    depth = image.shape[2]

    # iterates through the pixels, and apply the grayscale transform
    # since we know c=3 in (w, h, c), we can specify each channel with 0, 1 and 2
    for i in range(height):
        for j in range(width):
            red = image[i, j, 0] * 0.21
            green = image[i, j, 1] * 0.72
            blue = image[i, j, 2] * 0.07
            pixel = (red + green + blue)

            # k = current color channel
            for k in range(depth):
                gray_image[i, j, k] = pixel

    # returns and ensures correct datatype
    return gray_image.astype("uint8")


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia
    Uses pure python to add a vintage sepia-filter a given image and return it.
    Implementation loops through the array,
    and multiply each color value in the corresponding channel of a pixel with the RGB ordered sepia_matrix

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """

    # empty copy to operate on
    sepia_image = np.empty_like(image)

    height = image.shape[0]
    width = image.shape[1]
    depth = image.shape[2]
    sepia_matrix = [
        [0.393, 0.769, 0.189],  # 0
        [0.349, 0.686, 0.168],  # 1
        [0.272, 0.534, 0.131],  # 2
    ]     # 0    # 1    # 2

    # Iterates through the pixels and applies the sepia matrix
    # iterates through all color channels to multiply them with their matrix-values
    for i in range(height):
        for j in range(width):
            red = image[i, j, 0]
            green = image[i, j, 1]
            blue = image[i, j, 2]

            # k = current color channel
            for k in range(depth):
                pixel = (red * sepia_matrix[k][0]) + \
                        (green * sepia_matrix[k][1]) + \
                        (blue * sepia_matrix[k][2])

                # # assigns value and maxes value at 255
                sepia_image[i, j, k] = min(pixel, 255)

    # returns and ensures correct datatype
    return sepia_image.astype("uint8")
