import matplotlib.pyplot as plt

import numpy as np 
#f(0) is starting position
#f'(0) is the direction in which you are pointing 

func0 = 0.99 #put f(0) here
funcp0 = -1 #put f'(0) here
dx = 0.001

v = [func0,funcp0]

def fp(f0,fp0,t):
 c = (t**2*f0+t*f0**2-t)/(fp0*(1-t**2-f0**2))
 b = c*dx + fp0
 return(b)

def f(f0,fp0):
 return(dx*fp0+f0)

def val(func0,funcp0,s):
 t = 0
 f0 = func0
 fp0 = funcp0
 plt.scatter(t,f0)
 for i in range(int(s/dx)):
  nf0 = f(f0,fp0)
  nfp0 = fp(f0,fp0,t)
  t = t + dx
  plt.scatter(t,f0,s=1,c='black')
  f0 = nf0
  fp0 = nfp0
 plt.show()