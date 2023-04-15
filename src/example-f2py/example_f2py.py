r"""
Example how to call Fortran code using f2py

Note that f2py tries to be clever and converts subroutines into functions,
and tries to find optional arguments. As a result, the signature of the
function in python is not necessarily the original one.

Steps:

- Quick way: 1-step procedure
f2py -c filename.f90 -m modulename --fcompiler=gfortran

- Smart way: 2-step procedure
f2py filename.f90 -m modulename -h filename.pyf  (check signature)
f2py -c filename.pyc filename.f --fcompiler=gfortran

To keep in mind:
- The dll file MUST be placed next to the pyd file.

Sources:
- https://numpy.org/doc/stable/f2py/index.html

"""

from fortranmodule import mathtools
import numpy as np

# %% vectorsum (single precision)

# note how f2py changed the signature
print(mathtools.vectorsum.__doc__)

a = np.arange(1, 6, dtype=np.float64)
b = a + 1

r1 = mathtools.vectorsum(a, b)
print('result type: ', r1.dtype)
print('vectorsum: ', r1)

# %% vectorproduct (double precision)

print(mathtools.vectorproduct.__doc__)

r2 = mathtools.vectorproduct(a, b)
print('result type: ', r2.dtype)
print('vectorproduct: ', r2)

# %% saxpy (result returned via argument update)

print(mathtools.saxpy.__doc__)

a = 41
x = np.ones(5, dtype=np.float64)
y = np.ones(5, dtype=np.float64)

_ = mathtools.saxpy(a, x, y)
print('saxpy: ', y)
