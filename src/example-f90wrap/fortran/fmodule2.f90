module fmodule2
   !! A simple module to learn how to use f90wrap.
   !! This module includes a derived data type with type-bound procedures
   use, intrinsic :: iso_fortran_env, only: real64
   implicit none
   private
   public :: point, distance_to_origin, distance_to_point

   integer, parameter :: dp = real64

   type :: point
   !! Point data type
      real(dp) :: x, y
   contains
      procedure, pass(self) :: distance_to_origin
      procedure, pass(self) :: distance_to_point
   end type point
   
contains

   ! subroutine init(self, x, y)
   !    !! Initialize a point
   !    class(point), intent(inout) :: self
   !    real(dp), intent(in) :: x, y
   !    self%x = x
   !    self%y = y
   ! end subroutine

   subroutine distance_to_origin(self, res)
      !! Distance to origin
      class(point), intent(in) :: self
      real(dp), intent(out) :: res
      res = sqrt(self%x**2 + self%y**2)
   end subroutine

   subroutine distance_to_point(self, other, res)
      !! Distance to another point
      class(point), intent(in) :: self, other
      real(dp), intent(out) :: res
      res = sqrt((self%x - other%x)**2 + (self%y - other%y)**2)
   end subroutine

   ! type(point) function point_init(x,y) result(res)
   !    !! Initialize a point
   !    real(dp), intent(in) :: x, y
   !    res%x = x
   !    res%y = y
   ! end function

   ! real(dp) function point_distance_to_origin(self) result(res)
   !    class(point), intent(in) :: self
   !    res = sqrt(self%x**2 + self%y**2)
   ! end function

   ! real(dp) function point_distance_to_point(self, other) result(res)
   !    class(point), intent(in) :: self, other
   !    res = sqrt((self%x - other%x)**2 + (self%y - other%y)**2)
   ! end function

end module fmodule2
