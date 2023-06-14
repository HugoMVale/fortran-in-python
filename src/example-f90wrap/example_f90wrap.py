r"""
Example how to call Fortran code using f90wrap.
f90wrap builds on the capabilities of f2py but adds support for derived data
types and type-bound procedures.

@note:
- Unlike f2py, f90wrap respects the original signature of the fortran
procedures.
- Output arrays must be initiliazed before calling the function.

Build process:
- See ./fortran/build.bat.

Sources:
- https://iopscience.iop.org/article/10.1088/1361-648X/ab82d2
- https://github.com/jameskermode/f90wrap

"""

from fortranmodule import fmodule1
import numpy as np

# %% intsum

print('\n'*3, fmodule1.intsum.__doc__)
a = 2
b = 3
result = fmodule1.intsum(a, b)
print('result type: ', type(result))
print('result: ', result)

# %% real4sum

print('\n'*3, fmodule1.real4sum.__doc__)

result = fmodule1.real4sum(a, b)
print('result type: ', type(result))
print('result: ', result)


# %% real8sum

print('\n'*3, fmodule1.real8sum.__doc__)

result = fmodule1.real8sum(a, b)
print('result type: ', type(result))
print('result: ', result)


# %% vector4sum

print('\n'*3, fmodule1.vector4sum.__doc__)

a = np.arange(1, 6, dtype=np.float32)
b = a + 1
result = np.empty_like(a)

fmodule1.vector4sum(len(a), a, b, result)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrix8sum

print('\n'*3, fmodule1.matrix8sum.__doc__)

a = np.ones((2, 3), dtype=np.float64, order='F')
b = 1/2*np.ones_like(a)
result = np.empty_like(a)

fmodule1.matrix8sum(a.shape[0], a.shape[1], a, b, result)
print('result type: ', result.dtype)
print('result: \n', result)

# %% matrixtimesvector

print('\n'*3, fmodule1.matrixtimesvector.__doc__)

a = np.ones((4, 42), dtype=np.float64, order='F')
b = np.ones(42, dtype=np.float64)
result = np.empty(a.shape[0], dtype=np.float64)

fmodule1.matrixtimesvector(a.shape[0], a.shape[1], a, b, result)

print('result: \n', result)