"""
Profiling (IN4110 only)
"""

import pstats
import cProfile
import line_profiler

import numpy

import instapy
from . import io


def profile_with_cprofile(filter, image, ncalls=3):
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:
        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    profiler = cProfile.Profile()

    # - runs `filter(image)` in the profiler -
    # gathers info after enable, before disable
    profiler.enable()
    for i in range(ncalls):
        filter(image)
    profiler.disable()

    stats = pstats.Stats(profiler)

    # prints the top 10 results, sorted by cumulative time
    stats.sort_stats(pstats.SortKey.CUMULATIVE).print_stats(10)


def profile_with_line_profiler(filter, image, ncalls=3):
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:

        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    # creates the LineProfiler
    profiler = line_profiler.LineProfiler()

    # adds filter as a function to the profiler
    profiler.add_function(filter)

    # Measures filter by running it with the argument image
    for i in range(ncalls):
        profiler.runcall(filter, image)

    # prints statistics
    profiler.print_stats()


def run_profiles(profiler: str = "cprofile"):
    """Run profiles of every implementation

    Args:

        profiler (str): either 'line_profiler' or 'cprofile'
    """
    # Select which profile function to use
    if profiler == "line_profiler":
        profile_func = profile_with_line_profiler
    elif profiler.lower() == "cprofile":
        pass
        profile_func = profile_with_cprofile
    else:
        raise ValueError(f"{profiler=} must be 'line_profiler' or 'cprofile'")

    # construct a random 640x480 image
    image = io.random_image(640, 480)

    filter_names = ["color2gray", "color2sepia"]
    implementations = ["python", "cython", "numpy", "numba"]
    for filter_name in filter_names:
        for implementation in implementations:
            print(f"Profiling {implementation} {filter_name} with {profiler}:")
            filter = instapy.get_filter(filter_name, implementation)

            # call it once
            filter(image)
            profile_func(filter, image)


if __name__ == "__main__":
    print("Begin cProfile")
    run_profiles("cprofile")
    print("End cProfile")
    print("Begin line_profiler")
    run_profiles("line_profiler")
    print("End line_profiler")
