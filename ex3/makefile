FFOPTS = -c -O 
#FFOPTS = -c -g -C -f77=%all,logical  -onetrip -Bstatic 

.SUFFIXES: .o .f .f90

OBJS   = p2.o dsyev.o 
LIBDIR = /usr/local/lib

#----------------------------------------------------


p2 : $(OBJS)
	gfortran -o p2 $(OBJS) -L$(LIBDIR)  -llapack -lblas

p2.o : p2.f90
	gfortran $(FFOPTS) p2.f90

dsyev.o : dsyev.f
	gfortran $(FFOPTS) dsyev.f
clean:
	rm -rf *~ *o
