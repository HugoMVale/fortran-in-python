r"""
Example how to call Fortran code using f2py.
f2py makes it possible to call Fortran 77/90/95 external subroutines and
Fortran 90/95 module subroutines. Derived data types are not supported.

@note:
f2py tries to be clever/pythonic and converts subroutines into functions, and
tries to find optional arguments. As a result, the signature of the function
in python is not necessarily the original one.

Build process (see ./fortran/build.bat):

- Quick way: 1-step procedure
f2py -c filename.f90 -m modulename

- Smart way: 2-step procedure
f2py filename.f90 -m modulename -h filename.pyf  (check signature)
f2py -c filename.pyf filename.f

To keep in mind:
- The dll file MUST be placed next to the pyd file.

Sources:
- https://numpy.org/doc/stable/f2py/index.html

"""

from fortranmodule import mathtools
import numpy as np

# %% vectorsum (single precision)
# Note how f2py changed the signature of the original subroutine

print('\n'*3, mathtools.vectorsum.__doc__)

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

a = 40
x = np.ones(5, dtype=np.float64)
y = 2*np.ones(5, dtype=np.float64)

_ = mathtools.saxpy(a, x, y)

print('result (y): ', y)

# %% matrixpartialsum
# The input may have order='C' or order='F', but the output has order='F'.

print('\n'*3, mathtools.matrixpartialsum.__doc__)

a = np.ones((2, 3), dtype=np.float64, order='C')

result = mathtools.matrixpartialsum(a)

print('result type: ', result.dtype)
print('result has fortran order: ', np.isfortran(result))
print('result: \n', result)

# %% intproduct
# The result is recast to float!!!

print('\n', mathtools.intproduct.__doc__)

a = 2
b = 3

result = mathtools.intproduct(a, b)
print('result type: ', type(result))
print('result: ', result)


# %% intproduct2
# This works well, despite the warning by f2py

result = mathtools.intproduct2(a, b)
print('result type: ', type(result))
print('result: ', result)
