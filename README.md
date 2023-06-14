# Description

A few examples to illustrate the main steps required to build and call Fortran code from Python with the following tools:

| Tool | Pros | Cons |
| ---  |:---: |:---: |
| [ctypes](https://docs.python.org/3/library/ctypes.html) | <li>Allows for tailor-made wrappers.</li> <li>C-API as byproduct.</li> | <li>C-bindings and Python-bindings must be written for all data types and procedures (besides the manual effort, some aspects are not intuitive at all).</li> |
| [f2py](https://numpy.org/doc/stable/f2py/index.html) | <li>Little/no manual work.</li> <li>Fortran procedures are automatically given a Pythonic signature.</li> <li>Array dimensions become optional arguments.</li> | <li>No support for derived data types, abstract interfaces, etc.</li> <li>No possibility for wrapper customization.</li> |
| [f90wrap](https://github.com/jameskermode/f90wrap) | <li>Support for derived data types, abstract interfaces, etc.</li> <li>Can parse Doxygen (but not FORD) docstrings.</li> | <li>Procedure signatures remain unchanged (Fortranic, not Pythonic).</li> <li>Procedures with callbacks are excluded (bug?).</li> <li>Support seems limited (just an impression).</li> |
| [gfort2py](https://github.com/rjfarmer/gfort2py)| <li>to do!</li> | <li>to do!</li>|

A rather comprehensive list of tools to invoke Fortran code from Python can be found [here](https://github.com/Beliavsky/Fortran-Tools#interoperability).