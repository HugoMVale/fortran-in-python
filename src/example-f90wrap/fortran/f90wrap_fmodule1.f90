! Module fmodule1 defined in file fmodule1.f90

subroutine f90wrap_intsum(a, b, res)
    use fmodule1, only: intsum
    implicit none
    
    integer, intent(in) :: a
    integer, intent(in) :: b
    integer, intent(out) :: res
    call intsum(a=a, b=b, res=res)
end subroutine f90wrap_intsum

subroutine f90wrap_real4sum(a, b, res)
    use fmodule1, only: real4sum
    implicit none
    
    real(4), intent(in) :: a
    real(4), intent(in) :: b
    real(4), intent(out) :: res
    call real4sum(a=a, b=b, res=res)
end subroutine f90wrap_real4sum

subroutine f90wrap_real8sum(a, b, res)
    use fmodule1, only: real8sum
    implicit none
    
    real(8), intent(in) :: a
    real(8), intent(in) :: b
    real(8), intent(out) :: res
    call real8sum(a=a, b=b, res=res)
end subroutine f90wrap_real8sum

subroutine f90wrap_vector4sum(n, a, b, res, n0, n1, n2)
    use fmodule1, only: vector4sum
    implicit none
    
    integer, intent(in) :: n
    real(4), intent(in), dimension(n0) :: a
    real(4), intent(in), dimension(n1) :: b
    real(4), intent(inout), dimension(n2) :: res
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(b) :: n1 = shape(b,0)
    integer :: n2
    !f2py intent(hide), depend(res) :: n2 = shape(res,0)
    call vector4sum(n=n, a=a, b=b, res=res)
end subroutine f90wrap_vector4sum

subroutine f90wrap_matrix8sum(n, m, a, b, res, n0, n1, n2, n3, n4, n5)
    use fmodule1, only: matrix8sum
    implicit none
    
    integer, intent(in) :: n
    integer, intent(in) :: m
    real(8), intent(in), dimension(n0,n1) :: a
    real(8), intent(in), dimension(n2,n3) :: b
    real(8), intent(inout), dimension(n4,n5) :: res
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(b) :: n2 = shape(b,0)
    integer :: n3
    !f2py intent(hide), depend(b) :: n3 = shape(b,1)
    integer :: n4
    !f2py intent(hide), depend(res) :: n4 = shape(res,0)
    integer :: n5
    !f2py intent(hide), depend(res) :: n5 = shape(res,1)
    call matrix8sum(n=n, m=m, a=a, b=b, res=res)
end subroutine f90wrap_matrix8sum

subroutine f90wrap_matrixtimesvector(n, m, a, b, res, n0, n1, n2, n3)
    use fmodule1, only: matrixtimesvector
    implicit none
    
    integer, intent(in) :: n
    integer, intent(in) :: m
    real(8), intent(in), dimension(n0,n1) :: a
    real(8), intent(in), dimension(n2) :: b
    real(8), intent(inout), dimension(n3) :: res
    integer :: n0
    !f2py intent(hide), depend(a) :: n0 = shape(a,0)
    integer :: n1
    !f2py intent(hide), depend(a) :: n1 = shape(a,1)
    integer :: n2
    !f2py intent(hide), depend(b) :: n2 = shape(b,0)
    integer :: n3
    !f2py intent(hide), depend(res) :: n3 = shape(res,0)
    call matrixtimesvector(n=n, m=m, a=a, b=b, res=res)
end subroutine f90wrap_matrixtimesvector

subroutine f90wrap_saxpy(n, a, x, y, n0, n1)
    use fmodule1, only: saxpy
    implicit none
    
    integer, intent(in) :: n
    real(8) :: a
    real(8), intent(in), dimension(n0) :: x
    real(8), intent(inout), dimension(n1) :: y
    integer :: n0
    !f2py intent(hide), depend(x) :: n0 = shape(x,0)
    integer :: n1
    !f2py intent(hide), depend(y) :: n1 = shape(y,0)
    call saxpy(n=n, a=a, x=x, y=y)
end subroutine f90wrap_saxpy

! End of module fmodule1 defined in file fmodule1.f90

