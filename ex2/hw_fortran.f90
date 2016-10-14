subroutine matrix (X,Y,n,C)
integer,intent(in) :: n
real(8),dimension(n,n),intent(in) :: X,Y
real(8),dimension(n,n),intent(out) :: C

integer :: i,j,k
! c_ij = x_ik y_kj

do i = 1,n
    do j = 1,n
        C(i,j) = 0.0d0
        do k = 1,n
            C(i,j) = C(i,j)+X(i,k)*Y(k,j)
        end do
    end do
end do
return
end subroutine matrix