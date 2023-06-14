! Module fmodule2 defined in file fmodule2.f90

subroutine f90wrap_point__get__x(this, f90wrap_x)
    use fmodule2, only: point
    implicit none
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    integer, intent(in)   :: this(2)
    type(point_ptr_type) :: this_ptr
    real(8), intent(out) :: f90wrap_x
    
    this_ptr = transfer(this, this_ptr)
    f90wrap_x = this_ptr%p%x
end subroutine f90wrap_point__get__x

subroutine f90wrap_point__set__x(this, f90wrap_x)
    use fmodule2, only: point
    implicit none
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    integer, intent(in)   :: this(2)
    type(point_ptr_type) :: this_ptr
    real(8), intent(in) :: f90wrap_x
    
    this_ptr = transfer(this, this_ptr)
    this_ptr%p%x = f90wrap_x
end subroutine f90wrap_point__set__x

subroutine f90wrap_point__get__y(this, f90wrap_y)
    use fmodule2, only: point
    implicit none
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    integer, intent(in)   :: this(2)
    type(point_ptr_type) :: this_ptr
    real(8), intent(out) :: f90wrap_y
    
    this_ptr = transfer(this, this_ptr)
    f90wrap_y = this_ptr%p%y
end subroutine f90wrap_point__get__y

subroutine f90wrap_point__set__y(this, f90wrap_y)
    use fmodule2, only: point
    implicit none
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    integer, intent(in)   :: this(2)
    type(point_ptr_type) :: this_ptr
    real(8), intent(in) :: f90wrap_y
    
    this_ptr = transfer(this, this_ptr)
    this_ptr%p%y = f90wrap_y
end subroutine f90wrap_point__set__y

subroutine f90wrap_point_initialise(this)
    use fmodule2, only: point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: this_ptr
    integer, intent(out), dimension(2) :: this
    allocate(this_ptr%p)
    this = transfer(this_ptr, this)
end subroutine f90wrap_point_initialise

subroutine f90wrap_point_finalise(this)
    use fmodule2, only: point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: this_ptr
    integer, intent(in), dimension(2) :: this
    this_ptr = transfer(this, this_ptr)
    deallocate(this_ptr%p)
end subroutine f90wrap_point_finalise

subroutine f90wrap_distance_to_origin__binding__point(self, res)
    use fmodule2, only: point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: self_ptr
    integer, intent(in), dimension(2) :: self
    real(8), intent(out) :: res
    self_ptr = transfer(self, self_ptr)
    call self_ptr%p%distance_to_origin(res=res)
end subroutine f90wrap_distance_to_origin__binding__point

subroutine f90wrap_distance_to_point__binding__point(self, other, res)
    use fmodule2, only: point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: self_ptr
    integer, intent(in), dimension(2) :: self
    type(point_ptr_type) :: other_ptr
    integer, intent(in), dimension(2) :: other
    real(8), intent(out) :: res
    self_ptr = transfer(self, self_ptr)
    other_ptr = transfer(other, other_ptr)
    call self_ptr%p%distance_to_point(other=other_ptr%p, res=res)
end subroutine f90wrap_distance_to_point__binding__point

subroutine f90wrap_distance_to_origin(self, res)
    use fmodule2, only: distance_to_origin, point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: self_ptr
    integer, intent(in), dimension(2) :: self
    real(8), intent(out) :: res
    self_ptr = transfer(self, self_ptr)
    call distance_to_origin(self=self_ptr%p, res=res)
end subroutine f90wrap_distance_to_origin

subroutine f90wrap_distance_to_point(self, other, res)
    use fmodule2, only: distance_to_point, point
    implicit none
    
    type point_ptr_type
        type(point), pointer :: p => NULL()
    end type point_ptr_type
    type(point_ptr_type) :: self_ptr
    integer, intent(in), dimension(2) :: self
    type(point_ptr_type) :: other_ptr
    integer, intent(in), dimension(2) :: other
    real(8), intent(out) :: res
    self_ptr = transfer(self, self_ptr)
    other_ptr = transfer(other, other_ptr)
    call distance_to_point(self=self_ptr%p, other=other_ptr%p, res=res)
end subroutine f90wrap_distance_to_point

! End of module fmodule2 defined in file fmodule2.f90

