import random 
import matplotlib.pyplot as plt
e = 2.7182818284590455

nw = 1

first = 'buy'

def relu(i):
 if i < 0:
  return(0)
 elif i > 1:
  return(1)
 else:
  return(i)

def td(n):
 return(n - (n % 0.0001))

def chance(nw,l):
 if l == 'buy':
  c = relu((-0.05*nw)+(0.1 + 1/(1+(e**(-0.1*nw)))))
 else:
  c = relu((-0.05*nw)+(-0.1 + 1/(1+(e**(-0.1*nw)))))
 c = td(c)
 t = []
 for i in range(int(c*10000)):
  t.append(True)
 for q in range(int(10000 - int(c*10000))): 
  t.append(False)
 if random.choice(t) == True:
  return('buy')
 else:
  return('sell')
 
def transaction(nw,t):
 if t ==  'buy':
  a = nw + 0.1
  nw = a
 else:
  a = nw - 0.1 
  nw = a
 return(nw)

def go(nw,first,r):
 last = first
 l = []
 l.append(nw)
 for round in range(r):
  nw = transaction(nw,chance(nw,last))
  l.append(nw)
 plt.plot(l)
 plt.axis([0,r,min(l),max(l)])
 plt.show()
 