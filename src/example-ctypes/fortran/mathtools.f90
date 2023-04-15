module mathtools
   use, intrinsic :: iso_fortran_env, only: real64
   use iso_c_binding, only: c_double, c_int
   implicit none

contains

   subroutine vectorproduct(a, b, res)
      !! Element-wise product of two vectors (assumed shape)
      real(real64), intent(in) :: a(:), b(:)
      real(real64), intent(out) :: res(:)
      res = a*b
   end subroutine

   subroutine vectorproduct_c(n, a, b, res) bind(c, name='vectorproduct')
      !! C binding to internal fortran function (explicit shape required)
      integer(c_int), intent(in) :: n
      real(c_double), intent(in) :: a(n), b(n)
      real(c_double), intent(out) :: res(n)
      call vectorproduct(a, b, res)
   end subroutine

   function intproduct(a, b) bind(c, name='intproduct')
      !! Product of two integers directly in C types
      integer(c_int), intent(in) :: a, b
      integer(c_int) :: intproduct
      intproduct = a*b
   end function

   function doubleproduct(a, b) bind(c, name='doubleproduct')
      !! Product of two doubles directly in C types
      real(c_double), intent(in) :: a, b
      real(c_double) :: doubleproduct
      doubleproduct = a*b
   end function

end module mathtools
