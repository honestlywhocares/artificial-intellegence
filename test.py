import m
import matplotlib.pyplot as mp
import matplotlib.pyplot as plt
from mpl_toolkits.mp
lot3d import Axes3D
import math
from scipy.integrate import solve_ivp
def l(x):
 l = []
 k = 0
 for i in range(x):
  for t in range(x):
   if (t**2+i**2)<=x:
    l.append([i,t])
    l.append([-i,t])
    l.append([i,-t])
    l.append([-i,-t])
   else:
    break
 return(len(kill_repeat(l)))

def kill_repeat(li):
 k = []
 for i in li:
  if i in k:
   continue
  else:
   k.append(i)
 return(k)

def p_err(x):
 pi = 3.14159
 change = abs(l(x)-(pi*x))
 print(change)
 print(l(x))
 print(pi*x)
 p = (change/l(x))*100
 return(p)

def graph_l(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(l(i+1))
 m.graph2(x_vals,y_vals)


#f(x) = sin^2(sqrt(x))
#g(x) = integral from (0,x) of f(t)dt is like factor function l(x)

def graph_p(k):
 pi = 3.14159
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(pi*(i+1))
 m.graph2(x_vals,y_vals)


def graph_err(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(p_err(i+1))
 m.graph2(x_vals,y_vals)

def prime(x):
 p = True	
 for i in range(x-1):
  if i == 0:
   continue
  else:
   if x % (i+1) == 0:
   	p = False
   else:
    continue
 return(p)

def prime_count(x):
 count = 0
 for i in range(x):
  if prime(i) == True:
   count = count + 1
  else:
   continue
 return(count-2)

def graph_pi(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(prime_count(i))
 m.graph2(x_vals,y_vals)

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
def graph_fib(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(Fibonacci(i+2))
 m.graph2(x_vals,y_vals)

def graph_phi(k):
 phi = (m.sqrt(5)+1)/2
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(phi**(i))
 m.graph2(x_vals,y_vals)

def rat(n):
 r = Fibonacci(n)/Fibonacci(n-1)

def graph_ratio(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(rat(i+3))
 m.graph2(x_vals,y_vals)

def graph_integral(f,k,d):
 def inte(n):
  return(m.integral(f,0,n,100000))
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(inte(i*d))
 m.graph2(x_vals,y_vals)	

def totient_function(x):
 count = 0
 for i in range(1,x):
  if x%i == 0:
   count = count + 1
  else:
   continue
 return(count+1)

def graph_zeta(k,d):
 mp.subplots_adjust(wspace = 0.0001,hspace = 0.0001)
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(m.zeta_r(i*d,100000))
 m.graph2(x_vals,y_vals)

def graph_factorial(k,d):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(m.stirlings_approx(i*d))
 m.graph2(x_vals,y_vals)

def graph_derivative(f,k,d):
 def der(n):
  return(m.derivative(f,n,0.001))
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(der(i*d))
 m.graph2(x_vals,y_vals)	

def graph_totient(k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(totient_function(i))
 m.graph2(x_vals,y_vals)

def graph_w(k,d):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(m.w(i*d))
 m.graph2(x_vals,y_vals)

def ratio(num,fb):
 k = []
 nn = num.as_integer_ratio()
 k = [nn[0],nn[1]] 
 if k[0]+k[1] >= fb:
  return('not rational')
 else:
  return('rational')

def thomaes_eq(x):
 if x == 0:
  return(1)
 elif ratio(x,10000000000) == 'not rational':
  return(0) 
 elif ratio(x,10000000000) == 'rational':
  p = x.as_integer_ratio()
  return(1/(p[1])) 

def graph_thomae_eq(k,d):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(thomaes_eq(i*d))
 m.graph2(x_vals,y_vals)

def dirichlet(x,u,j):
 p = m.pi()
 part1 = m.factorial(u) 
 part2 = math.cos(part1*p*x)
 return(part2**(2*j))

def graph_dirichlet(k,d):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i*d)
  y_vals.append(dirichlet(i*d,100,100))
 m.graph2(x_vals,y_vals)

def recursive(init,f,recurses):
 for i in range(recurses):
  init = m.evaluate(f,init)
 return(init)

def parametric(fx,fy,dt,end,si):
 t = 0
 for i in range(end):
  xval = m.evaluate(fx,t)
  yval = m.evaluate(fy,t)
  plt.scatter(xval,yval,color = 'black',s = si)
  t = t + dt 
 plt.show()

def parametric_3d(fx,fy,fz,dt,end,si):
 fig = plt.figure()
 ax = fig.add_subplot(111,projection = '3d')
 t = 0
 for i in range(end):
  xval = m.evaluate(fx,t)
  yval = m.evaluate(fy,t)
  zval = m.evaluate(fz,t)
  ax.scatter(xval,yval,zval,color = 'black',s = si)
  t = t + dt 
 plt.show()

def graph_chaos(init,f,k):
 x_vals = []
 y_vals = []
 for i in range(k):
  x_vals.append(i+1)
  y_vals.append(recursive(i+1,f,i))
 m.graph2(x_vals,y_vals)
# make a time evolving function for chaos eq and more.

def mandelbrot(c,accu):
 m = accu 
 z = 0
 n = 0
 for i in range(m):
  if abs(z) > 2:
   return(False)
  elif abs(z) <= 2:
   z = z**2+c
   n = n + 1

'a+bi'
def complex_plane(z,col):
 plt.ylabel('imaginary')
 plt.xlabel('real')
 re = int(str(z)[0])
 imag = int(str(z)[2])
 plt.scatter(re,imag, color=col)
 plt.show()

def imag(re,im):
 return(complex(re,im))

def graph_mandelbrot(acc,si):
 plt.ylabel('imaginary')
 plt.xlabel('real')
 s = -1
 n = []
 nn = []
 k = False
 while s <= 1:
  a = -2
  while a <= 1:
   if mandelbrot(imag(a,s),100) == False:
   	plt.scatter(a,s,color='red',s=si)
   else:
   	plt.scatter(a,s,color='blue',s=si)
   a = a + acc
  s = s + acc
 plt.show()
#from re;-2,1 and imag;-1,1
# recurse- zn = zn-1**2+c
def julia_set(z,c,epochs): 
 n = 0
 for i in range(epochs):
  if abs(z) > 2:
   return(False)
  elif abs(z) <= 2:
   z = z**2+c
   n = n + 1 
#-2,2 and -2,2
def graph_julia(acc,si,c):

 lt.ylabel('imaginary')
 plt.xlabel('real')
 s = -2
 n = []
 nn = []
 k = False
 while s <= 2:
  a = -2
  while a <= 2:
   if julia_set(imag(a,s),c,100) == False:
   	plt.scatter(a,s,color='red',s=si)
   else:
   	plt.scatter(a,s,color='blue',s=si)
   a = a + acc
  s = s + acc
 plt.show()

def triangle_chaos(p1,p2,p3):
 p10 = p1[0]
 p11 = p1[1]
 p20 = p2[0]
 p21 = p2[1]
 p30 = p3[0]
 p31 = p3[1]
 plt.scatter(p10,p11)
 plt.scatter(p20,p21)
 plt.scatter(p30,p31)
 

def go1(start,size):
 num = 1.73205080757
 import random
 start1 = start[0]
 start2 = start[1]
 plt.scatter(start1,start2,color='blue',s = size)
 n = random.randint(1,3)
 if n == 1:
  new1 = (1+start1)/2
  new2 = (0+start2)/2
 elif n == 2:
  new1 = (-1+start1)/2
  new2 = (0+start2)/2
 elif n == 3:
  new1 = (0+start1)/2
  new2 = (num+start2)/2
 new = [new1,new2]
 return(new)

def chaos(start,iters,size):
 num = 1.73205080757
 triangle([1,0],[-1,0],[0,num])
 s = start
 for i in range(iters):
  k = go1(s,size)
  s = k
 plt.show()

def graph3(x_vals,y_vals):
 plt.plot(x_vals, y_vals)  

def line(p1,p2):
# plt.scatter(p1[0],p1[1])
# plt.scatter(p2[0],p2[1])
 graph3([p1[0],p2[0]],[p1[1],p2[1]])

def triangle(p1,p2,p3):
 line(p1,p2)
 line(p2,p3)
 line(p1,p3)
 
def shape(points):
 for i in range(len(points)-1):
  point = points[i]
  pointp1 = points[i+1]
  line(point,pointp1)
 line(points[len(points)-1],points[0])

def length(p1,p2):
 delx = p2[0] - p1[0]
 dely = p2[1] - p1[1]
 length = m.nthroot(delx**2+dely**2,2)
 return(length)

def perimeter(points):
 p = 0
 for i in range(len(points)-1):
  p = p + length(points[i],points[i+1])
 p = p + length(points[len(points)-1],points[0])
 return(p)

def fully_connect(point,points):
 for i in points:
  if i == point:
   continue
  else:
   line(point,i)

def fully_connected(points): 
 for i in points:
  fully_connect(i,points)
 plt.show() 