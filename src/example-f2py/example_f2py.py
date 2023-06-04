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

from fortranmodule import fmodule
import numpy as np

# %% intsum

print('\n'*3, fmodule.intsum.__doc__)
a = 2
b = 3
result = fmodule.intsum(a, b)
print('result type: ', type(result))
print('result: ', result)

# %% real4sum

print('\n'*3, fmodule.real4sum.__doc__)

result = fmodule.real4sum(a, b)
print('result type: ', type(result))
print('result: ', result)

# %% real8sum

print('\n'*3, fmodule.real8sum.__doc__)

result = fmodule.real8sum(a, b)
print('result type: ', type(result))
print('result: ', result)


# %% vector4sum

print('\n'*3, fmodule.vector4sum.__doc__)

a = np.arange(1, 6, dtype=np.float32)
b = a + 1

result = fmodule.vector4sum(a, b)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrix8sum

print('\n'*3, fmodule.matrix8sum.__doc__)

a = np.ones((2, 3), dtype=np.float64)
b = 1/2*np.ones_like(a)

result = fmodule.matrix8sum(a, b)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrixtimesvector

print('\n'*3, fmodule.matrixtimesvector.__doc__)

a = np.ones((4, 42), dtype=np.float64)
b = np.ones(42, dtype=np.float64)

result = fmodule.matrixtimesvector(a, b)

print('result: \n', result)

# %% saxpy
# result returned via argument update

print('\n'*3, fmodule.saxpy.__doc__)

a = 40
x = np.ones(5, dtype=np.float64)
y = 2*np.ones(5, dtype=np.float64)

_ = fmodule.saxpy(a, x, y)
print('result (y): ', y)

# %% averagefnc
# example with callback function

print('\n'*3, fmodule.averagefnc.__doc__)


def fx(x: float): return x**2


a = 1
b = 2
result = fmodule.averagefnc(fx, a, b)
print('result: ', result)
