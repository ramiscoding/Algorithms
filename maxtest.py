#!/bin/python

import math

def maxim(A,l,r):
  if (r-l == 0):
    return A[r]
  lmax = maxim(A, l, (l+r)/2)
  rmax = maxim(A, ((l+r)/2)+1, r)
  print (rmax,lmax)
  if (rmax < lmax):
    return lmax
  else:
    return rmax

A=[1,2,3,4,5]
maxelem = maxim(A,0,4)
