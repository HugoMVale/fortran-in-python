r"""
Example how to call Fortran code using f2py

@note:
f2py tries to be clever/pythonic and converts subroutines into functions, and 
tries to find optional arguments. As a result, the signature of the function
in python is not necessarily the original one.

Build process (see build.bat):

- Quick way: 1-step procedure
f2py -c filename.f90 -m modulename

- Smart way: 2-step procedure
f2py filename.f90 -m modulename -h filename.pyf  (check signature)

To keep in mind:
- The dll file MUST be placed next to the pyd file.

Sources:
- https://numpy.org/doc/stable/f2py/index.html

"""

from fortranmodule import mathtools
import numpy as np

# %% vectorsum (single precision)

# note how f2py changed the signature
print('\n', mathtools.vectorsum.__doc__)

a = np.arange(1, 6, dtype=np.float64)
b = a + 1

result = mathtools.vectorsum(a, b)

print('result type: ', result.dtype)
print('result: ', result)

# %% vectorproduct (double precision)

print('\n'*3, mathtools.vectorproduct.__doc__)

result = mathtools.vectorproduct(a, b)

print('result type: ', result.dtype)
print('result: ', result)

# %% saxpy (result returned via argument update)

print('\n'*3, mathtools.saxpy.__doc__)

a = 41
x = np.ones(5, dtype=np.float64)
y = np.ones(5, dtype=np.float64)

_ = mathtools.saxpy(a, x, y)

print('result (y): ', y)

# %% matrixpartialsum
# The input may have order='C' or order='F', but the output has order='F'.

print('\n'*3, mathtools.matrixpartialsum.__doc__)

N = 2
M = 3
a = np.ones((N, M), dtype=np.float64, order='C')

result = mathtools.matrixpartialsum(a)

print('result type: ', result.dtype)
print('result has fortran order: ', np.isfortran(result))
print('result: \n', result)
