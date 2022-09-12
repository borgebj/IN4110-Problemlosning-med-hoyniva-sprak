
# Begynnelse av n-dimensional array

def make_array(shape):
    data = False
    while len(shape) > 0:
        data = [data for x in range(shape[-1])]
        shape.pop()
    return data


def main():
    shape = (2, 2, 2)
    values = (1, 2, 3, 4)

    array = make_array(list(shape))
    print(array)


main()
