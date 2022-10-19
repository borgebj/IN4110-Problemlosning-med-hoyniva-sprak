import numpy as np


def main():
    """2D-array"""
    # height 3 width 3
    arr_two = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

    print("--------------------")
    # [Iteration 1] - using array
    for i in arr_two:
        for j in i:
            print(j, end=" ")
        print()
    print()

    print("--------------------")
    # [Iteration 2] - Using index
    for i in range(len(arr_two)):
        for j in range(len(arr_two[i])):
            print(arr_two[i][j], end=" ")
        print()
    print()

    print("---------2D---------")
    """3D-array"""
    # heigh 3 width 3 depth 2
    arr_three = [[[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]],

                 [[19, 20, 21],
                  [22, 23, 24],
                  [25, 26, 27]]]

    print("---------3D---------")
    # [Iteration 1] - using arrays
    for i in arr_three:
        for j in i:
            for k in j:
                print(k, end=" ")
            print()
        print()

    print("--------------------")
    # [Iteration 2] - using index
    for i in range(len(arr_three)):
        for j in range(len(arr_three[i])):
            for k in range(len(arr_three[i][j])):
                print(arr_three[i][j][k], end=" ")
            print()
        print()
    print()

    print("--------------------")
    # heigh 3 width 3 depth 3
    arr_four = [[[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]],

                [[19, 20, 21],
                 [22, 23, 24],
                 [25, 26, 27]],

                [[28, 29, 30],
                 [31, 32, 33],
                 [34, 35, 36]]]

    print("--------------------")
    a = arr_four[:][:][0]
    b = arr_four[:][:][1]
    c = arr_four[:][:][2]
    print(a)
    print(b)
    print(c)


main()
