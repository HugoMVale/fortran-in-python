module mathtools
   !! A simple module to learn how to use f2py.
   use, intrinsic :: iso_fortran_env, only: real32, real64
   implicit none
   private
   public :: vectorproduct, vectorsum, saxpy, matrixpartialsum

   integer, parameter :: dp = real64

contains

   subroutine vectorproduct(n, a, b, res)
      !! Element-wise product of two vectors (explicit shape)
      integer, intent(in) :: n
      real(dp), intent(in) :: a(n), b(n)
      real(dp), intent(out) :: res(n)
      res = a*b
   end subroutine

   subroutine vectorsum(n, a, b, res)
      !! Element-wise sum of two vectors (explicit shape)
      integer, intent(in) :: n
      real(real32), intent(in) :: a(n), b(n)
      real(real32), intent(out) :: res(n)
         res = a + b
   end subroutine

   subroutine saxpy(n, a, x, y)
      !! Saxpy (explicit shape)
      integer, intent(in) :: n
      real(real64) :: a
      real(real64), intent(in) :: x(n)
      real(real64), intent(inout) :: y(n)
         y = a*x + y
   end subroutine

   subroutine matrixpartialsum(n, m, a, res)
      !! Partial sum of matrix elements (explicit shape)
      integer, intent(in) :: n, m
      real(real64), intent(in) :: a(n, m)
      real(real64), intent(out) :: res(n, m)
      integer :: i, j
      ! Dumb algorithm
      do j=1,m
         do i=1,n
            res(i,j) = sum(a(1:i,1:j))
         end do
      end do
   end subroutine

end module mathtools
