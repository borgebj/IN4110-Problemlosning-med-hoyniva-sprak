"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Uses numpy slicing together with numpy vectorization
    to grayscale an image given from parameters

    Implementation also ensures the returning array
    keeps the same shape as input array

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)

    # gets every pixel from each pixel-channel and applies weights
    red = image[..., 0] * 0.21  # new red value
    green = image[..., 1] * 0.72  # new green value
    blue = image[..., 2] * 0.07  # new blue value

    # assigns the new values to each pixel with weighted sum of each color
    gray_image[..., 0] = red + green + blue
    gray_image[..., 1] = red + green + blue
    gray_image[..., 2] = red + green + blue

    # returns and ensures correct datatype
    return gray_image.astype("uint8")


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    Returns:
        np.array: sepia_image
    """

    # --for optional bonus tasks-- #
    if not 0 <= k <= 1:
        raise ValueError(f"k must be between [0-1], got {k=}")

    # defines the sepia matrix with numpy
    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ])

    # uses @-operand for simplified np.matmul (matrix multiplication) of image-array and transposed sepia-matrix
    sepia_image = image @ sepia_matrix.T

    # adds altered sepia and altered original with K together to create a mix
    # image only tunes when specified - 1 = default
    if 0.0 <= k < 1.0:
        sepia_image = (sepia_image * k) + image * (1 - k)

    # sets a min and max value for elements in array to ensure value doesnt exceed 255 limit
    sepia_image = sepia_image.clip(0, 255)

    # Returns image as right type
    return sepia_image.astype("uint8")

# [alternative] for sepia (slow) (previous implementation)
# Einstein summation with given numpy 3d array and the transposed 2d sepia-matrix
# sepia_image = np.einsum("ijk,kl->ijl", image, sepia_matrix.T)

# [alternative] for sepia (same as @)
# uses np.matmul (matrix multiplication) of image-array and transposed sepia-matrix
# sepia_image = np.matmul(image, sepia_matrix.T)
