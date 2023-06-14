:: Clean previous files
del *.pyd
del *.o
del *.mod
del f90wrap*.f90
del ..\*.pyd
del ..\fortranmodule.py
del ..\*.dll
del _fortranmodule\.libs\*.* /f /q

pause

:: Create wrappers suitable for input to f2py
f90wrap -v -k kind_map.json -m fortranmodule fmodule1.f90 fmodule2.f90

pause
:: Generate modules (otherwise next step won't work) 
gfortran -c -O3 fmodule1.f90 fmodule2.f90 
:: Build extension module 
f2py-f90wrap -c -m _fortranmodule f90wrap_fmodule1.f90 f90wrap_fmodule2.f90 fmodule1.f90 fmodule2.f90 --fcompiler=gnu95

:: Move extension module and dll to target folder
move *.pyd ..
move fortranmodule.py ..
move _fortranmodule\.libs\*.dll ..
