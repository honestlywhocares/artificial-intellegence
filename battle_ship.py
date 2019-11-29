import random
import scipy
from scipy.misc import toimage
import numpy as np
import ai_lib

board = [['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.']]

def show():
 print('.',' A','B','C','D','E','F','G','H','I','J')
 print('1 ',board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],board[0][5],board[0][6],board[0][7],board[0][8],board[0][9])   
 print('2 ',board[1][0],board[1][1],board[1][2],board[1][3],board[1][4],board[1][5],board[1][6],board[1][7],board[1][8],board[1][9])
 print('3 ',board[2][0],board[2][1],board[2][2],board[2][3],board[2][4],board[2][5],board[2][6],board[2][7],board[2][8],board[2][9])
 print('4 ',board[3][0],board[3][1],board[3][2],board[3][3],board[3][4],board[3][5],board[3][6],board[3][7],board[3][8],board[3][9])
 print('5 ',board[4][0],board[4][1],board[4][2],board[4][3],board[4][4],board[4][5],board[4][6],board[4][7],board[4][8],board[4][9])
 print('6 ',board[5][0],board[5][1],board[5][2],board[5][3],board[5][4],board[5][5],board[5][6],board[5][7],board[5][8],board[5][9])
 print('7 ',board[6][0],board[6][1],board[6][2],board[6][3],board[6][4],board[6][5],board[6][6],board[6][7],board[6][8],board[6][9])
 print('8 ',board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6],board[7][7],board[7][8],board[7][9])
 print('9 ',board[8][0],board[8][1],board[8][2],board[8][3],board[8][4],board[8][5],board[8][6],board[8][7],board[8][8],board[8][9])
 print('10',board[9][0],board[9][1],board[9][2],board[9][3],board[9][4],board[9][5],board[9][6],board[9][7],board[9][8],board[9][9])

d = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}

def max_array(arr):
 return(max(max(arr)))

def translate(place):
 if len(place) == 2:
  coor = [int(place[1])-1,d[place[0]]-1]
 else:
  coor = [9,d[place[0]]-1]
 return(coor)

def shoot(place,hom):
 coor = translate(place)
 if hom == 'hit':
  board[coor[0]][coor[1]] = '#'
 if hom == 'miss': 
  board[coor[0]][coor[1]] = '*'
 show()

def cover(blocks,place,uplr):
 coor = translate(place)
 if uplr == 'right':
  s = 0
  for i in range(blocks):
   board[coor[0]][coor[1] + s] = 'x'
   s = s + 1
 elif uplr == 'up':
  s = 0
  for i in range(blocks):
   board[coor[0]-s][coor[1]] = 'x'
   s = s + 1
 elif uplr == 'left':
  s = 0
  for i in range(blocks):
   board[coor[0]][coor[1] - s] = 'x'
   s = s + 1
 elif uplr == 'down':
  s = 0
  for i in range(blocks):
   board[coor[0] + s][coor[1]] = 'x'
   s = s + 1

def place_ship(ship,place,uplr):
 if ship == 'destroyer':
  cover(2,place,uplr)
 if ship == 'carrier':
  cover(5,place,uplr)   
 if ship == 'submarine':
  cover(3,place,uplr)   
 if ship == 'battle ship':
  cover(4,place,uplr)   
 if ship == 'cruiser':
  cover(3,place,uplr)  

def t(ship):
 if ship == 'destroyer':
  return(2)
 elif ship == 'carrier':
  return(5)   
 elif ship == 'submarine':
  return(3)  
 elif ship == 'battle ship':
  return(4)  
 elif ship == 'cruiser':
  return(3) 

def check_bound(uplr,ship,place):
 coor = translate(place)
 def check_up(coor,ship):
  if coor[0]+1 < t(ship):
   return(False)
  elif coor[0]+1 > t(ship):
   return(True) 
  elif coor[0]+1 == t(ship):
   return(True)
 def check_down(coor,ship):
  if coor[0]+1 < 11-t(ship):
   return(True)
  elif coor[0]+1 > 11-t(ship):
   return(False) 
  elif coor[0]+1 == 11-t(ship):
   return(True)
 def check_left(coor,ship):
  if coor[1]+1 < t(ship):
   return(False)
  elif coor[1]+1 > t(ship):
   return(True) 
  elif coor[1]+1 == t(ship):
   return(True)
 def check_right(coor,ship):
  if coor[1]+1 < 11-t(ship):
   return(True)
  elif coor[1]+1 > 11-t(ship):
   return(False) 
  elif coor[1]+1 == 11-t(ship):
   return(True)
 if uplr == 'right':
  return(check_right(coor,ship))
 elif uplr == 'left':
  return(check_left(coor,ship))
 elif uplr == 'up':
  return(check_up(coor,ship))
 elif uplr == 'down':
  return(check_down(coor,ship))

def check_coll(place,ship,uplr):
 ans = True
 blocks = t(ship)
 coor = translate(place)
 if uplr == 'right':
  s = 0
  for i in range(blocks):
   if board[coor[0]][coor[1] + s] == 'x' or board[coor[0]][coor[1] + s] == '*' or board[coor[0]][coor[1] + s] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'up':
  s = 0
  for i in range(blocks):
   if board[coor[0]-s][coor[1]] == 'x' or board[coor[0]-s][coor[1]] == '*' or board[coor[0]-s][coor[1]] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'left':
  s = 0
  for i in range(blocks):
   if board[coor[0]][coor[1] - s] == 'x' or board[coor[0]][coor[1] - s] == '*' or board[coor[0]][coor[1] - s] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'down':
  s = 0
  for i in range(blocks):
   if board[coor[0] + s][coor[1]] == 'x' or board[coor[0] + s][coor[1]] == '*' or board[coor[0] + s][coor[1]] == '#':  
    return(False)
   else:
    s = s + 1
 return(ans)

def check(place,ship,uplr):
 if check_bound(uplr,ship,place) == True and check_coll(place,ship,uplr) == True:
  return(True)  
 else:
  return(False)

def clear():
 for i in range(0,10):
  for t in range(0,10):
   if board[i][t] == 'x':
    board[i][t] = '.'
   else:
    continue

def delete(place):
 coor = translate(place)
 board[coor[0]][coor[1]] = '.'

def gen_rand(ships):
 def rand_carrier():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check(move,'carrier',uplr) == False:
    done = False
   else:
    place_ship('carrier',move,uplr)
    break
 def rand_destroyer():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check(move,'destroyer',uplr) == False:
    done = False
   else:
    place_ship('destroyer',move,uplr)
    break
 def rand_submarine():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check(move,'submarine',uplr) == False:
    done = False
   else:
    place_ship('submarine',move,uplr)
    break
 def rand_battleship():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check(move,'battle ship',uplr) == False:
    done = False
   else:
    place_ship('battle ship',move,uplr)
    break
 def rand_cruiser():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check(move,'cruiser',uplr) == False:
    done = False
   else:
    place_ship('cruiser',move,uplr)
    break
 for i in ships:
  if i == 'carrier':
   rand_carrier()
  elif i == 'cruiser':
   rand_cruiser()
  elif i == 'battle ship':
   rand_battleship()
  elif i == 'destroyer':
   rand_destroyer()
  elif i == 'submarine':
   rand_submarine()

def prob(place,iters,ships):
 c = 0
 coor = translate(place)
 for i in range(iters):
  gen_rand(ships)
  if board[coor[0]][coor[1]] == 'x':
   c = c + 1
   clear()
  else:
   clear()
 return(c/iters)  

def heat_vals(iters,ships):
 new = []
 for i in ['A','B','C','D','E','F','G','H','I','J']:
  newn = []
  for t in ['1','2','3','4','5','6','7','8','9','10']:
   place = i+t
   newn.append(prob(place,iters,ships))
  new.append(newn)
  newn = []
 return(new)

def rev(coor):
 rd = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}
 s = str(rd[coor[0]])+str(coor[1])      
 return(s)
 
def best(iters,ships):
 hm = heat_vals(iters,ships)
 return(rev(find(np.amax(hm),hm)))

def flatten(l):
 l = np.array(l)
 l = l.flatten()
 l = list(l)
 return(l)

def find(obj,l):
 inum = 0
 tnum = 0 
 for i in l:
  inum = inum + 1
  tnum = 0
  for t in i:
   tnum = tnum + 1
   if t == obj:
    return([inum,tnum])
   else:
    continue

comp_board =  [['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.']]
 
def show_some(board):
 print('.',' A','B','C','D','E','F','G','H','I','J')
 print('1 ',board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],board[0][5],board[0][6],board[0][7],board[0][8],board[0][9])   
 print('2 ',board[1][0],board[1][1],board[1][2],board[1][3],board[1][4],board[1][5],board[1][6],board[1][7],board[1][8],board[1][9])
 print('3 ',board[2][0],board[2][1],board[2][2],board[2][3],board[2][4],board[2][5],board[2][6],board[2][7],board[2][8],board[2][9])
 print('4 ',board[3][0],board[3][1],board[3][2],board[3][3],board[3][4],board[3][5],board[3][6],board[3][7],board[3][8],board[3][9])
 print('5 ',board[4][0],board[4][1],board[4][2],board[4][3],board[4][4],board[4][5],board[4][6],board[4][7],board[4][8],board[4][9])
 print('6 ',board[5][0],board[5][1],board[5][2],board[5][3],board[5][4],board[5][5],board[5][6],board[5][7],board[5][8],board[5][9])
 print('7 ',board[6][0],board[6][1],board[6][2],board[6][3],board[6][4],board[6][5],board[6][6],board[6][7],board[6][8],board[6][9])
 print('8 ',board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6],board[7][7],board[7][8],board[7][9])
 print('9 ',board[8][0],board[8][1],board[8][2],board[8][3],board[8][4],board[8][5],board[8][6],board[8][7],board[8][8],board[8][9])
 print('10',board[9][0],board[9][1],board[9][2],board[9][3],board[9][4],board[9][5],board[9][6],board[9][7],board[9][8],board[9][9])

def cover_comp(blocks,place,uplr):
 coor = translate(place)
 if uplr == 'right':
  s = 0
  for i in range(blocks):
   comp_board[coor[0]][coor[1] + s] = 'x'
   s = s + 1
 elif uplr == 'up':
  s = 0
  for i in range(blocks):
   comp_board[coor[0]-s][coor[1]] = 'x'
   s = s + 1
 elif uplr == 'left':
  s = 0
  for i in range(blocks):
   comp_board[coor[0]][coor[1] - s] = 'x'
   s = s + 1
 elif uplr == 'down':
  s = 0
  for i in range(blocks):
   comp_board[coor[0] + s][coor[1]] = 'x'
   s = s + 1

def place_ship_comp(ship,place,uplr):
 if ship == 'destroyer':
  cover_comp(2,place,uplr)
 if ship == 'carrier':
  cover_comp(5,place,uplr)   
 if ship == 'submarine':
  cover_comp(3,place,uplr)   
 if ship == 'battle ship':
  cover_comp(4,place,uplr)   
 if ship == 'cruiser':
  cover_comp(3,place,uplr)  

def t(ship):
 if ship == 'destroyer':
  return(2)
 elif ship == 'carrier':
  return(5)   
 elif ship == 'submarine':
  return(3)  
 elif ship == 'battle ship':
  return(4)  
 elif ship == 'cruiser':
  return(3) 


def check_bound_comp(uplr,ship,place):
 coor = translate(place)
 def check_up(coor,ship):
  if coor[0]+1 < t(ship):
   return(False)
  elif coor[0]+1 > t(ship):
   return(True) 
  elif coor[0]+1 == t(ship):
   return(True)
 def check_down(coor,ship):
  if coor[0]+1 < 11-t(ship):
   return(True)
  elif coor[0]+1 > 11-t(ship):
   return(False) 
  elif coor[0]+1 == 11-t(ship):
   return(True)
 def check_left(coor,ship):
  if coor[1]+1 < t(ship):
   return(False)
  elif coor[1]+1 > t(ship):
   return(True) 
  elif coor[1]+1 == t(ship):
   return(True)
 def check_right(coor,ship):
  if coor[1]+1 < 11-t(ship):
   return(True)
  elif coor[1]+1 > 11-t(ship):
   return(False) 
  elif coor[1]+1 == 11-t(ship):
   return(True)
 if uplr == 'right':
  return(check_right(coor,ship))
 elif uplr == 'left':
  return(check_left(coor,ship))
 elif uplr == 'up':
  return(check_up(coor,ship))
 elif uplr == 'down':
  return(check_down(coor,ship))

def check_coll_comp(place,ship,uplr):
 ans = True
 blocks = t(ship)
 coor = translate(place)
 if uplr == 'right':
  s = 0
  for i in range(blocks):
   if comp_board[coor[0]][coor[1] + s] == 'x' or board[coor[0]][coor[1] + s] == '*' or board[coor[0]][coor[1] + s] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'up':
  s = 0
  for i in range(blocks):
   if comp_board[coor[0]-s][coor[1]] == 'x' or board[coor[0]-s][coor[1]] == '*' or board[coor[0]-s][coor[1]] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'left':
  s = 0
  for i in range(blocks):
   if comp_board[coor[0]][coor[1] - s] == 'x' or board[coor[0]][coor[1] - s] == '*' or board[coor[0]][coor[1] - s] == '#':
    return(False)
   else:
    s = s + 1
 elif uplr == 'down':
  s = 0
  for i in range(blocks):
   if comp_board[coor[0] + s][coor[1]] == 'x' or board[coor[0] + s][coor[1]] == '*' or board[coor[0] + s][coor[1]] == '#':  
    return(False)
   else:
    s = s + 1
 return(ans)

def check_comp(place,ship,uplr):
 if check_bound_comp(uplr,ship,place) == True and check_coll_comp(place,ship,uplr) == True:
  return(True)  
 else:
  return(False)

def place_comp():
 def rand_carrier():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check_comp(move,'carrier',uplr) == False:
    done = False
   else:
    place_ship_comp('carrier',move,uplr)
    break  
 def rand_destroyer():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check_comp(move,'destroyer',uplr) == False:
    done = False
   else:
    place_ship_comp('destroyer',move,uplr)
    break
 def rand_submarine():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check_comp(move,'submarine',uplr) == False:
    done = False
   else:
    place_ship_comp('submarine',move,uplr)
    break
 def rand_battleship():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check_comp(move,'battle ship',uplr) == False:
    done = False
   else:
    place_ship_comp('battle ship',move,uplr)
    break
 def rand_cruiser():
  done = False
  while done == False: 
   ore = random.randint(1,4)
   if ore == 1:
    uplr = 'up'
   elif ore == 2:
    uplr = 'right'
   elif ore == 3:
    uplr = 'down'
   elif ore == 4:
    uplr = 'left'
   letter = random.choice(['A','B','C','D','E','F','G','H','I','J'])
   num = random.choice(['1','2','3','4','5','6','7','8','9','10'])
   move = letter + num
   if check_comp(move,'cruiser',uplr) == False:
    done = False
   else:
    place_ship_comp('cruiser',move,uplr)
    break
 rand_carrier()
 rand_battleship()
 rand_cruiser()
 rand_destroyer()
 rand_submarine()
 
def clear_comp():
 for i in range(0,10):
  for t in range(0,10):
   if comp_board[i][t] == 'x':
    comp_board[i][t] = '.'
   else:
    continue

def delete_comp(place):
 coor = translate(place)
 comp_board[coor[0]][coor[1]] = '.'

def shoot_comp(place):
 coor = translate(place)
 if comp_board[coor[0]][coor[1]] == 'x':
  comp_board[coor[0]][coor[1]] = '#'
  print('hit')
 else: 
  print('miss')
  comp_board[coor[0]][coor[1]] = '*'

def heat_map(iters,ships):
 hv = heat_vals(iters,ships)
 toimage(hv).show()

def show_comp():
 show_some(comp_board)