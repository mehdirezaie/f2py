#!/usr/bin/python
"""
   Pure Python module to do matrix multiplication
   (c) Mehdi Rezaie
"""
import math, sys,numpy

def mul(x,y):
    t = numpy.shape(x)
    z = numpy.zeros((t[0],t[0]))
    for i in range(t[0]):
        for j in range(t[0]):
            for k in range(t[0]):
                z[i][j] += x[i][k]*y[k][j]
    return z
