:: Clean previous files
del *.mod
del *.dll
del *.o

gfortran -c -O3 mathtools.f90
gfortran -c -O3 mathtools_bindings.f90 
gfortran -shared -o mathtools.dll mathtools.o mathtools_bindings.o 