module fmodule
   !! A simple module to learn how to use f2py.
   !! f2py is restricted to fortran<=95: no derived data types, no abstract interfaces, etc.
   !! Real kind specification is intentionally mixed, to show that kind mapping works. 
   use, intrinsic :: iso_fortran_env, only: real32, real64
   implicit none
   private
   public :: intsum, real4sum, real8sum, vector4sum, matrix8sum, saxpy, matrixtimesvector
   public :: averagefnc, applyfnctomatrix

   integer, parameter :: sp = real32
   integer, parameter :: dp = real64

contains

   subroutine intsum(a, b, res)
      !! Sum of two integers
      integer, intent(in) :: a, b
      integer, intent(out) :: res
      res = a + b
   end subroutine

   ! non-real functions do not work due to f2py bug
   ! integer function intsum(a, b) result(res)
   !    !! Sum of two integers
   !    integer, intent(in) :: a, b
   !    res = a + b
   ! end function

   subroutine real4sum(a, b, res)
      !! Sum of two reals
      real(real32), intent(in) :: a, b
      real(real32), intent(out) :: res
      res = a + b
   end subroutine

   subroutine real8sum(a, b, res)
      !! Sum of two reals(8)
      real(real64), intent(in) :: a, b
      real(real64), intent(out) :: res
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
      real(real64), intent(in) :: a(n,m), b(m)
      real(real64), intent(out) :: res(n)
      res = matmul(a,b)
   end subroutine

   subroutine saxpy(n, a, x, y)
      !! Saxpy (explicit shape)
      integer, intent(in) :: n
      real(real64) :: a
      real(real64), intent(in) :: x(n)
      real(real64), intent(inout) :: y(n)
      y = a*x + y
   end subroutine

   subroutine averagefnc(fnc, a, b, res)
      !! Average of function with explicit interface
      interface 
         function fnc(x)
            import dp
            real(dp), intent(in) :: x
            real(dp) :: fnc
         end function
      end interface
      real(dp), intent(in) :: a, b
      real(dp), intent(out) :: res
      res = (fnc(a) + fnc(b))/2
   end subroutine

   subroutine applyfnctomatrix(fnc, n, m, a, res)
      !! Apply a function column-wise to a matrix
      interface
         subroutine fnc(s, x, u)
            import dp
            integer, intent(in) :: s
            real(dp), intent(in) :: x(s)
            real(dp), intent(out) :: u(s)
         end subroutine
      end interface
      integer, intent(in) :: n, m
      real(dp), intent(in) :: a (n, m)
      real(dp), intent(out) :: res(n, m)
      integer :: j
      do j=1,m
            call fnc(n, a(:,j), res(:,j))
      end do
   end subroutine

end module fmodule
