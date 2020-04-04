import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
from numpy import median

def help():
 print('''nthroot(x,n) --> gives the nth root of x''')
 print('''graph(formula,x_range) --> graphes the formula over the x_range written like graph('x**2',range(-10,10))''')
 print('''graph2(x_vals,y_vals) --> graphs points given in the two lists''')
 print('''derivative(f,x,h) --> gives the derivative of f at x. decreasing h increases accuracy''')
 print('''integral(f,startx,endx,no) --> gives the integral from startx till endx of f. increasing no increases accuracy''')
 print('''zero(f,start,iters) --> gives where the function f equals zero,start can be any number and iters increases accuracy''')
 print('''solve_2d(1st x coefficient,2nd x coefficient,1st y coefficient, 2nd y coefficient, power of x in both equations,power of y in both equations.) --> solves 2d equations smae structre for 3d and 4d solvers as well''')
 print('''solve_zeros_lin(c1,b) --> gives zero of bx+c1''')
 print('''sqrt(x) --> gives square root of x''')
 print('''solve_zeros_quad(c1,c2,b) --> solves c1x**2+c2*x+b=0''')
 print('''sum_product(a,b,c) --> finds (if it exists) rational numbers k1,k2 such that k1+k2 = b and k1*k2 = ac used in factoring''')
 print('''evaluate(function,i) --> evaluates the function at point i''')
 print('''fixed_point(function) --> evaluates what any number would collapse to if f was applied to itself infinitly many times (if such a value exists)''')
 print('''sum(f,start,end) --> evaluates sigma from start till end''')
 print('''zeta(x,k) --> evaluates riemman zeta function at x k increases accuracy''')
 print('''prob(favorable outcomes, total outcomes) --> gives probability (in %) of a favourable outcome''')
 print('''e() --> gives a approximation of the number e''')
 print('''pi() --> gives a approximation of the number pi''')
 print('''w(x) --> gives the lambert w function at x''')
 print('''prod(function,start,end) --> applies pi (multiplier) on function from start till end''')
 print('''arcsin(x) --> gives the approximate value of arcsin(x)''')
 print('''sin(x) --> gives the value of sin(x)''')
 print('''factorial(x) --> gives the value of factorial x''')
 print('''special_factorial(x) --> gives less accurate value however works at non integer values as well''')
 print('''vertex(a,b,c) --> finds vertex of parabola with coefficiants a,b,c''')
 print('''equal(f1,f2,start,acc) --> finds solution to f1 = f2 start,acc are for increasing accuracy''')
 print('''spindle(d) --> gives area of spindle with diameter d''')
 print('''ellipse(a,b,c) --> gives area of ellipse with equation ax^2+by^2 = c''')
 print('''euler_machroini_constant() --> gives value of E.M constant up to 50 places''')
 print('''iter_f(f,start,iters) --> preforms an iteration on f starting at start for iters iterations''')
 print('''total_things(k_list) --> if k_list is a list of no.'s it returns sum of all no.'s''')
 print('''chance(times,thing,k_list) --> gives the chance that something from thing is selected times successive times from k_list''')
 print('''chance(times_not,thing,k_list) --> gives the chance that something from thing is not selected times_not successive times from k_list''')

def nthroot (x, n):
 r = 1
 for i in range(16):
  r = (((n - 1) * r) + x / (r ** (n - 1))) / n
 return r

def graph(formula, x_range):  
 x = np.array(x_range)  
 y = eval(formula)
 plt.plot(x, y)  
 plt.show()

def graph2(x_vals,y_vals):
 plt.plot(x_vals, y_vals)  
 plt.show()


def derivative(f,x,h):
 rise = evaluate(f,x+h)-evaluate(f,x)
 slope = rise/h
 return(slope)

def integral(f,startx,endx,no):
 area = 0
 width = (endx-startx)/no
 for i in range(no):
  height = evaluate(f,startx + i*width)
  area = area + (width*height)
 return(area)

def cont_average(start,end,func):
 a = integral(func,start,end,10000000)
 b = end-start
 return(a/b)

def zero(f,start,iters):
 ha = False
 for i in range(iters):
  try:
   start = start - (evaluate(f,start)/derivative(f,start,0.00001))
  except:
   continue
 if evaluate(f,start) > 0.5:
  print('no zeros')
  return 
 else:
  return(start)

def solve_2d(xc1,xc2,yc1,yc2,n1,n2,xp,yp):
 cof1_x = xc1
 cof2_x = xc2
 p_x = xp
 p_y = yp
 cof1_y = yc1
 cof2_y = yc2
 a = [[cof1_x,cof1_y],
      [cof2_x,cof2_y]]
 z = [int(n1),
      int(n2)]

 inv_a = npl.inv(a)
 
 asol = np.matmul(inv_a,z)

# [a,b] = [x^k,y^p] , x^k = a , y^k = b : x = a**(1/k) , y = b**(1/p)  

 x_p = asol[0]

 y_p = asol[1]

 x = nthroot(x_p,int(p_x))
 y = nthroot(y_p,int(p_y))

 print(x)
 print(y)

 return([x,y])

def solve_3d(xc1,xc2,xc3,yc1,yc2,yc3,zc1,zc2,zc3,n1,n2,n3,xp,yp,zp):
 cof1_x = xc1
 cof2_x = xc2
 cof3_x = xc3
 p_x = xp
 p_y = yp
 p_z = zp
 cof1_y = yc1
 cof2_y = yc2
 cof3_y = yc3
 
 cof1_z = zc1
 cof2_z = zc2
 cof3_z = zc3

 a = [[cof1_x,cof1_y,cof3_x],
      [cof2_x,cof2_y,cof3_y],
      [cof1_z,cof2_z,cof3_z]]
 z = [n1,
      n2,
      n3]

 inv_a = npl.inv(a)
 
 asol = np.matmul(inv_a,z)

# [a,b] = [x^k,y^p] , x^k = a , y^k = b : x = a**(1/k) , y = b**(1/p)  

 x_p = asol[0]

 y_p = asol[1]

 z_p = asol[2]

 x = nthroot(x_p,int(p_x))
 y = nthroot(y_p,int(p_y))
 z = nthroot(z_p,int(p_z))

 print(x)
 print(y)
 print(z)
 return([x,y,z])

 cof1_x = xc1
 cof2_x = xc2
 p_x = xp
 p_y = yp
 cof1_y = yc1
 cof2_y = yc2
 a = [[cof1_x,cof1_y],
      [cof2_x,cof2_y]]
 z = [int(n1),
      int(n2)]

 inv_a = npl.inv(a)
 
 asol = np.matmul(inv_a,z)

# [a,b] = [x^k,y^p] , x^k = a , y^k = b : x = a**(1/k) , y = b**(1/p)  

 x_p = asol[0]

 y_p = asol[1]

 x = nthroot(x_p,int(p_x))
 y = nthroot(y_p,int(p_y))

 print(x)
 print(y)

 return([x,y])

def solve_4d(xc1,xc2,xc3,xc4,yc1,yc2,yc3,yc4,zc1,zc2,zc3,zc4,dc1,dc2,dc3,dc4,n1,n2,n3,n4,xp,yp,zp,dp):
 cof1_x = xc1
 cof2_x = xc2
 cof3_x = xc3
 cof4_x = xc4
 p_x = xp
 p_y = yp
 p_z = zp
 p_d = dp
 cof1_y = yc1
 cof2_y = yc2
 cof3_y = yc3
 cof4_y = yc4

 cof1_z = zc1
 cof2_z = zc2
 cof3_z = zc3
 cof4_z = zc4

 cof1_d = dc1
 cof2_d = dc2
 cof3_d = dc3
 cof4_d = dc4


 a = [[cof1_x,cof1_y,cof3_x,cof4_x],
      [cof2_x,cof2_y,cof3_y,cof4_y],
      [cof1_z,cof2_z,cof3_z,cof4_z],
      [cof1_d,cof2_d,cof3_d,cof4_d]]

 z = [n1,
      n2,
      n3,
      n4]

 inv_a = npl.inv(a)
 
 asol = np.matmul(inv_a,z)

# [a,b] = [x^k,y^p] , x^k = a , y^k = b : x = a**(1/k) , y = b**(1/p)  

 x_p = asol[0]

 y_p = asol[1]

 z_p = asol[2]

 d_p = asol[3]

 x = nthroot(x_p,int(p_x))
 y = nthroot(y_p,int(p_y))
 z = nthroot(z_p,int(p_z))
 d = nthroot(d_p,int(p_d))

 print(x)
 print(y)
 print(z)
 print(d)
 return([x,y,z,d])

#c1x+b
def solve_zeros_lin(c1,b):
 sol = (-1*b)/(c1)
 return(sol)

def sqrt(x):
 return(float(x)**float(1/2))

#c1x^2+c2x+b
def solve_zeros_quad(c1,c2,b):
 sol1 = ((-1*c2)+(sqrt(c2**2-(4*c1*b))))/(2*c1)
 sol2 = ((-1*c2)-(sqrt(c2**2-(4*c1*b))))/(2*c1)
 print (sol1)
 print (sol2)
 return([sol1,sol2])

def sum_product(a,b,c):
 s=b
 p=a*c
 sol = []
 for i in range(s):
  q = s-i
  if q*i == p:
   sol = [q,i]
  else:
   continue
 return(sol)
 
def evaluate(function,i):
 x = i
 y = eval(function)
 return(y)

def fixed_point(f):
 fn = str(f)+'-x'
 ans = zero(fn,1,100000)
 return(ans)

def sum(f,start,end):
 running_sum = 0
 for i in range(end-start):
  running_sum = running_sum + evaluate(f,i+start)
 return(running_sum)

def zeta_r(x,acc):
 sum = 0
 for i in range(1,acc):
  sum = sum + 1/(i**x)
 return(sum)

def zeta_c(s,k):
 c = 1/(1-(2**(1-s)))
 s = sum('((-1)**(x-1))*(x**(-'+str(s)+'))',1,k)
 ans = c*s
 return(ans)

def prob(favourable_outcomes,total_outcomes):
 return(str((favourable_outcomes/total_outcomes)*100)+' %')

def e():
 y = 0
 for i in range(100):
  y = y + (1/factorial(i)) 
 return(y)

def pi():
 return(3.14159265358979323846)

def w(a):
 k = e()
 func = 'x*'+str(k)+'**x-'+str(a)
 ans = zero(func,1,1000)
 return(ans)

def prod(f,start,end):
 running_product = 1
 for i in range(end-start+1):
  running_product = running_product * evaluate(f,i+start)
 return(running_product)

def arcsin(x):
 y = 0
 for i in range(80):
  num = prod('4*(x**2)+4*x+1',0,i-1)
  ola = (x**(2*i+1))/factorial(2*i+1)
  y = y + (num*ola)
 return(y)

def sin(x):
 y = 0
 for i in range(1000):
  y = y + (((-1)**i)*((x**(2*i+1))/factorial(2*i+1)))
 return(y)  

def factorial(x):
 return(prod('x',1,x))


def fun_to_int(x,y): # The function to integrate.
 import math
 f = nthroot(1-(math.cos(x)*math.cos(y)-(math.sin(x)*math.sin(y))),2)
 return f

def factor(x):
 factorlist = []
 for i in range(1,x):
  if x % i == 0:
   factorlist.append(i)
  else:
   continue
 return(factorlist)

def dblint(xl,xu,yl,yu,step):
 x_lower_bound = xl
 x_upper_bound = xu
 y_lower_bound = yl
 y_upper_bound = yu
 step_size = step
 integral = 0
 
 x = x_lower_bound
 while (x < x_upper_bound):
    y = y_lower_bound
    while (y < y_upper_bound):
        f_lower_left = fun_to_int(x,y)
        f_lower_right = fun_to_int(x+step_size,y)
        f_upper_left = fun_to_int(x,y+step_size)
        f_upper_right = fun_to_int(x+step_size,y+step_size)
        sum = f_lower_left+f_lower_right+f_upper_left+f_upper_right
        volume = 0.25*step_size**2*sum
        integral = integral + volume
        y = y + step_size
    x = x + step_size
     
 return(integral)

def der_2(acc,f,x):
 d1 = 1/acc
 d2 = 1/acc
 def func(x):
  return(evaluate(f,x))
 go = (func(x+d1+d2) - func(x+d2)-func(x+d1)+func(x))/(d1*d2)
 return(go)

def special_factorial(z):
 k = integral('x**('+str(z)+')*'+str(e())+'**(-x)',0,10000000,1000000)
 return(k)

def stirlings_approx(x):
 a = e()
 b = pi()
 part1 = nthroot(2*b*x,2)
 part2 = (x/a)**(x)
 part = part1*part2
 return(part)

def vertex(a,b,c):
 x = (-1*b)/(2*a)
 y = ((-1*a*(b**2))/(4*(a**2)))+c 
 return((x,y))
 
def equal(f1,f2,start,acc):
 f3 = f1 + '-' + f2
 sol = zero(f3,start,acc)
 if sol =='no zeros':
  return('no solution')
 else:
  return(sol)

def spindle(d):
  return(((pi()-2)/(sqrt(2)))*(d))

def ellipse(a,b,c):
 f1 = 2/nthroot(b,2)
 start = -1*nthroot(c/a,2)
 end = nthroot(c/a,2)
 f2 = integral('nthroot('+str(c)+'-'+str(a)+'*x**2,2)',start,end,1000000)
 return(f1*f2)

def euler_machroini_constant():
 return(0.57721566490153286060651209008240243104215933593992)

def iter_f(function,start,iters):
 k = start 
 for i in range(iters):
  k = eval(function,k)
 return(k)

def chance(times,thing,k_list):
 running_prod = 1
 kai = k_list[thing - 1]
 total = total_things(k_list)
 for i in range(times):
  running_prod = running_prod * ((kai-i)/total)
 return(running_prod)

def chance_not(times_not,thing,k_list):
 running_prod = 1
 kai = k_list[thing-1]
 total = total_things(k_list)
 for i in range(0,times_not):
  running_prod = running_prod * (1-((kai-i)/total))
 return(running_prod)

def vertex(a,b,c):
 x = (-1*b)/(2*a)
 y = c-((b**2)/(4*a))
 return([x,y])
 
def mean(l):
 n = len(l)
 running_sum = 0
 for i in l:
  running_sum = running_sum+i
 avg = running_sum/n
 return(avg)

def average(l):
 return(median([l]))

def mode(array):
 most = max(list(map(array.count, array)))
 return list(set(filter(lambda x: array.count(x) == most, array)))

def deviation(a,l):
 return(a-mean(l))

def varience(l):
 rs = 0
 for i in l:
  rs = rs + (deviation(i,l)**2)
 v = rs/(len(l)-1)
 return(v)

def standard_deviation(l):
 ans = nthroot(varience(l),2)
 return(ans)

 #[a,b,c
 # d,e,f,
 # g,h,i]
 l = []
 for i in range(int(rank)):
  l.append(s)
  s = s + 1 + rank
  return(l)


def e_eq(a,k):
 rank = nthroot(len(a),2)
 l = []
 for i in range(int(rank)+1):
  l.append(i*(rank+1))
  return(l)
 o = nums(rank,0)
 lamlist = [] 
 for i in range(int(rank)**2):
  if i in o:
   lamlist.append(k)
  else:
   lamlist.append(0)
 return(lamlist)
 
def sig(x):
 val = 1/(1+e**-x)
 return(val)

def limit(func,val):
 return(evaluate(func,val-0.000000000000000001))

def solve_first_ode(x1,x2,xlabel,ylabel):
 import numpy as np
 import matplotlib.pyplot as plt 
 import scipy
 from scipy.integrate import odeint
 def model(y,t): # put the model here
  dydt = 1 #put dydt here
  return(dydt)
 y0 = 0#put init val
 t = np.linspace(0,20)
 y = odeint(model,y0,t)
 plt.plot(t,y)
 plt.xlabel(xlabel)
 plt.ylabel(ylabel)
 plt.show()

def solve_2nd_ode(x1,x2,xlabel,ylabel):
 # follow https://nathantypanski.com/blog/2014-08-23-ode-solver-py.html
 #check here for answers https://scicomp.stackexchange.com/questions/34646/attempt-to-solve-2nd-order-o-d-e-using-scipy-integrate-odeint-resulting-in-error
 #check out sympy
 import numpy as np
 import matplotlib.pyplot as plt 
 import scipy
 from scipy.integrate import odeint
 def model(y,t): # put the model here y is a matrix
  dydt = y[1] #put f' here
  ddyddt = (2*y[0]*y[1]**2+y[0]+y[0]**3-y[1]**2)/(1+y[0]**2-y[1]**2) #put f'' here
  return([dydt,ddyddt])
 y0 = 1#put init val of y 
 yp0 = 1#put init val of y'
 t = np.linspace(x1,x2,200)
 ys = odeint(model,[y0,yp0],t)
 print("printing ys")
 print(ys)
 yss = ys[:,1]
 plt.plot(t,yss)
 plt.xlabel(xlabel)
 plt.ylabel(ylabel)
 plt.show()     

def integral_graph(s,xrang,yrang,graph_func):
 F = 0
 t = 0
 def f(x):#function to be integrated 
  return(np.sin((2.7182818284590455)**x))
 d = 0.001
 for i in range(int(s/d)):
  nF = f(t)*d+F
  if graph_func == False:
   plt.scatter(t,nF,s=1,c='black')
  else: 
   plt.scatter(t,nF,s=1,c='black')
   plt.scatter(t,f(t),s=1,c='blue') 
  F = nF
  t = t + d
 plt.axis([xrang[0],xrang[1],yrang[0],yrang[1]])
 plt.show()

def solve_2nd_ode_gen(func0,funcp0,s,graph_der,axis):
 t = 0
 fp0 = funcp0
 f0 = func0
 dt = 0.005#decrease for accuracy, increase for lower rutime
 def fpl(if0,ifp0,t):
  return(if0+ifp0-t)# put the value of f'' *after isolation* in terms of f' and f and x (denoted as ifp0,if0,t respectivly)
 def fp(if0,ifp0,t):
  nt = fpl(if0,ifp0,t)
  return(nt*dt+ifp0)  
 def f(if0,ifp0,t):#dont do anything here
  return(dt*ifp0+if0) 
 plt.scatter(t,f0)
 for i in range(int(s/dt)):
  nfp0 = fp(f0,fp0,t)
  nf0 = f(f0,fp0,t)
  if graph_der == True:
   plt.scatter(t,f0,s=1,c='black')
   plt.scatter(t,fp0,s=1,c='blue')
  else:
   plt.scatter(t,f0,s=1,c='black')
  t = t + dt
  f0 = nf0
  fp0 = nfp0
 if axis == 0:     
  plt.show()
 else:
  plt.axis(axis) 
  plt.show()   

def solve_1st_ode_gen(func0,s,axis):
 t = 0 
 dt = 0.01
 f0 = func0 
 def fpl(f,t):
  return(np.sin(f)) 
 def fp(f,t):
  return(fpl(f,t)*dt+f)
 plt.scatter(t,f0)
 for i in range(int(s/dt)):
  nf0 = fp(f0,t)
  plt.scatter(t,f0,s=1,c='black')
  t = t + dt
  f0 = nf0
 if axis == 0:     
  plt.show()
 else:
  plt.axis(axis) 
  plt.show()   
       