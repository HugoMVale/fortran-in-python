module fmodule
   !! A module with various toy functions and subroutines to learn how to invoke fortran code
   !! from python.
   use, intrinsic :: iso_fortran_env, only: real32, real64
   implicit none
   private
   public :: intsum, real4sum, real8sum, vector4sum, matrix8sum, saxpy, matrixtimesvector
   public :: averagefnc

   integer, parameter :: sp = real32
   integer, parameter :: dp = real64

contains

   subroutine intsum(a, b, res)
      !! Sum of two integers
      integer, intent(in) :: a, b
      integer, intent(out) :: res
      res = a + b
   end subroutine

   subroutine real4sum(a, b, res)
      !! Sum of two reals
      real(sp), intent(in) :: a, b
      real(sp), intent(out) :: res
      res = a + b
   end subroutine

   subroutine real8sum(a, b, res)
      !! Sum of two reals(8)
      real(dp), intent(in) :: a, b
      real(dp), intent(out) :: res
      res = a + b
   end subroutine

   subroutine vector4sum(n, a, b, res)
      !! Element-wise sum of two vectors (explicit shape)
      integer, intent(in) :: n
      real(sp), intent(in) :: a(n), b(n)
      real(sp), intent(out) :: res(n)
      res = a + b
   end subroutine

   subroutine matrix8sum(n, m, a, b, res)
      !! Element-wise sum of two matrices (explicit shape)
      integer, intent(in) :: n, m
      real(dp), intent(in) :: a(n,m), b(n,m)
      real(dp), intent(out) :: res(n,m)
      res = a + b
   end subroutine

   subroutine matrixtimesvector(n, m, a, b, res)
      !! Product of matrix*vector (explicit shape)
      integer, intent(in) :: n, m
      real(dp), intent(in) :: a(n,m), b(m)
      real(dp), intent(out) :: res(n)
      res = matmul(a,b)
   end subroutine

   subroutine saxpy(n, a, x, y)
      !! Saxpy (explicit shape)
      integer, intent(in) :: n
      real(dp), intent(in) :: a
      real(dp), intent(in) :: x(n)
      real(dp), intent(inout) :: y(n)
      y = a*x + y
   end subroutine

   real(dp) function averagefnc(fnc, a, b) result(res)
      !! Average of function with explicit interface
      interface
         function fnc(x)
            import dp
            real(dp), intent(in) :: x
            real(dp) :: fnc
         end function
      end interface
      real(dp), intent(in) :: a, b
      res = (fnc(a) + fnc(b))/2
   end function

end module fmodule
