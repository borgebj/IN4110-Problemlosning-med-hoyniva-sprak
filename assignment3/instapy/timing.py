"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from instapy import io
from typing import Callable


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeats the filter-call `calls` times,
    and returns the overall average time from all.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """

    # runs once
    filter_function(*arguments)

    # list to hold the time of calls
    times = []

    # runs the filter function `calls` times
    for i in range(calls):
        t0 = time.perf_counter()
        filter_function(*arguments)
        t1 = time.perf_counter()
        times.append(t1 - t0)

    # returns the _average_ time of one call
    return sum(times) / len(times)


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Makes timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
        calls: integer for how many times to test each filter
    """

    # writes to file, if exist: reset
    out_file = open("timing-report.txt", "w")
    out_file.truncate()

    print("------------------------------------------------------------------------------------")

    # load the image
    pixels = io.read_image(filename)

    # print the image name, width, height
    txt = f'Time performed using {filename}: {pixels.shape[1]}x{pixels.shape[0]}'
    out_file.write("\n" + txt + "\n")
    print(txt, "\n")

    # filters to test
    filter_names = ["color2gray", "color2sepia"]

    # iterates through the filters
    for filter_name in filter_names:

        # get the reference filter function
        reference_filter = instapy.get_filter()

        # time the reference implementation
        reference_time = time_one(reference_filter, pixels)

        txt = f'Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})'
        out_file.write(txt + "\n")
        print(txt)

        # iterate through the implementations
        implementations = ["cython", "numpy", "numba"]

        for implementation in implementations:
            filter = instapy.get_filter(filter_name, implementation)

            # times the filter via function that measures time
            filter_time = time_one(filter, pixels)

            # Comparing the reference time to the optimized time
            speedup = (reference_time / filter_time)
            txt = f'Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)'
            out_file.write(txt + "\n")
            print(txt)
        print("\n------------------------------------------------------------------------------------")
    out_file.close()


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
