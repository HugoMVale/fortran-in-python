from __future__ import print_function, absolute_import, division
import _fortranmodule
import f90wrap.runtime
import logging
import numpy

class Fmodule1(f90wrap.runtime.FortranModule):
    """
    Module fmodule1
    
    
    Defined at fmodule1.f90 lines 1-95
    
    """
    @staticmethod
    def intsum(a, b):
        """
        res = intsum(a, b)
        
        
        Defined at fmodule1.f90 lines 13-17
        
        Parameters
        ----------
        a : int
        b : int
        
        Returns
        -------
        res : int
        
        """
        res = _fortranmodule.f90wrap_intsum(a=a, b=b)
        return res
    
    @staticmethod
    def real4sum(a, b):
        """
        res = real4sum(a, b)
        
        
        Defined at fmodule1.f90 lines 25-29
        
        Parameters
        ----------
        a : float
        b : float
        
        Returns
        -------
        res : float
        
        """
        res = _fortranmodule.f90wrap_real4sum(a=a, b=b)
        return res
    
    @staticmethod
    def real8sum(a, b):
        """
        res = real8sum(a, b)
        
        
        Defined at fmodule1.f90 lines 31-35
        
        Parameters
        ----------
        a : float
        b : float
        
        Returns
        -------
        res : float
        
        """
        res = _fortranmodule.f90wrap_real8sum(a=a, b=b)
        return res
    
    @staticmethod
    def vector4sum(n, a, b, res):
        """
        vector4sum(n, a, b, res)
        
        
        Defined at fmodule1.f90 lines 37-42
        
        Parameters
        ----------
        n : int
        a : float array
        b : float array
        res : float array
        
        """
        _fortranmodule.f90wrap_vector4sum(n=n, a=a, b=b, res=res)
    
    @staticmethod
    def matrix8sum(n, m, a, b, res):
        """
        matrix8sum(n, m, a, b, res)
        
        
        Defined at fmodule1.f90 lines 44-49
        
        Parameters
        ----------
        n : int
        m : int
        a : float array
        b : float array
        res : float array
        
        """
        _fortranmodule.f90wrap_matrix8sum(n=n, m=m, a=a, b=b, res=res)
    
    @staticmethod
    def matrixtimesvector(n, m, a, b, res):
        """
        matrixtimesvector(n, m, a, b, res)
        
        
        Defined at fmodule1.f90 lines 51-56
        
        Parameters
        ----------
        n : int
        m : int
        a : float array
        b : float array
        res : float array
        
        """
        _fortranmodule.f90wrap_matrixtimesvector(n=n, m=m, a=a, b=b, res=res)
    
    @staticmethod
    def saxpy(n, a, x, y):
        """
        saxpy(n, a, x, y)
        
        
        Defined at fmodule1.f90 lines 58-64
        
        Parameters
        ----------
        n : int
        a : float
        x : float array
        y : float array
        
        """
        _fortranmodule.f90wrap_saxpy(n=n, a=a, x=x, y=y)
    
    _dt_array_initialisers = []
    

fmodule1 = Fmodule1()

class Fmodule2(f90wrap.runtime.FortranModule):
    """
    Module fmodule2
    
    
    Defined at fmodule2.f90 lines 1-48
    
    """
    @f90wrap.runtime.register_class("fortranmodule.point")
    class point(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=point)
        
        
        Defined at fmodule2.f90 lines 9-14
        
        """
        def __init__(self, handle=None):
            """
            self = Point()
            
            
            Defined at fmodule2.f90 lines 9-14
            
            
            Returns
            -------
            this : Point
            	Object to be constructed
            
            
            Automatically generated constructor for point
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _fortranmodule.f90wrap_point_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Point
            
            
            Defined at fmodule2.f90 lines 9-14
            
            Parameters
            ----------
            this : Point
            	Object to be destructed
            
            
            Automatically generated destructor for point
            """
            if self._alloc:
                _fortranmodule.f90wrap_point_finalise(this=self._handle)
        
        def distance_to_origin(self):
            """
            res = distance_to_origin__binding__point(self)
            
            
            Defined at fmodule2.f90 lines 24-28
            
            Parameters
            ----------
            self : unknown
            
            Returns
            -------
            res : float
            
            """
            res = \
                _fortranmodule.f90wrap_distance_to_origin__binding__point(self=self._handle)
            return res
        
        def distance_to_point(self, other):
            """
            res = distance_to_point__binding__point(self, other)
            
            
            Defined at fmodule2.f90 lines 30-34
            
            Parameters
            ----------
            self : unknown
            other : unknown
            
            Returns
            -------
            res : float
            
            """
            res = \
                _fortranmodule.f90wrap_distance_to_point__binding__point(self=self._handle, \
                other=other._handle)
            return res
        
        @property
        def x(self):
            """
            Element x ftype=real(dp) pytype=float
            
            
            Defined at fmodule2.f90 line 11
            
            """
            return _fortranmodule.f90wrap_point__get__x(self._handle)
        
        @x.setter
        def x(self, x):
            _fortranmodule.f90wrap_point__set__x(self._handle, x)
        
        @property
        def y(self):
            """
            Element y ftype=real(dp) pytype=float
            
            
            Defined at fmodule2.f90 line 11
            
            """
            return _fortranmodule.f90wrap_point__get__y(self._handle)
        
        @y.setter
        def y(self, y):
            _fortranmodule.f90wrap_point__set__y(self._handle, y)
        
        def __str__(self):
            ret = ['<point>{\n']
            ret.append('    x : ')
            ret.append(repr(self.x))
            ret.append(',\n    y : ')
            ret.append(repr(self.y))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @staticmethod
    def distance_to_origin(self):
        """
        res = distance_to_origin(self)
        
        
        Defined at fmodule2.f90 lines 24-28
        
        Parameters
        ----------
        self : unknown
        
        Returns
        -------
        res : float
        
        """
        res = _fortranmodule.f90wrap_distance_to_origin(self=self._handle)
        return res
    
    @staticmethod
    def distance_to_point(self, other):
        """
        res = distance_to_point(self, other)
        
        
        Defined at fmodule2.f90 lines 30-34
        
        Parameters
        ----------
        self : unknown
        other : unknown
        
        Returns
        -------
        res : float
        
        """
        res = _fortranmodule.f90wrap_distance_to_point(self=self._handle, \
            other=other._handle)
        return res
    
    _dt_array_initialisers = []
    

fmodule2 = Fmodule2()

