"""numba-optimized filters"""
from numba import jit
import numpy as np


@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Converts rgb pixel array to grayscale

    Uses python implementation from python_filters,
    but this time using @jit -decorator.

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    height = image.shape[0]
    width = image.shape[1]
    depth = image.shape[2]

    for i in range(height):
        for j in range(width):
            red = image[i, j, 0] * 0.21
            green = image[i, j, 1] * 0.72
            blue = image[i, j, 2] * 0.07
            pixel = (red + green + blue)

            for k in range(depth):
                gray_image[i, j, k] = pixel

    return gray_image.astype("uint8")


@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)

    height = image.shape[0]
    width = image.shape[1]
    depth = image.shape[2]
    sepia_matrix = [
        [0.393, 0.769, 0.189],  # 0
        [0.349, 0.686, 0.168],  # 1
        [0.272, 0.534, 0.131],  # 2
    ]  # 0    # 1    # 2

    for i in range(height):
        for j in range(width):
            red = image[i, j, 0]
            green = image[i, j, 1]
            blue = image[i, j, 2]

            for k in range(depth):
                pixel = (red * sepia_matrix[k][0]) + \
                        (green * sepia_matrix[k][1]) + \
                        (blue * sepia_matrix[k][2])

                sepia_image[i, j, k] = min(pixel, 255)

    return sepia_image.astype("uint8")
