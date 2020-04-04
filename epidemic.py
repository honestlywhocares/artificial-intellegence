import random
import matplotlib.pyplot as plt

#   . -> unaffected
#   * -> infected 
#   x -> dead
#   r -> recovered 

population = [['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.','.','.','.','.','.','.']]


chance_of_recovery = 0.4
chance_of_death = 0.1
chance_of_infection = 0.75
travel_chance = 0.04
start = [1,1]

def show():
 print(population[0][0],population[0][1],population[0][2],population[0][3],population[0][4],population[0][5],population[0][6],population[0][7],population[0][8],population[0][9],population[0][10],population[0][11],population[0][12],population[0][13])
 print(population[1][0],population[1][1],population[1][2],population[1][3],population[1][4],population[1][5],population[1][6],population[1][7],population[1][8],population[1][9],population[1][10],population[1][11],population[1][12],population[1][13])
 print(population[2][0],population[2][1],population[2][2],population[2][3],population[2][4],population[2][5],population[2][6],population[2][7],population[2][8],population[2][9],population[2][10],population[2][11],population[2][12],population[2][13])
 print(population[3][0],population[3][1],population[3][2],population[3][3],population[3][4],population[3][5],population[3][6],population[3][7],population[3][8],population[3][9],population[3][10],population[3][11],population[3][12],population[3][13])
 print(population[4][0],population[4][1],population[4][2],population[4][3],population[4][4],population[4][5],population[4][6],population[4][7],population[4][8],population[4][9],population[4][10],population[4][11],population[4][12],population[4][13])
 print(population[5][0],population[5][1],population[5][2],population[5][3],population[5][4],population[5][5],population[5][6],population[5][7],population[5][8],population[5][9],population[5][10],population[5][11],population[5][12],population[5][13])
 print(population[6][0],population[6][1],population[6][2],population[6][3],population[6][4],population[6][5],population[6][6],population[6][7],population[6][8],population[6][9],population[6][10],population[6][11],population[6][12],population[6][13])
 print(population[7][0],population[7][1],population[7][2],population[7][3],population[7][4],population[7][5],population[7][6],population[7][7],population[7][8],population[7][9],population[7][10],population[7][11],population[7][12],population[7][13])
 print(population[8][0],population[8][1],population[8][2],population[8][3],population[8][4],population[8][5],population[8][6],population[8][7],population[8][8],population[8][9],population[8][10],population[8][11],population[8][12],population[8][13])
 print(population[9][0],population[9][1],population[9][2],population[9][3],population[9][4],population[9][5],population[9][6],population[9][7],population[9][8],population[9][9],population[9][10],population[9][11],population[9][12],population[9][13])
 print(population[10][0],population[10][1],population[10][2],population[10][3],population[10][4],population[10][5],population[10][6],population[10][7],population[10][8],population[10][9],population[10][10],population[10][11],population[10][12],population[10][13])
 print(population[11][0],population[11][1],population[11][2],population[11][3],population[11][4],population[11][5],population[11][6],population[11][7],population[11][8],population[11][9],population[11][10],population[11][11],population[11][12],population[11][13])
 print(population[12][0],population[12][1],population[12][2],population[12][3],population[12][4],population[12][5],population[12][6],population[12][7],population[12][8],population[12][9],population[12][10],population[12][11],population[12][12],population[12][13])
 print(population[13][0],population[13][1],population[13][2],population[13][3],population[13][4],population[13][5],population[13][6],population[13][7],population[13][8],population[13][9],population[13][10],population[13][11],population[13][12],population[13][13])

def infect(coor):
 population[coor[0]][coor[1]] = '*'

def kill(coor):
 population[coor[0]][coor[1]] = 'x'

def cure(coor):
 population[coor[0]][coor[1]] = 'r'

def chance(p,vcoor):
 k = 0
 x = int(100*p)
 l = []
 for i in range(100-x):
  l.append(False)
 for q in range(x):
  l.append(True) 
 o = random.choice(l)
 if o == True and population[vcoor[0]][vcoor[1]] == '.':
  infect(vcoor)
 else:
  k = 1

def check_edge(coor):
 if coor[0] == 0 and coor[1] == 0:
  return('top left')
 elif coor[0] == 0 and coor[1] == 13:
  return('top right') 
 elif coor[0] == 13 and coor[1] == 0:
  return('bottom left')
 elif coor[0] == 13 and coor[1] == 13:
  return('bottom right')
 elif coor[0] != 0 and coor[0] != 13 and coor[1] == 0:
  return('left')
 elif coor[0] == 0 and coor[1] != 0 and coor[1] != 13:
  return('top')
 elif coor[0] != 0 and coor[0] != 13 and coor [1] == 13:
  return('right')
 elif coor[0] == 13 and coor[1] != 0 and coor[1] != 13:
  return('bottom')
 else:
  return('not an edge')

def infect_tl():
 chance(chance_of_infection,[0,1])
 chance(chance_of_infection,[1,0])

def infect_tr():
 chance(chance_of_infection,[0,12])
 chance(chance_of_infection,[1,13])

def infect_bl():
 chance(chance_of_infection,[12,0])
 chance(chance_of_infection,[13,1])

def infect_br():
 chance(chance_of_infection,[13,12])
 chance(chance_of_infection,[12,13])
 
def infect_top(coor):
 chance(chance_of_infection,[1,coor[1]])
 chance(chance_of_infection,[0,coor[1]-1])
 chance(chance_of_infection,[0,coor[1]+1])

def infect_bottom(coor):
 chance(chance_of_infection,[12,coor[1]])
 chance(chance_of_infection,[13,coor[1]-1])
 chance(chance_of_infection,[13,coor[1]+1])

def infect_left(coor):
 chance(chance_of_infection,[coor[0],1])
 chance(chance_of_infection,[coor[0]-1,0])
 chance(chance_of_infection,[coor[0]+1,0])

def infect_right(coor):
 chance(chance_of_infection,[coor[0],12])
 chance(chance_of_infection,[coor[0]-1,13])
 chance(chance_of_infection,[coor[0]+1,13])

def infect_center(coor):
 chance(chance_of_infection,[coor[0],coor[1]-1])
 chance(chance_of_infection,[coor[0],coor[1]+1])
 chance(chance_of_infection,[coor[0]-1,coor[1]])
 chance(chance_of_infection,[coor[0]+1,coor[1]])

def infect_around(coor):
 v = check_edge(coor)
 if v == 'top left':
  infect_tl()
 elif v =='top right':
  infect_tr()
 elif v =='bottom left':
  infect_bl()
 elif v =='bottom right':
  infect_br()
 elif v == 'top':
  infect_top(coor)
 elif v == 'bottom':
  infect_bottom(coor)
 elif v == 'right':
  infect_right(coor)
 elif v == 'left':
  infect_left(coor)
 elif v == 'not an edge':
  infect_center(coor)

def infect_pop():
 coorlist = []
 for row in range(len(population)):
  for person in range(len(population)):
   if population[row][person] == '*':
    coorlist.append([row,person])
   else:
    continue
 for c in coorlist:
  infect_around(c)

def chance_cure(p1,p2,vcoor):
 x1 = int(100*p1) 
 x2 = int(100*p2) 
 if count_infected()+count_dead()+count_recovered() >= 150:
  x1 = x1 - 3
  x2 = x2 + 3
 l = []
 for i in range(x1):
  l.append('1')
 for q in range(x2):
  l.append('2') 
 for t in range(100-x1-x2):
  l.append('3')
 o = random.choice(l)
 return(o)

def cure_pop(): 
 coorlist = []
 for row in range(len(population)):
  for person in range(len(population)):
   if population[row][person] == '*':
    coorlist.append([row,person])
   else:
    continue
 for c in coorlist:
  cu = chance_cure(chance_of_recovery,chance_of_death,c)
  if cu == '1':
   population[c[0]][c[1]] = 'r'
  elif cu == '2':
   population[c[0]][c[1]] = 'x'
  elif cu == '3':
   population[c[0]][c[1]] = '*'

def travel(coor1,coor2):
 nc1 = population[coor2[0]][coor2[1]]
 nc2 = population[coor1[0]][coor1[1]]
 population[coor1[0]][coor1[1]] = nc1
 population[coor2[0]][coor2[1]] = nc2
 
def chance_travel(p,vcoor):
 k = 0
 x = int(100*p)
 if count_infected()+count_recovered()+count_dead() >= 100:
  x = x - 1
 l = []
 for i in range(100-x):
  l.append(False)
 for q in range(x):
  l.append(True) 
 o = random.choice(l)
 if o == True:
  travel(vcoor,[random.randint(0,13),random.randint(0,13)])
 else:
  k = 1

def travel_pop():
 for row in range(len(population)):
  for person in range(len(population)):
   chance_travel(travel_chance,[row,person])
  else:
    continue

def timestep():
 infect_pop()
 infect_pop()
 travel_pop()
 cure_pop()

def count_infected():
 count = 0
 for row in range(len(population)):
  for person in range(len(population)):
   if population[row][person] == '*':
    count = count + 1
   else:
    continue
 return(count)

def count_dead():
 count = 0
 for row in range(len(population)):
  for person in range(len(population)):
   if population[row][person] == 'x':
    count = count + 1
   else:
    continue
 return(count)

def count_recovered():
 count = 0
 for row in range(len(population)):
  for person in range(len(population)):
   if population[row][person] == 'r':
    count = count + 1
   else:
    continue 
 return(count)

def go(time):
 # blue - recovered
 # red - infected
 # black - dead
 # green- unaffected
 l1 = []
 l2 = []
 l3 = []
 l4 = []
 infect(start)
 n = []
 t = 0
 for i in range(time): 
  timestep()
  show()
  print('------------------------------------')
  l1.append(count_infected())
  l2.append(count_dead())
  l3.append(count_recovered())
  l4.append(196-count_recovered()-count_infected()-count_dead())
  n.append(t)
  t = t + 1
 plt.plot(n,l1,color='red')
 plt.plot(n,l2,color='black')
 plt.plot(n,l3,color='blue')
 plt.plot(n,l4,color='green')
 plt.show()