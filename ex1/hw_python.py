#!/usr/bin/python
"""
   Pure Python Scientific Hello World module.
   (c) Mehdi Rezaie
"""
import math, sys

def hw1(r1, r2):
    s = math.sin(r1 + r2)
    return s

def hw2(r1, r2):
    s = math.sin(r1 + r2)
    print 'Hello, World! sin(%g+%g)=%g' % (r1,r2,s)
