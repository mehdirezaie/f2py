#!/usr/bin/python
"""
   a driver script that imports Fortran/Pythob modules to 
   do Multiplication of two matrices
   (c) Mehdi Rezaie
"""
import sys,time
import numpy as np

try:
    r1 = int(sys.argv[1])
except IndexError:
    print 'Usage:', sys.argv[0], 'r1'; sys.exit(1)



#
#   Assigning values to two matrices X and Y
#
np.random.seed(seed=10)
x = np.random.random((r1,r1))
y = np.random.random((r1,r1))

#
#   Fortran pythonic module mul calculates the multiplications
#   does not work at the moment
#from hw_python import mul
#start_py = time.time()
#z0 = mul(x,y)
#end_py = time.time()
#elapsed_time_python = end_py - start_py




#
#   Fortran module test
#
from hw_fortran import matrix
start_f = time.time()
z1 = matrix(x,y)
end_f = time.time()
elapsed_time_fortran = end_f-start_f


#
#   Python numpy.dot routine calcualtes the result
#
start_py_dot = time.time()
z2 = np.dot(x,y)
end_py_dot = time.time()
elapsed_time_python_dot = end_py_dot-start_py_dot



#
#   Printing results
#
print 'Dimension of the matrices are: ',r1,'*',r1
#print 'First matrix x: \n',x
#print 'Second matrix y: \n',y
#print 'Result, matrix z0 :\n',z0
#print 'Result matrix z1 (Fortran) :\n',z1
#print 'Result, matrix z2 :\n',z2
#print 'Py is as same as Py-Fort :',np.array_equal(z0,z1)
#print 'Py is as same as Py-numpy.dot', np.array_equal(z1,z2)

#print 'Time elapsed for this calculations (Py):',elapsed_time_python
print 'Time elapsed for this calculations (Py-dot):',elapsed_time_python_dot
print 'Time elapsed for this calculations (F):',elapsed_time_fortran
