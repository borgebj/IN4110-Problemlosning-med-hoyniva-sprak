"""
Tests for the array class

note: i have not tested on float since the result was pretty inconsistent and unstable.
      would sometimes result in small decimal differences.

      test_index, test_str and test_reuse are own-made testing methods.
      * index checks if indexing is correct
      * str checks if str prints out an okay string
      * reuse checks if possible to reuse array for further operations
"""

from array_class import Array


# 1D tests (Task 4)

def test_index_1d():
    my_array = Array((3,), 1, 2, 3)
    assert my_array[1] == 2
    assert my_array[-1] == 3


def test_str_1d():
    assert Array((3,), 1, 2, 3).__str__() == "[1, 2, 3]"
    assert Array((3,), 1, 2, 3).__str__() != "[1, 2, 3, 4, 5]"
    assert Array((2,), True, False).__str__() == "[True, False]"


def test_reuse_1d():
    a = Array((2,), 5, 8)
    b = Array((2,), 4, 1)
    a = a + 5
    b = b - 5
    assert a == Array((2,), 10, 13)
    assert b == Array((2,), -1, -4)
    a = a + b
    b = b * a
    assert a == Array((2,), 9, 9)
    assert b == Array((2,), -9, -36)


def test_add_1d():
    assert Array((4,), 1, 2, 3, 4) + 5 == Array((4,), 6, 7, 8, 9)
    assert 5 + Array((4,), 1, 2, 3, 4) == Array((4,), 6, 7, 8, 9)
    assert Array((3,), 5, 6, 1) + Array((3,), 1, 5, 1) == Array((3,), 6, 11, 2)


def test_sub_1d():
    assert Array((2,), 1, 5) - 5 == Array((2,), -4, 0)
    assert 6 - Array((2,), 3, 7) == Array((2,), -3, 1)
    assert Array((3,), 5, 6, 3) - Array((3,), 1, 5, 5) == Array((3,), 4, 1, -2)


def test_mul_1d():
    assert Array((2,), 1, 5) * 5 == Array((2,), 5, 25)
    assert 5 * Array((2,), 1, 5) == Array((2,), 5, 25)
    assert Array((2,), 5, 6) * Array((2,), 1, 5) == Array((2,), 5, 30)


def test_eq_1d():
    assert Array((1,), 5) == Array((1,), 5)
    assert Array((1,), 5) != Array((2,), 2, 1)
    assert Array((5,), 5, 3, 2, 1, 6) != Array((3,), 5, 3, 2)


def test_same_1d():
    assert Array((3,), 5, 6, 3).is_equal(Array((3,), 5, 6, 3)) == Array((3,), True, True, True)
    assert Array((3,), 5, 6, 3).is_equal(Array((3,), 1, 6, 2)) == Array((3,), False, True, False)
    assert Array((3,), 5, 6, 3).is_equal(Array((3,), 6, 3, 5)) == Array((3,), False, False, False)


def test_smallest_1d():
    assert Array((4,), 1, 2, 3, 4).min_element() == 1.0
    assert Array((4,), 6, 69, 7, 89).min_element() == 6.0
    assert Array((1,), 5).min_element() != 6.0


def test_mean_1d():
    assert Array((3,), 5, 6, 7).mean_element() == 6.0
    assert Array((3,), 5, 6, 7).mean_element() != 5.0
    assert Array((1,), 5).mean_element() == 5.0


# 2D tests (Task 6)

def test_index_2d():
    my_array = Array((3, 2), 8, 3, 4, 1, 6, 1)
    assert my_array[1][0] == 1
    assert my_array[-1][-1] == 1
    assert my_array[1][1] == 6


def test_str_2d():
    assert Array((2, 2), 1, 2, 3, 4).__str__() == "[[1, 2], [3, 4]]"
    assert Array((2, 2), 1, 2, 3, 4).__str__() != "[[1, 2], [3, 4], [5, 6]]"


def test_reuse_2d():
    aa = Array((2, 2), 5, 8, 2, 2)
    bb = Array((2, 2), 4, 1, 5, 5)
    aa = aa + 5
    bb = bb - 5
    assert aa == Array((2, 2), 10, 13, 7, 7)
    assert bb == Array((2, 2), -1, -4, 0, 0)
    aa = aa + bb
    bb = bb * aa
    assert aa == Array((2, 2), 9, 9, 7, 7)
    assert bb == Array((2, 2), -9, -36, 0, 0)


def test_add_2d():
    assert Array((2, 2), 1, 2, 3, 4) + 6 == Array((2, 2), 7, 8, 9, 10)
    assert Array((3, 3), 1, 2, 3, 4, 5, 6, 7, 8, 3) + 2 == Array((3, 3), 3, 4, 5, 6, 7, 8, 9, 10, 5)
    assert Array((2, 2), 3, 3, 4, 4) + Array((2, 2), 2, 4, 5, 6) == Array((2, 2), 5, 7, 9, 10)


def test_sub_2d():
    assert Array((2, 2), 1, 2, 3, 4) - 6 == Array((2, 2), -5, -4, -3, -2)
    assert Array((3, 3), 1, 2, 3, 4, 5, 6, 7, 8, 3) - 1 == Array((3, 3), 0, 1, 2, 3, 4, 5, 6, 7, 2)
    assert Array((2, 2), 3, 3, 4, 4) - Array((2, 2), 2, 4, 5, 6) == Array((2, 2), 1, -1, -1, -2)


def test_mult_2d():
    assert Array((2, 2), 4, 6, 9, 3) * 3 == Array((2, 2), 12, 18, 27, 9)
    assert Array((3, 3), 1, 2, 3, 4, 5, 6, 7, 8, 9) * 2 == Array((3, 3), 2, 4, 6, 8, 10, 12, 14, 16, 18)
    assert Array((2, 2), 3, 3, 4, 4) * Array((2, 2), 2, 4, 5, 6) == Array((2, 2), 6, 12, 20, 24)


def test_eq_2d():
    assert Array((1, 1), 5) == Array((1, 1), 5)
    assert Array((2, 2), 2, 2, 4, 4) != Array((2, 2), 4, 4, 2, 2)
    assert Array((1, 3), True, True, False) == Array((1, 3), True, True, False)


def test_same_2d():
    assert Array((2, 1), 5, 1).is_equal(Array((2, 1), 5, 1)) == Array((2, 1), True, True)
    assert Array((2, 2), 1, 2, 4, 4).is_equal(Array((2, 2), 1, 2, 3, 4)) == Array((2, 2), True, True, False, True)
    assert Array((2, 2), 5, 6, 3, 1).is_equal(Array((2, 2), 6, 3, 5, 1)) == Array((2, 2), False, False, False, True)


def test_smallest_2d():
    assert Array((2, 2), 11, 42, 56, 12).min_element() == 11.0
    assert Array((2, 2), 3, 6, 2, 7).min_element() == 2.0
    assert Array((1, 3), 5, 6, 1).min_element() != 5.0


def test_mean_2d():
    assert Array((3, 3), 1, 2, 3, 4, 5, 6, 7, 8, 9).mean_element() == 5.0
    assert Array((1, 5), 5, 6, 7, 4, 9).mean_element() != 3.0
    assert Array((2, 2), 5.2, 5.6, 2.3, 9.9).mean_element() == 5.75


if __name__ == "__main__":
    # Task 4: 1d tests
    test_index_1d()
    test_reuse_1d()
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_index_2d()
    test_str_2d()
    test_reuse_2d()
    test_add_2d()
    test_sub_2d()
    test_mult_2d()
    test_eq_2d()
    test_same_2d()
    test_smallest_2d()
    test_mean_2d()

    print("All tests passed")
