"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io
from . import timing


def run_filter(
        file: str,
        out_file: str = None,
        implementation: str = "python",
        filter: str = "color2gray",
        scale: int = 1,
        runtime: int = 3,
        tuning: float = 1,
) -> None:
    """Run the selected filter"""
    # loads the image from given file
    image = io.read_image(file)

    # Resizes image, if specified
    if scale != 1:
        im = Image.fromarray(image)
        resize = im.resize((im.width // scale, im.height // scale))
        image = np.asarray(resize)

    # Applies the filter to image
    filter_used = instapy.get_filter(filter, implementation)

    # applies tuning if (only) numpy and sepia
    if "color2sepia" in str(filter_used) and "numpy" in str(filter_used):
        filtered = filter_used(image, tuning)
    else:
        filtered = filter_used(image)

    # optional: shows average runtime after 3 runs
    if runtime:
        average = timing.time_one(filter_used, image)
        print("------------------------------------------------------------------------------------\n")
        print(f'{filter}-filter used with {implementation}:')
        print(f"Average time over 3 runs: {average:.3f}s")
        print("\n------------------------------------------------------------------------------------")
    if out_file:
        # saves the file to the folder 'saved-files'
        io.write_image(filtered, "saved-files/" + out_file)
    else:
        # not asked to save, displays it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    # defines the parser
    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file",
                        help="The filename to apply filter to")

    # Additional, not required arguments
    parser.add_argument("-o", "--out",
                        help="The output filename")

    parser.add_argument("-g", "--gray", action="store_true",
                        help="Select gray filter")

    parser.add_argument("-se", "--sepia", action="store_true",
                        help="Select sepia filter")

    parser.add_argument("-sc", "--scale", type=int, default=1,
                        help="Scale factor to resize image")

    parser.add_argument("-i", "--implementation", type=str.lower, default="python", choices=["python", "numba", "numpy", "cython"],
                        help="The implementation to use {python, numba, numpy, cython}")

    parser.add_argument("-r", "--runtime", action="store_true",
                        help="Shows average runtime of 3 calls in the terminal")

    parser.add_argument("-t", "--tuning", type=float, default=1,
                        help="Tuning percentage for sepia filter. Only for numpy sepia {0 - 1}")

    # parse arguments and call run_filter
    args = parser.parse_args()

    # runs filter specified
    # 2 cases: Sepia, or default (gray python)
    if args.sepia:
        run_filter(file=args.file,
                   scale=args.scale,
                   out_file=args.out,
                   tuning=args.tuning,
                   filter="color2sepia",
                   runtime=args.runtime,
                   implementation=args.implementation)
    else:
        run_filter(file=args.file,
                   scale=args.scale,
                   out_file=args.out,
                   runtime=args.runtime,
                   implementation=args.implementation)
