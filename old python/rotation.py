import numpy as np
import matplotlib.pyplot as plt
import test as t
def point_rotation(point,angle,p_r):
 x = point[0]
 y = point[1]
 xn = (x-p_r[0])*np.cos(np.radians(angle)) - (y-p_r[1])*np.sin(np.radians(angle))+p_r[0]
 yn = (x-p_r[0])*np.sin(np.radians(angle)) + (y-p_r[1])*np.cos(np.radians(angle))+p_r[1]
 return([xn,yn])

def rotate(angle,points,p_r):
 l = []
 for i in points:
  l.append(point_rotation(i,angle,p_r))
 return(l)