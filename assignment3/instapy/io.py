"""input/output utilities

for reading, writing, and displaying image files
as numpy arrays

Also a function generate_random used for testing
"""

import numpy as np
from PIL import Image
import random


def read_image(filename: str) -> np.array:
    """Read an image file to an rgb array"""
    return np.asarray(Image.open(filename))


def write_image(array: np.array, filename: str) -> None:
    """Write a numpy pixel array to a file"""
    return Image.fromarray(array).save(filename)


def random_image(width: int = 320, height: int = 180) -> np.array:
    """Create a random image array of a given size"""
    return np.random.randint(0, 255, size=(height, width, 3), dtype=np.uint8)


def display(array: np.array):
    """Show an image array on the screen"""
    Image.fromarray(array).show()


def random_index(image):
    """generate indexes for a random pixel and one color channel"""
    i = random.randint(0, image.shape[0] - 1)
    j = random.randint(0, image.shape[1] - 1)
    k = random.randint(0, image.shape[2] - 1)
    return i, j, k
