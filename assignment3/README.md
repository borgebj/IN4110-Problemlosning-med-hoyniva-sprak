
# Instapy

## The instapy package
- The instapy package is a package created to apply a filter to images.
- The filters supported is grayscale and sepia filter.
- The `pillow` package allows us to turn images into arrays so we can operate on them
- The `numpy` package is used to manipulate the image together with pillow to change RGB values of the image.
- Other packages used are `Cython` and `numba`for testing faster implementation methods, and `line-profiler` for further profiling
- N.B. sometimes added images are created with 4-dimensions through Pillow. The sepia filter does not support 4D arrays.

## How to install package
- The instapy package is installed using the pip command `pip install .` in the assignment3 folder
- This will download dependencies used in the package.

### Check if package is installed
- If package is installed correctly, you can test this with the test-file test_package.py with the terminal command:
	`python -m  pytest -v test/test_package.py`
	or
	`pytest -v test/test_package.py`

## How to run package

### Profiling reports
- Can be run on terminal inside main folder 'assignment3'
- Will create a new text-file with the name '_timing-report.txt_', a written report including name, timing and comparisons.
- Will also print in terminal.
- To run the report write `python -m instapy.timing` in terminal

#### More profiling
- More profiling included in task 15 is available as well in the '_profiling.py_' file
- This report is shown in the terminal with the command `python -m instapy.profiling`

### Unit tests
- Unit tests are included in the test-folder.
- Checks every implementation type to ensure shape and type of input and output is same.
- Also checks a random pixel sample to see if RGB modifications are correct
- Unit tests can be run from the main folder with: `pytest`

### Image filtering
- The instapy package includes a command-line interface, run with `instapy`
- Has flags that can specify filter, implementation and more
- For overview of flags, use help-flag: `instapy --help` or `instapy -h`
- The only required flag is the file, or image in which to apply the filter to. This is added at the start.
- Will run Grayscale filter with python, full scale on default 
- Will display image if out is not specified
- **note**: filter using _numpy_ and _sepia_ has the option to add a tuning parameter

Flags and uses:

| Flags | Descriptions |
| ----- | ----- |
| `instapy rain.jpg` | required image-file after package name, rain.jpg in this case |
| `-se` or `--sepia` | for _Sepia_ filter |
| `-g`  or `--gray` | for _Grayscale_ filter |
| `-sc 1` or `--scale 1` | for a resized image based on scale given,| 1=100% | 2=50% | 4=25% | |
| `-i Cython` or `--implementation Cython` | for implementation using _Cython_ |
| `-o out.jpg` or `-out new.jpg` | creates an _output_ file with name sepia_rain.jpg |
| `-r` or `--runtime` | shows the average runtime for 3 calls on used filter |
| `-t` or `--tuning` | A float between 0 and 1 for how vintage an image should be displayed. (only numpy sepia) |

## Examples of filtering commands:

### Grayscale using Python
* Only includes required argument "file"
* It is not necessary to specify **-g** **-i IMPLEMENTATION** or **-sc SCALE** for grayscale python with scale 1
```
instapy test/rain.jpg
```

### Grayscale using Cython with output-file
* Out-file specified with **-o**
* Cython specified with **-i Cython**
* The new image will be saved in the "saved-files" folder with given out-name
```
instapy test/rain.jpg -i Cython -o gray_rain.jpg
```

### Sepia using Numpy rescaled to half size with runtime info
* Sepia specified with **-se**
* Numpy specified with **-i numpy**
* Scaled to half size with **-sc 2**
* Runtime info in terminal with **-r**
```
instapy test/rain.jpg -se -i numpy -sc 2 -r
```

# short summation
- The package supports turning images into a grayscale or a vintage version, or shows various reports to the user.
- A command-line interface using different flags are implemented and makes the package easy to use.
- The main commands for running this package are:
  - `python -m instapy.timing` for a time-report
  - `python -m instapy.profiling` for a more detailed time-report
  - `instapy image.jpg -se` or `instapy image.jpg -g` for a quick display of grayscale or vintage image. Additional flags can be added
