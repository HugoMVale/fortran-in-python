:: Clean previous files
del *.mod
del *.dll
del *.o

gfortran -c -O3 fmodule.f90
gfortran -c -O3 fmodule_bindings.f90 
gfortran -shared -o fmodule.dll fmodule.o fmodule_bindings.o 

:: gcc test_bindings.c -L./ -l/fmodule