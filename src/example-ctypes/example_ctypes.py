"""
Example of how to call Fortran code using ctypes

Steps:
 - Write code with C bindings.
 - Compile module.
 - Create _shared_ library (dll).

To keep in mind:
 - Default return type is int. Other types need to be manually specified.
 - By default, fortran expects arguments passed by reference.

Useful info:
 - https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/ctypes.html
 - https://github.com/daniel-de-vries/fortran-ctypes-python-example
"""

from ctypes import CDLL, c_int, c_float, c_double, byref, POINTER, CFUNCTYPE
import numpy as np
import os


# %% Import dll
here = os.path.dirname(os.path.realpath(__file__))
mathtools = CDLL(os.path.join(here, './fortran/mathtools.dll'))

# %% intsum
# int args passed by reference

a = 3
b = 4
result = mathtools.intsum_c(byref(c_int(a)), byref(c_int(b)))
print("intsum: ", result)

# %% intsum
# int args passed by value

a = 3
b = 4
result = mathtools.intsum_byvalue_c(c_int(a), c_int(b))
print("intsum_byvalue: ", result)

# %% real4sum
# float args passed by reference
# float return type

a = 3e0
b = 4e0
mathtools.real4sum_c.restype = c_float
result = mathtools.real4sum_c(byref(c_float(a)), byref(c_float(b)))
print("real4sum: ", result)


# %% real8sum
# double args passed by reference
# double return type

a = 3e0
b = 4e0
mathtools.real8sum_c.restype = c_double
result = mathtools.real8sum_c(byref(c_double(a)), byref(c_double(b)))
print("real8sum: ", result)

# %% vector4sum
# float array args passed as pointers to np arrays

N = 10
a = np.asarray([i for i in range(1, N+1)], dtype=c_float)
b = np.asarray([i**2 for i in range(1, N+1)], dtype=c_float)
c = np.empty_like(a)
floatptr = POINTER(c_float)
mathtools.vector4sum_c(byref(c_int(N)),
                       a.ctypes.data_as(floatptr),
                       b.ctypes.data_as(floatptr),
                       c.ctypes.data_as(floatptr))
print("vector4sum: ", c)

# %% matrix8sum 
# double array args passed as pointers to np arrays

n = 2
m = 3
a = np.ones((n, m), dtype=c_double)
b = 1/2*np.ones_like(a)
c = np.empty_like(a)
doubleptr = POINTER(c_double)
mathtools.matrix8sum_c(byref(c_int(n)), byref(c_int(m)),
                       a.ctypes.data_as(doubleptr),
                       b.ctypes.data_as(doubleptr),
                       c.ctypes.data_as(doubleptr))
print("matrix8sum: ", c)

# %% matrixtimesvector
# double array args passed as pointers to np arrays

n = 2
m = 3
a = np.ones((n, m), dtype=c_double)
b = 2*np.ones(m, dtype=c_double)
c = np.empty(n, dtype=c_double)
doubleptr = POINTER(c_double)
mathtools.matrixtimesvector_c(byref(c_int(n)), byref(c_int(m)),
                              a.ctypes.data_as(doubleptr),
                              b.ctypes.data_as(doubleptr),
                              c.ctypes.data_as(doubleptr))
print("matrixtimesvector: ", c)

# %% saxpy
# double array args passed as pointers to np arrays
# arg y is updated in place, i.e. intent(inout)

n = 5
a = 40.
x = np.ones(n, dtype=c_double)
y = 2*np.ones(n, dtype=c_double)
doubleptr = POINTER(c_double)
mathtools.saxpy_c(byref(c_int(n)),
                  byref(c_double(a)),
                  x.ctypes.data_as(doubleptr),
                  y.ctypes.data_as(doubleptr))
print("saxpy: ", y)

# %% averagefnc
# Does not work yet! :)


@CFUNCTYPE(c_double, c_double)
def fnc(x):
    return x**2


a = 1.
b = 2.
averagefnc = mathtools.averagefnc_c
averagefnc.restype = c_double
result = averagefnc(fnc, byref(c_double(a)), byref(c_double(b)))
print("averagefnc: ", result)