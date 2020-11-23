import numpy as np  # import the NumPy library

# Initializing a NumPy array
arr = np.array([-1, 2, 5], dtype=np.float32)

# Print the representation of the array
print(repr(arr))

# NumPy arrays are basically just Python lists
# with added features. In fact, you can easily
# convert a Python list to a Numpy array using the
# np.array function, which takes in a Python list as
# its required argument. The function also has quite a
# few keyword arguments, but the main one to know is dtype.
# The dtype keyword argument takes in a NumPy
# type and manually casts the array to the specified type.


# this is an example of 2d array through numpy

import numpy as np

arr = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
print(repr(arr))


# integers are cast to their floating-point equivalents.
arr = np.array([0, 0.1, 2])
print(repr(arr))

# casting in numpy
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)

# numpy np.nan defaults
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
np.array([np.nan, 1, 2], dtype=np.int32)


# representation of infinity in python
print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
np.array([np.inf, 3], dtype=np.int32)

# import datetime
# today = datetime.datetime.now()
#
# # Prints readable format for date-time object
# print( str(today))
#
# # prints the official format of date-time object
# print( repr(today))
import numpy as np
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(d)))

# will return an array with all the integers in the range [0, n)
arr = np.arange(5)
print(repr(arr))
# will return an array with all the integers in the range [m, n)
arr = np.arange(5.1,dtype = 'int32')
print(repr(arr))

arr = np.arange(-1, 4)
print(repr(arr))
# will return an array with the integers in the range [m, n) using a step size of s.
arr = np.arange(-1.5, 4, 2)
print(repr(arr))

# this is used for creating no of arrays we want
arr = np.linspace(5, 11, num=7)
print(repr(arr))
# The end of the range is inclusive for np.linspace,
# unless the keyword argument endpoint is set to False.

arr = np.linspace(5, 11, num=4, endpoint=True)
print(repr(arr))

arr = np.linspace(5, 11, num=4, dtype=np.int32)
print(repr(arr))

arr = np.arange(8)


# The code below shows example usages of np.reshape.
reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))



# The code below shows an example usage of the np.transpose function.
# The matrix rows become columns after the transpose.

arr = np.arange(8)
arr = np.reshape(arr, (4, 2))
transposed = np.transpose(arr)
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(transposed))
print('transposed shape: {}'.format(transposed.shape))


# The code below shows an example usage of the np.transpose function
# with the axes keyword argument. The shape property gives us the shape of an array.

# In this example, the old first dimension became the new third dimension,
# the old second dimension became the new first dimension, and
# the old third dimension became the new second dimension.
# The default value for axes is a dimension
# reversal (e.g. for 3-D data the default axes value is [2, 1, 0]).
arr = np.arange(24)
arr = np.reshape(arr, (3, 4, 2))
transposed = np.transpose(arr, axes=(1, 0, 2))
print('arr shape: {}'.format(arr.shape))
print('transposed shape: {}'.format(transposed.shape))





# The code below shows example usages of np.zeros and np.ones.

arr = np.zeros(4)
print(repr(arr))

arr = np.ones((2, 3))
print(repr(arr))

arr = np.ones((2, 3), dtype=np.int32)
print(repr(arr))


# The code below shows example usages of np.zeros_like and np.ones_like.
arr = np.array([[1, 2], [3, 4]])
print(repr(np.zeros_like(arr)))

arr = np.array([[0., 1.], [1.2, 4.]])
print(repr(np.ones_like(arr)))
print(repr(np.ones_like(arr, dtype=np.int32)))