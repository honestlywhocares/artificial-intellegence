import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import time
import util as u

def ball(c,r):
 plt.scatter(c[0],c[1],s = r)

def pendulum(theta0,l):
 g = 9.8
 def dU_dx(U, x):
  # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
  return [U[1],  (-g/l)*np.sin(U[0])]
 U0 = [theta0, 0]
 xs = np.linspace(0, 10, 200)
 Us = odeint(dU_dx, U0, xs)
 ys = Us[:,0]
 plt.xlabel("x")
 plt.ylabel("y")
 plt.title("pendulum")
 plt.plot(xs,ys)
 plt.show()

def projectile_motion_x(v,theta,x0):
 g = 9.8
 n = 0
 w = []
 def dU_dx(U, x):
  # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
  return [U[1],  0]
 U0 = [x0, v*np.cos(theta)]
 xs = np.linspace(0, 10, 200)
 Us = odeint(dU_dx, U0, xs)
 for i in Us:
  w.append([xs[n],i[0]])
  n = n + 1
 return(w)


def projectile_motion_y(m,v,theta,y0):
 g = 9.8
 n= 0
 w = []
 def dU_dy(U, x):
  # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
  return [U[1],  -1*m*g]
 U0 = [y0, v*np.cos(theta)]
 xs = np.linspace(0, 10, 200)
 U = odeint(dU_dy, U0, xs)
 for i in U:
  w.append([xs[n],i[0]])
  n = n + 1
 return(w)

def planet(m1,m2,xlim,ylim,x0,x1):
 dt = 0.01       
 T = 35000       
 gamma = .00002 
 x0 = np.array([0, 0, 1, 0])
 x1 = np.array([0, 0, 1, 0.005])
 xs = [x0, x1]
 def F(x):
  r1 = x[:2]  
  r2 = x[2:4]    
  posdiff_vec = r2 - r1                
  dist = np.linalg.norm(posdiff_vec)     
  F1 = gamma * m2 * posdiff_vec / (dist**2)   
  F2 = - gamma * m1 * posdiff_vec / (dist**2)      
  return np.concatenate([F1, F2], axis=0)
 for i in range(T):   
  Lx = xs[-1]
  LLx = xs[-2]
  F_prev = F(Lx)                 
  x = dt**2*F_prev + 2*Lx - LLx       
  xs.append(x)
 x, y = np.split(np.array(xs), 2, axis=1)
 u.plotAnim(xlim,ylim,x, y, T, isSaveVideo=False)

def path_under_gravity(v,h0,a,endt):
 x_vals = []
 y_vals = []
 for i in range(endt):
  x_vals.append(v*i)
  y_vals.append(h0-(1/2*a*i**2))
 m.graph2(x_vals,y_vals)

def ex_pend1(l,theta):
 plot_point([0,0],-1*theta,1)


def plot_point(point, angle, length):
 '''
  point - Tuple (x, y)
  angle - Angle you want your end point at in degrees.
  length - Length of the line you want to plot.
  Will plot the line on a 10 x 10 plot.
 '''
 # unpack the first point
 x, y = point
 # find the end point
 endy = length * math.sin(math.radians(angle))
 endx = length * math.cos(math.radians(angle))
 # plot the points
 fig = plt.figure()
 ax = plt.subplot(111)
 ax.set_ylim([-10, 10])   # set the bounds to be 10, 10
 ax.set_xlim([-10, 10])
 ax.plot([x, endx], [y, endy])
 line([x,y],[endx,endy])
 fig.show()
