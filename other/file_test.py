import numpy as np

#Begynnelse av n-dimensional array

# one way of creating nd-array
def n_array_one(shape, values):
    data = 0
    while len(shape) > 0:
        data = [data for x in range(shape[-1])]
        shape.pop()
    return data


# another way
def n_array_two(shape, values):
    empty_list = 1
    for n in shape:
        empty_list = [empty_list] * n
    return empty_list


def main():

    sepia_matrix = [
        [0.393, 0.769, 0.189],  # 0
        [0.349, 0.686, 0.168],  # 1
        [0.272, 0.534, 0.131],  # 2
    ]    # 0    # 1    # 2

    for k in range(3):
        print(sepia_matrix[0][k], end=", ")

main()

import sys
print()
print(sys.path)
print()