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

from ctypes import CDLL, c_int, c_double, byref, POINTER
import numpy as np
import os


# %% Import dll
here = os.path.dirname(os.path.realpath(__file__))
mathtools = CDLL(os.path.join(here, './fortran/mathtools.dll'))

# %% intproduct

a = 3
b = 4
result = mathtools.intproduct(byref(c_int(a)), byref(c_int(b)))
print("intproduct: ", result)

# %% doubleproduct

a = 3e0
b = 4e0
mathtools.doubleproduct.restype = c_double
result = mathtools.doubleproduct(byref(c_double(a)), byref(c_double(b)))
print("doubleproduct: ", result)

# %% vectorproduct

N = 10
a = np.asarray([i for i in range(1, N+1)], dtype=c_double)
b = np.asarray([i**2 for i in range(1, N+1)], dtype=c_double)
c = np.empty_like(a)
doubleptr = POINTER(c_double)
mathtools.vectorproduct(byref(c_int(N)),
                        a.ctypes.data_as(doubleptr),
                        b.ctypes.data_as(doubleptr),
                        c.ctypes.data_as(doubleptr))
print("vectorproduct: ", c)
