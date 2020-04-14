import random
def choose_prob(l,prob_list):
 n_list = []
 for i in range(len(l)-1):
  for t in range(int(float(prob_list[i])*100)):
   n_list.append(l[i])
 return(random.choice(n_list)) 

def numfinder(l,o):
 n = 0
 for i in l:
  if i == o:
   return(n)
  else:
   n = n + 1
   continue

def jump(state_matrix,states,state):
 num = numfinder(states,state)
 li = state_matrix[num]
 return(choose_prob(states,li))

def seq(state_matrix,states,start_state,length):
 state = start_state
 for i in range(length):
  print('the current state is '+state)
  n_state = jump(state_matrix,states,state)
  state = n_state
