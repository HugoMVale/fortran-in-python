module fmodule_bindings
   use fmodule
   use iso_c_binding, only: c_float, c_double, c_int
   implicit none

   abstract interface 
      function fx_c(x) bind(c)
         import c_double
         real(c_double), intent(in) :: x
         real(c_double) :: fx_c
      end function
   end interface

contains

   integer(c_int) function intsum_c(a, b) result(res) bind(c, name='intsum')
      integer(c_int), value, intent(in) :: a, b
      call intsum(a, b, res)
   end function

   integer(c_int) function intsum_byref_c(a, b) result(res) bind(c, name='intsum_byref')
      integer(c_int), intent(in) :: a, b
      call intsum(a, b, res)
   end function

   real(c_float) function real4sum_c(a, b) result(res) bind(c, name='real4sum')
      real(c_float), value, intent(in) :: a, b
      call real4sum(a, b, res)
   end function

   real(c_double) function real8sum_c(a, b) result(res) bind(c, name='real8sum')
      real(c_double), value, intent(in) :: a, b
      call real8sum(a, b, res)
   end function

   integer(c_int) function vector4sum_c(n, a, b, c) result(res) bind(c, name='vector4sum')
      integer(c_int), value, intent(in) :: n
      real(c_float), intent(in) :: a(n), b(n)
      real(c_float), intent(out) :: c(n)
      call vector4sum(n, a, b, c)
      res = 0
   end function

   subroutine matrix8sum_c(n, m, a, b, res) bind(c, name='matrix8sum')
      integer(c_int), value, intent(in) :: n, m
      real(c_double), intent(in) :: a(n,m), b(n,m)
      real(c_double), intent(out) :: res(n,m)
      call matrix8sum(n, m, a, b, res)
   end subroutine

   subroutine matrixtimesvector_c(n, m, a, b, res) bind(c, name='matrixtimesvector')
      integer(c_int), value, intent(in) :: n, m
      real(c_double), intent(in) :: a(n,m), b(m)
      real(c_double), intent(out) :: res(n)
      call matrixtimesvector(n, m, a, b, res)
   end subroutine

   subroutine saxpy_c(n, a, x, y) bind(c, name='saxpy')
      integer(c_int), value, intent(in) :: n
      real(c_double), value, intent(in) :: a
      real(c_double), intent(in) :: x(n)
      real(c_double), intent(inout) :: y(n)
      call saxpy(n, a, x, y)
   end subroutine

   real(c_double) function averagefnc_abstract_c(fnc, a, b) result(res) bind(c, name='averagefnc_abstract')
      procedure(fx_c) :: fnc
      real(c_double), intent(in) :: a, b
      res = averagefnc(fnc, a, b)
   end function

   real(c_double) function averagefnc_explicit_c(fnc, a, b) result(res) bind(c, name='averagefnc_explicit')
      interface 
         function fnc(x) bind(c)
            import c_double
            real(c_double), intent(in) :: x
            real(c_double) :: fnc
         end function
      end interface
      real(c_double), intent(in) :: a, b
      res = averagefnc(fnc, a, b)
   end function

end module fmodule_bindings
