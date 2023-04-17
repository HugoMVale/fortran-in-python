r"""
Example how to call Fortran code using f2py.
f2py makes it possible to call Fortran 77/90/95 external subroutines and
Fortran 90/95 module subroutines. Derived data types are not supported.

@note:
- f2py tries to be clever/pythonic and converts subroutines into functions, and
tries to find optional arguments. As a result, the signature of the function
in python is not necessarily the original one.
- abstract interfaces are not accepted (fortran 2003).

Build process:
 - See ./fortran/build.bat

Sources:
- https://numpy.org/doc/stable/f2py/index.html

"""

from fortranmodule import mathtools
import numpy as np

# %% intsum

print('\n'*3, mathtools.intsum.__doc__)
a = 2
b = 3
result = mathtools.intsum(a, b)
print('result type: ', type(result))
print('result: ', result)

# %% real4sum

print('\n'*3, mathtools.real4sum.__doc__)

result = mathtools.real4sum(a, b)
print('result type: ', type(result))
print('result: ', result)

# %% real8sum

print('\n'*3, mathtools.real8sum.__doc__)

result = mathtools.real8sum(a, b)
print('result type: ', type(result))
print('result: ', result)


# %% vectorsum

print('\n'*3, mathtools.vectorsum.__doc__)

a = np.arange(1, 6, dtype=np.float32)
b = a + 1

result = mathtools.vectorsum(a, b)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrixsum

print('\n'*3, mathtools.matrixsum.__doc__)

a = np.ones((2, 3), dtype=np.float64)
b = 1/2*np.ones_like(a)

result = mathtools.matrixsum(a, b)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrixtimesvector

print('\n'*3, mathtools.matrixtimesvector.__doc__)

a = np.ones((2, 3), dtype=np.float64)
b = 1/2*np.ones(3, dtype=np.float64)

result = mathtools.matrixtimesvector(a, b)

print('result: \n', result)

# %% saxpy
# result returned via argument update

print('\n'*3, mathtools.saxpy.__doc__)

a = 40
x = np.ones(5, dtype=np.float64)
y = 2*np.ones(5, dtype=np.float64)

_ = mathtools.saxpy(a, x, y)
print('result (y): ', y)

# %% averagefnc
# example with callback function

print('\n'*3, mathtools.averagefnc.__doc__)


def fx(x: float): return x**2


a = 1
b = 2
result = mathtools.averagefnc(fx, a, b)
print('result: ', result)
