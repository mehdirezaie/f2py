!
!	(c) Mehdi Rezaie Last revised 19-10-2015 2:42 a.m.
!
!
!     The Schroedinger equation for the one-dimensional harmonic oscillator
!	using matrix diagonalization
!	we set the units
!     	m = c = hbar = k = 1.
!
program problem2
 implicit none
 integer,parameter :: kwrite = 6
 real(8),parameter :: r_min = -10.0d0,r_max = 10.0d0
 integer :: i,k,n_steps,info,num
 real(8) :: potential,h,const1,const2,y1_es,dy1,y2_es,dy2,y3_es,dy3

 real(8),dimension(:),allocatable :: x,v,d,e,w,work,y1,y2,y3
 real(8),dimension(:,:),allocatable :: a

 n_steps = 200

 h = (r_max-r_min)/n_steps
 allocate(x(0:n_steps),v(0:n_steps))
 x = 0.0d0;v = 0.0d0


 do i=0, n_steps
     x(i) = r_min+i*h
     v(i) = potential(x(i))
 end do

 allocate(d(1:n_steps-1),e(1:n_steps-1))

 const1 = 2.0d0/(h*h)
 const2 = -1.0d0/(h*h)
 d(1:n_steps-1)=const1+v(1:n_steps-1)
 e(1:n_steps-1)=const2

 allocate(a(1:n_steps-1,1:n_steps-1))
 a = 0.0d0

!       matrix definitation

 do k=1,n_steps-1
  a(k,k)=d(k) +a(k,k)
 end do
 do k=1,n_steps-2
  a(k,k+1) = e(k) + a(k,k+1)
  a(k+1,k) = e(k) + a(k+1,k)
 enddo


 allocate(w(n_steps-1),work(5*n_steps))

!	Here my code calls subroutine dsyev.f from the LAPACK library
 call dsyev ('V', 'U', n_steps-1, a, n_steps-1, w, work, 5*n_steps, info)
 if(info .ne. 0) stop "Dsyev() returned non-zero vaue!"

 write(kwrite,'(4e26.15)')h,w(1:3)


10 format(i10,3f10.6)
end



!
!
!	Function for the potential
!
!

function potential(a)
 real(8) :: a,potential
 potential = a*a
end
