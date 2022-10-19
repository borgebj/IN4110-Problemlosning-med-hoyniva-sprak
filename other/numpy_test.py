import numpy as np


def addOddSubEven(x):
    if x % 2 == 0:
        return x - 1
    else:
        return x + 1


def addFive(x):
    return x + 5


def main():
    # regular list
    native_one = [1, 2, 3]

    # 2D - 3 rows 3 columns
    native_two = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

    # 3D - 3 rows - 3 columns - 3 depth
    native_three = [
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]],

        [[19, 20, 21],
         [22, 23, 24],
         [25, 26, 27]]]

    print("--------------------")
    """ Creating numpy array from native array """
    numpy_native_one = np.array(native_one)
    numpy_native_two = np.array(native_two)
    numpy_native_three = np.array(native_three)

    print("---1D---")
    print(numpy_native_one)
    print("\n---2D---")
    print(numpy_native_two)
    print("\n---3D---")
    print(numpy_native_three)

    print("--------------------")
    """ Creating numpy array from given size"""
    # filled with: (zeros) (ones) (empty)
    # can include tuples aka shape: (2, 2)  (3, 3, 3)
    numpy_zero = np.zeros((3, 3, 3))
    numpy_one = np.ones((2, 2))
    numpy_empty = np.empty(3)

    print("\n----zero---")
    print(numpy_zero)
    print("\n----one----")
    print(numpy_one)
    print("\n---empty---")
    print(numpy_empty)

    print("\n-------Methods-------")
    print("\n .ravel() flattens array for iteration")
    for i in numpy_one.ravel():
        print(i, end="  ")
    print()

    print("\n .reshape() changes shape of numpy array [ (2, 2) > (4,) ]")
    print("Can also access shape via .shape()")
    print("- prev shape: ", numpy_one.shape)
    numpy_one = numpy_one.reshape(4)
    print("- ", numpy_one)
    print("- aft shape: ", numpy_one.shape)

    print("\n np.vectorize(function) converts a function to a vectorized function")
    vfunc = np.vectorize(addOddSubEven)
    numpy_native_three_operation = vfunc(numpy_native_three)
    print(numpy_native_three_operation)

    print("\nUsing vectorization to add 5 to an empty np.array")
    empty_arr = np.zeros(3)
    vfunc = np.vectorize(addFive)
    print(vfunc(empty_arr))

    print("\n-------Iteration-------")
    print("[Iteration 1] - Using array")
    for row in numpy_native_three:
        for col in row:
            for element in col:
                print(element, end=" ")
            print()
        print()

    print("[Iteration 2] - Using index")
    for i in range(len(numpy_native_three)):
        for j in range(len(numpy_native_three[i])):
            for k in range(len(numpy_native_three[i][j])):
                print(numpy_native_three[i, j, k], end=" ")
            print()
        print()

    print("When nested-lists can access index with tuple: "
          "\n3rd dim(?), 2nd row, 2nd element")
    print(numpy_native_three[2, 1, 1])

    print("-------Indexing-------")
    x = np.ndarray((3, 3, 3), dtype=int).clip(10, 100)
    print(x)
    print("\nny")
    print(np.dot(x[..., :3], [0.21, 0.72, 0.007]))
    print("\nny")
    print(x.dot([0.21, 0.72, 0.007]))


main()
