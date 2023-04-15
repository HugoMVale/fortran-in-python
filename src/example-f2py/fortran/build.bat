:: Clean previous files
del *.pyd
del *.pyf
del ..\*.pyd
del fortranmodule\.libs\*.* /f /q
del ..\*.dll

:: Create function signatures
f2py mathtools.f90 -m fortranmodule -h mathtools.pyf
:: Generate module (otherwise next step won't work) 
gfortran -c -O3 mathtools.f90
:: Build extension module 
f2py -c --opt='-O3' mathtools.pyf mathtools.f90 --fcompiler=gfortran

:: Copy extension module and dll to target folder
copy *.pyd ..
copy fortranmodule\.libs\*.dll ..