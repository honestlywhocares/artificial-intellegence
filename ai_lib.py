import numpy as np
import random

#computationally find whether pd is positive or negative and takes a step of size s

def sigmoid(x):
 e = 2.718281828459045
 return(1/(1+(e**(-x))))

def relu(x):
 if x > 0:
  return(x)
 else:
  return(0)

def leaky_relu(x,slope):
 if x > 0:
  return(x)
 else:
  return(slope*x)

def input_layer(inputs):
 in_layer = list(inputs)
 return(in_layer)

def layer_to_layer(layer1_vector,weight_matrix,bias_vector,activation):
 layer2a = np.dot(weight_matrix,layer1_vector)+bias_vector  
 layer2 = []
 if activation == 'sigmoid':
  for i in layer2a:
   layer2.append(sigmoid(i))
 elif activation == 'relu':
  for i in layer2a:
   layer2.append(relu(i))
 elif activation == 'leaky relu':
  for i in layer2a:
   layer2.append(leaky_relu(i,0.01))   
 return(layer2)

def gen_rand_weight_matrix(layer1_num,layer2_num):
 w1 = []
 w2 = []
 for i in range(layer2_num):
  w1.append(w2)
  w2 = []
  for i in range(layer1_num):
   w2.append(random.random())
 for i in range(layer1_num):
  w1[0].append(random.random()) 
 return(w1)

def gen_rand_bias(layer2_num):
 b = []
 for i in range(layer2_num): 
  b.append(random.random())
 return(b) 

def squared_cost(target,result):
 c = 0
 n = 0
 for i in target:
  c = c + ((target[n]-result[n])**2) 
  n = n + 1
 return(0.5*c)

def sigprime(x):
 return(sigmoid(x)*(1-sigmoid(x)))

def reluprime(x):
 if x < 0:
  return(0)
 else:
  return(1)

def leaky_relu_prime(slope,x):
 if x < 0:
  return(slope)
 else:
  return(1)

def directional_cost(target,result):
 c = []
 n = 0
 for i in target:
  c.append(target[n] - result[n]) 
  n = n + 1
 return(c)

#weights = [weight_matix for input layer,etc...], bias is the same concept
