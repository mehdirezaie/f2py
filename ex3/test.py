#!/usr/bin/python
import numpy as np

import scipy.cluster
import scipy


import time

def potential(x):
    return x*x


r_min,r_max,n_steps = -10.0,10.0,500
h = (r_max-r_min)/float(n_steps)
const1 = 2.0/(h*h)
const2 = -1.0/(h*h)

x = [r_min+i*h for i in range(n_steps+1)]
v = [potential(x[i]) for i in range(n_steps+1)]
d = [const1+v[i+1] for i in range(n_steps-1)]
e = [const2 for i in range(n_steps-1)]

a = np.zeros((n_steps-1,n_steps-1))


for i in range(n_steps-1):
    a[i][i] += d[i]

for i in range(n_steps-2):
    a[i][i+1] += e[i]
    a[i+1][i] += e[i]

#
#   routine python
#
t1_py_linalg = time.time()
eigenvalues = scipy.linalg.eig(a)
t2_py_linalg = time.time()

print np.sort(eigenvalues[0])[0:3],'\n elapsed time (sp.linalg.eig)',t2_py_linalg-t1_py_linalg


t1_py_linalg = time.time()
eigenvalues = np.linalg.eig(a)
t2_py_linalg = time.time()

print np.sort(eigenvalues[0])[0:3],'\n elapsed time (np.linalg.eig)',t2_py_linalg-t1_py_linalg




#
#   Routine Fortran dsyev is called
#
import dsyev
t1_py_dsyev = time.time()
w,work,info = dsyev.dsyev('V','U',n_steps-1,a,n_steps-1,3*n_steps-1)
t2_py_dsyev = time.time()
print w[0:3],'\n elapsed time (dsyev)',t2_py_dsyev-t1_py_dsyev


print "dsyev is called correctly, INFO is :",info
