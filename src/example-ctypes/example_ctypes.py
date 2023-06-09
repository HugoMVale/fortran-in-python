r"""
Example of how to invoke Fortran code using ctypes.

Steps:
 - Write code with C bindings.
 - Compile module.
 - Create _shared_ library (dll).

To keep in mind:
 - Default return type is int. Other types need to be manually specified.
 - By default, Fortran expects arguments passed by reference.
 - Callbacks can be a bit tricky because of pointers. By comparison, this is
   where you see how convenient f2py is.

Useful info:
 - https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/ctypes.html
 - https://github.com/daniel-de-vries/fortran-ctypes-python-example
 - https://gist.github.com/Nican/5198719
 - https://numba.pydata.org/numba-doc/latest/user/cfunc.html
"""

from ctypes import CDLL, c_int, c_float, c_double, byref, POINTER, CFUNCTYPE
import numpy as np
from numba import cfunc, types
import os


# %% Load shared library with C-bindings
here = os.path.dirname(os.path.realpath(__file__))
fmodule = CDLL(os.path.join(here, './fortran/fmodule.dll'))

# %% intsum

a = 3
b = 4
result = fmodule.intsum(c_int(a), c_int(b))
print("intsum: ", result)

# %% intsum
# int args passed by reference

a = 3
b = 4
result = fmodule.intsum_byref(byref(c_int(a)), byref(c_int(b)))
print("intsum_byref: ", result)

# %% real4sum
# float return type

a = 3e0
b = 4e0
fmodule.real4sum.restype = c_float
result = fmodule.real4sum(c_float(a), c_float(b))
print("real4sum: ", result)


# %% real8sum
# double return type

a = 3e0
b = 4e0
fmodule.real8sum.restype = c_double
result = fmodule.real8sum(c_double(a), c_double(b))
print("real8sum: ", result)

# %% vector4sum
# float array args passed as pointers to np arrays

N = 10
a = np.asarray([i for i in range(1, N+1)], dtype=c_float)
b = np.asarray([i**2 for i in range(1, N+1)], dtype=c_float)
c = np.empty_like(a)
floatptr = POINTER(c_float)
fmodule.vector4sum(c_int(N),
                   a.ctypes.data_as(floatptr),
                   b.ctypes.data_as(floatptr),
                   c.ctypes.data_as(floatptr))
print("vector4sum: ", c)

# %% matrix8sum
# double array args passed as pointers to np arrays
# matrix should preferably have Fortran order

n = 2
m = 3
a = np.ones((n, m), dtype=c_double, order='F')
b = 1/2*np.ones_like(a)
c = np.empty_like(a)
doubleptr = POINTER(c_double)
fmodule.matrix8sum(c_int(n), c_int(m),
                   a.ctypes.data_as(doubleptr),
                   b.ctypes.data_as(doubleptr),
                   c.ctypes.data_as(doubleptr))
print("matrix8sum: ", c)

# %% matrixtimesvector
# double array args passed as pointers to np arrays
# matrix should preferably have Fortran order

n = 2
m = 3
a = np.ones((n, m), dtype=c_double, order='F')
b = 2*np.ones(m, dtype=c_double)
c = np.empty(n, dtype=c_double)
doubleptr = POINTER(c_double)
fmodule.matrixtimesvector(c_int(n), c_int(m),
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
fmodule.saxpy(c_int(n),
              c_double(a),
              x.ctypes.data_as(doubleptr),
              y.ctypes.data_as(doubleptr))
print("saxpy: ", y)

# %% averagefnc
# with Python callback

# Define the function return type
averagefnc = fmodule.averagefnc_explicit
averagefnc.restype = c_double

# Define the callback function, with its prototype
# Since x is passed as pointer, it must be dereferenced.

@CFUNCTYPE(c_double, POINTER(c_double))
def fnc1(x):
    return x[0]**2


a = 10.
b = 20.

result = fmodule.averagefnc_explicit(fnc1,
                                     byref(c_double(a)),
                                     byref(c_double(b)))
print("averagefnc with Python callback: ", result)


# %% averagefnc
# with Numba callback

@cfunc(types.double(types.CPointer(types.double)))
def fnc2(x):
    return x[0]**2


result = fmodule.averagefnc_explicit(fnc2.ctypes,
                                     byref(c_double(a)),
                                     byref(c_double(b)))
print("averagefnc with numba callback: ", result)
