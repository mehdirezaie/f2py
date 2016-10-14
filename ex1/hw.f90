    real*8 function hw1(r1, r2)
    real*8 r1, r2
    hw1 = sin(r1 + r2)
    return
    end

    subroutine hw2(r1, r2)
    real*8 r1, r2, s
    s = sin(r1 + r2)
    write(*,100) 'Hello, World! sin(',r1+r2,')=',s
100 format(A,F6.3,A,F8.6)
    return
    end