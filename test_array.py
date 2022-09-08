"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)

a = Array((4,), 1, 2, 3, 4)
b = Array((2,), 5, 6)
c = Array((6,), 1, 2, 3, 4)
d = 5

def test_str_1d():
    pass


def test_add_1d():

    assert (b + d == [10, 11])
    assert (c + b == [1, 2, 3, 4, 5, 6])

    try:
        assert (a + b)
    except ValueError:
        return True

def test_radd_1d():
    assert (d + b == [10, 11])
    assert (b + c == [1, 2, 3, 4, 5, 6])



def test_sub_1d():
    assert (b - d == [1, 2])
    assert b - d == []


def test_mul_1d():
    pass


def test_eq_1d():
    pass


def test_same_1d():
    pass


def test_smallest_1d():
    pass


def test_mean_1d():
    pass


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
