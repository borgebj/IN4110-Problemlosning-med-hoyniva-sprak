# Profiling report

## Questions

A few questions below to help understand the kind of information we can get from profiling outputs.
 We are not asking for lots of detail, just 1-2 sentences each.

### Question 1

> Which profiler produced the most useful output, and why?

I myself think the line profiler produced the most useful output.
I believe so because the line profiler shows exactly which lines are using most time. 
This way we can compare various lines we know are usually fast or slow, and find irregularities and places of improvement.
Also because i find line profiler to be easier to understand by looking at.

### Question 2

> Pick one profiler output (e.g. `cprofile numpy_color2sepia`).
  Based on this profile, where should we focus effort on improving performance?

> **Hint:** two things to consider when picking an optimization:

> - how much time is spent in the step? (reducing a step that takes 1% of the time all the way to 0 can only improve performance by 1%)
> - are there other ways to do it? (simple steps may already be optimal. Complex steps often have many implementations with different performance)

selected profile: **numpy color2sepia with cprofile**

From the output we get an overview of various actions and their time usage. A potential area of improvement could be where the built-in neumpy method **_einsum_** is used, as it raises the cumulative time from 0.013 to 0.138, a big time spike compared to the rest.
This implementation could for example be switched out for another method or way of doing this, like an implementation using numpys matrix multiplication.
- NOTE: written before implementation changes to using multiplication array (@). Einsum still commented out in same file.


## Profile output

Paste the outputs of `python3 -m instapy.profiling` below:

<details>
<summary>cProfile output</summary>

```
Profiling python color2gray with cprofile:
         16 function calls in 11.913 seconds

   Ordered by: cumulative time                                                                                                                                                              
                                                                                                                                                                                            
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                                                                                                     
        3   11.911    3.970   11.913    3.971 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\python_filters.py:6(python_color2gray)
        3    0.001    0.000    0.001    0.000 {method 'astype' of 'numpy.ndarray' objects}                                                                                                  
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)                                                                                                
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}                                                                       
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\multiarray.py:80(empty_like)                   
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}                                                                                              
                                                                                                                                                                                            
                                                                                                                                                                                            
Profiling cython color2gray with cprofile:                                                                                                                                                  
         16 function calls (13 primitive calls) in 0.161 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.160    0.027    0.161    0.054 instapy\cython_filters.pyx:7(cython_color2gray)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numpy color2gray with cprofile:
         16 function calls in 0.046 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.045    0.015    0.046    0.015 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numpy_filters.py:7(numpy_color2gray)
        3    0.001    0.000    0.001    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numba color2gray with cprofile:
         7 function calls in 0.010 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.010    0.003    0.010    0.003 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numba_filters.py:6(numba_color2gray)
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numba\core\serialize.py:29(_numba_unpickle)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling python color2sepia with cprofile:
         16 function calls in 12.876 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3   12.874    4.291   12.876    4.292 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\python_filters.py:36(python_color2sepia)
        3    0.002    0.001    0.002    0.001 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2sepia with cprofile:
         16 function calls (13 primitive calls) in 0.164 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.164    0.027    0.164    0.055 instapy\cython_filters.pyx:37(cython_color2sepia)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numpy color2sepia with cprofile:
         94 function calls in 0.154 seconds

   Ordered by: cumulative time
   List reduced from 19 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.002    0.001    0.154    0.051 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numpy_filters.py:37(numpy_color2sepia)
        9    0.000    0.000    0.136    0.015 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.136    0.045 <__array_function__ internals>:177(einsum)
        3    0.000    0.000    0.136    0.045 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\einsumfunc.py:1009(einsum)
        3    0.136    0.045    0.136    0.045 {built-in method numpy.core._multiarray_umath.c_einsum}
        3    0.000    0.000    0.013    0.004 {method 'clip' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.013    0.004 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\_methods.py:126(_clip)
        3    0.013    0.004    0.013    0.004 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\_methods.py:107(_clip_dep_invoke_with_casting)
        3    0.003    0.001    0.003    0.001 {method 'astype' of 'numpy.ndarray' objects}
        6    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numpy\core\_methods.py:92(_clip_dep_is_scalar_nan)


Profiling numba color2sepia with cprofile:
         7 function calls in 0.014 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.014    0.005    0.014    0.005 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numba_filters.py:34(numba_color2sepia)
        3    0.000    0.000    0.000    0.000 D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\venv\lib\site-packages\numba\core\serialize.py:29(_numba_unpickle)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```

</details>

<details>
<summary>line_profiler output</summary>

```
Profiling python color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 22.9986 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\python_filters.py
Function: python_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           def python_color2gray(image: np.array) -> np.array:
     7                                               """Convert rgb pixel array to grayscale
     8                                               Uses pure python with to grayscale image and numpy to store the image in an array
     9                                               Includes the use of double for loops to access the "height" and "width" of the image via indexing,
    10                                               then choosing manually the "depth" of the image, aka the color channels.
    11
    12                                               Args:
    13                                                   image (np.array)
    14                                               Returns:
    15                                                   np.array: gray_image
    16                                               """
    17         3        568.0    189.3      0.0      gray_image = np.empty_like(image)
    18         3         79.0     26.3      0.0      height = image.shape[0]
    19         3         19.0      6.3      0.0      width = image.shape[1]
    20         3         16.0      5.3      0.0      depth = image.shape[2]
    21
    22                                               # iterates through the pixels, and apply the grayscale transform
    23                                               # since we know c=3 in (w, h, c), we can specify each channel with 0, 1 and 2
    24      1443       8330.0      5.8      0.0      for i in range(height):
    25    923040    4651593.0      5.0      2.0          for j in range(width):
    26   3686400   21959932.0      6.0      9.5              for k in range(depth):
    27   2764800   58434793.0     21.1     25.4                  red = image[i, j, 0] * 0.21
    28   2764800   57876261.0     20.9     25.2                  green = image[i, j, 1] * 0.72
    29   2764800   57152648.0     20.7     24.9                  blue = image[i, j, 2] * 0.07
    30   2764800   29887409.0     10.8     13.0                  gray_image[i, j, k] = (red + green + blue)
    31
    32                                               # returns and ensures correct datatype
    33         3      14478.0   4826.0      0.0      return gray_image.astype("uint8")

Profiling cython color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 2.45309 s
File: instapy\cython_filters.pyx
Function: cython_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           cpdef np.ndarray[np.uint8_t, ndim=3] cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image):

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 0.0483443 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numpy_filters.py
Function: numpy_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Uses numpy slicing together with numpy vectorization
    11                                               to grayscale an image given from parameters
    12
    13                                               Implementation also ensures the returning array
    14                                               keeps the same shape as input array
    15
    16                                               Args:
    17                                                   image (np.array)
    18                                               Returns:
    19                                                   np.array: gray_image
    20                                               """
    21         3        669.0    223.0      0.1      gray_image = np.empty_like(image)
    22
    23                                               # gets every pixel from each pixel-channel and applies weights
    24         3      42521.0  14173.7      8.8      red = image[..., 0] * 0.21  # new red value
    25         3      44099.0  14699.7      9.1      green = image[..., 1] * 0.72  # new green value
    26         3      52057.0  17352.3     10.8      blue = image[..., 2] * 0.07  # new blue value
    27
    28                                               # assigns the new values to each pixel with weighted sum of each color
    29         3     115398.0  38466.0     23.9      gray_image[..., 0] = red + green + blue
    30         3     103054.0  34351.3     21.3      gray_image[..., 1] = red + green + blue
    31         3     110142.0  36714.0     22.8      gray_image[..., 2] = red + green + blue
    32
    33                                               # returns and ensures correct datatype
    34         3      15503.0   5167.7      3.2      return gray_image.astype("uint8")

Profiling numba color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 0 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numba_filters.py
Function: numba_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @jit(nopython=True)
     7                                           def numba_color2gray(image: np.array) -> np.array:
     8                                               """Converts rgb pixel array to grayscale
     9
    10                                               Uses python implementation from python_filters,
    11                                               but this time using @jit -decorator.
    12
    13                                               Args:
    14                                                   image (np.array)
    15                                               Returns:
    16                                                   np.array: gray_image
    17                                               """
    18                                               gray_image = np.empty_like(image)
    19                                               height = image.shape[0]
    20                                               width = image.shape[1]
    21                                               depth = image.shape[2]
    22
    23                                               for i in range(height):
    24                                                   for j in range(width):
    25                                                       for k in range(depth):
    26                                                           red = image[i, j, 0] * 0.21
    27                                                           green = image[i, j, 1] * 0.72
    28                                                           blue = image[i, j, 2] * 0.07
    29                                                           gray_image[i, j, k] = (red + green + blue)
    30
    31                                               return gray_image.astype("uint8")

Profiling python color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 35.3808 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\python_filters.py
Function: python_color2sepia at line 36

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    36                                           def python_color2sepia(image: np.array) -> np.array:
    37                                               """Convert rgb pixel array to sepia
    38                                               Uses pure python to add a vintage sepia-filter a given image and return it.
    39                                               Implementation loops through the array,
    40                                               and multiply each color value in the corresponding channel of a pixel with the RGB ordered sepia_matrix
    41
    42                                               Args:
    43                                                   image (np.array)
    44                                               Returns:
    45                                                   np.array: sepia_image
    46                                               """
    47
    48                                               # empty copy to operate on
    49         3        477.0    159.0      0.0      sepia_image = np.empty_like(image)
    50
    51         3         77.0     25.7      0.0      height = image.shape[0]
    52         3         32.0     10.7      0.0      width = image.shape[1]
    53         3         27.0      9.0      0.0      depth = image.shape[2]
    54         3         28.0      9.3      0.0      sepia_matrix = [
    55         3         36.0     12.0      0.0          [0.393, 0.769, 0.189],  # 0
    56         3         27.0      9.0      0.0          [0.349, 0.686, 0.168],  # 1
    57         3         27.0      9.0      0.0          [0.272, 0.534, 0.131],  # 2
    58                                               ]  # 0    # 1    # 2
    59
    60                                               # Iterates through the pixels and applies the sepia matrix
    61                                               # iterates through all color channels to multiply them with their matrix-values
    62      1443      12683.0      8.8      0.0      for i in range(height):
    63    923040    8258441.0      8.9      2.3          for j in range(width):
    64   3686400   36960282.0     10.0     10.4              for k in range(depth):
    65                                                           # k = current color channel
    66                                                           # 0 = red | 1 = green | 2 = blue
    67   8294400  128919275.0     15.5     36.4                  pixel = (image[i, j, 0] * sepia_matrix[k][0]) + \
    68   2764800   71126404.0     25.7     20.1                          (image[i, j, 1] * sepia_matrix[k][1]) + \
    69   2764800   70400699.0     25.5     19.9                          (image[i, j, 2] * sepia_matrix[k][2])
    70
    71                                                           # # assigns value and maxes value at 255
    72   2764800   38115506.0     13.8     10.8                  sepia_image[i, j, k] = pixel if pixel < 255 else 255
    73
    74                                               # returns and ensures correct datatype
    75         3      14243.0   4747.7      0.0      return sepia_image.astype("uint8")

Profiling cython color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 2.95682 s
File: instapy\cython_filters.pyx
Function: cython_color2sepia at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                           cpdef np.ndarray[np.uint8_t, ndim=3]  cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image):

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 0.143125 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numpy_filters.py
Function: numpy_color2sepia at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                           def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    38                                               """Convert rgb pixel array to sepia
    39
    40                                               Args:
    41                                                   image (np.array)
    42                                                   k (float): amount of sepia filter to apply (optional)
    43
    44                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    45                                               k=1 yields full sepia.
    46
    47                                               (note: implementing 'k' is a bonus task,
    48                                               you may ignore it for Task 9)
    49
    50                                               Returns:
    51                                                   np.array: sepia_image
    52                                               """
    53
    54                                               # defines the sepia matrix with numpy
    55         6        399.0     66.5      0.0      sepia_matrix = np.array([
    56         3         43.0     14.3      0.0          [0.393, 0.769, 0.189],  # 0
    57         3         28.0      9.3      0.0          [0.349, 0.686, 0.168],  # 1
    58         3         27.0      9.0      0.0          [0.272, 0.534, 0.131],  # 2
    59                                               ])  # 0     # 1    # 2
    60
    61                                               # --for optional bonus tasks-- #
    62         3         36.0     12.0      0.0      if not 0 <= k <= 1:
    63                                                   raise ValueError(f"k must be between [0-1], got {k=}")
    64                                               else:
    65         3        418.0    139.3      0.0          sepia_matrix *= (1-k)
    66
    67                                               # Einstein summation with given numpy 3d array and the transposed 2d sepia-matrix
    68                                               # applies the sepia-matrix to
    69         3    1283633.0 427877.7     89.7      sepia_image = np.einsum("ijk,kl->ijl", image, sepia_matrix.T)
    70
    71                                               # sets a min and max value for elements in array to ensure value doesnt exceed 255 limit
    72         3     129264.0  43088.0      9.0      sepia_image = sepia_image.clip(0, 255)
    73
    74                                               # io.display(sepia_image.astype("uint8")) # TODO: Remove
    75
    76                                               # Returns image as right type
    77         3      17401.0   5800.3      1.2      return sepia_image.astype("uint8")

Profiling numba color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 0 s
File: D:\Dokumenter\GitHub\IN4110-Problemlosning-med-hoyniva-sprak\obliger\IN3110-borgebj\assignment3\instapy\numba_filters.py
Function: numba_color2sepia at line 34

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    34                                           @jit(nopython=True)
    35                                           def numba_color2sepia(image: np.array) -> np.array:
    36                                               """Convert rgb pixel array to sepia
    37
    38                                               Args:
    39                                                   image (np.array)
    40                                               Returns:
    41                                                   np.array: sepia_image
    42                                               """
    43                                               sepia_image = np.empty_like(image)
    44
    45                                               height = image.shape[0]
    46                                               width = image.shape[1]
    47                                               depth = image.shape[2]
    48                                               sepia_matrix = [
    49                                                   [0.393, 0.769, 0.189],  # 0
    50                                                   [0.349, 0.686, 0.168],  # 1
    51                                                   [0.272, 0.534, 0.131],  # 2
    52                                               ]  # 0    # 1    # 2
    53
    54                                               for i in range(height):
    55                                                   for j in range(width):
    56                                                       for k in range(depth):
    57                                                           pixel = (image[i, j, 0] * sepia_matrix[k][0]) + \
    58                                                                   (image[i, j, 1] * sepia_matrix[k][1]) + \
    59                                                                   (image[i, j, 2] * sepia_matrix[k][2])
    60
    61                                                           sepia_image[i, j, k] = pixel if pixel < 255 else 255
    62
    63                                               return sepia_image.astype("uint8")

```

</details>
