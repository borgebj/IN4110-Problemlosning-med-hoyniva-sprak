"""Cython implementation of filter functions"""

import numpy as np
cimport numpy as np

# specifies ctype function, return type and arguments for Cython optimization
cpdef np.ndarray[np.uint8_t, ndim=3] cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image):
    """Convert rgb pixel array to grayscale
    Uses a combination of ctype declarations together with python code
    to access all "pixels" on each color channel (c in (w, h, c)) with nested for-loops
    then assigns each "pixel" a new modified value

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    cdef np.ndarray[np.uint8_t, ndim=3] gray_image = np.empty_like(image)
    cdef int i, j
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]
    cdef int depth = image.shape[2]

    for i in range(height):
        for j in range(width):
            for k in range(depth):
                red = image[i, j, 0] * 0.21
                green = image[i, j, 1] * 0.72
                blue = image[i, j, 2] * 0.07
                gray_image[i, j, k] = (red + green + blue)

    return gray_image.astype("uint8")


# specifies ctype function, return type and arguments for Cython optimization
cpdef np.ndarray[np.uint8_t, ndim=3]  cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef np.ndarray[np.uint8_t, ndim=3] sepia_image = np.empty_like(image)
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]
    cdef int depth = image.shape[2]
    cdef float[3][3] sepia_matrix = [
        [0.393, 0.769, 0.189],  # 0
        [0.349, 0.686, 0.168],  # 1
        [0.272, 0.534, 0.131],  # 2
    ]    # 0    # 1    # 2

    for i in range(height):
        for j in range(width):
            for k in range(depth):
                pixel = (image[i, j, 0] * sepia_matrix[k][0]) + \
                        (image[i, j, 1] * sepia_matrix[k][1]) + \
                        (image[i, j, 2] * sepia_matrix[k][2])

                sepia_image[i, j, k] = pixel if pixel < 255 else 255

    return sepia_image.astype("uint8")

