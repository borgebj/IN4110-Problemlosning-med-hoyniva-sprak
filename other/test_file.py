# Begynnelse av n-dimensional array

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
    shape = (2, 2, 2)
    values = (1, 2, 3, 4)

    arr1 = n_array_one(list(shape), list(values))
    print(arr1)

    arr2 = n_array_two(list(shape), list(values))
    print(arr2)


main()
