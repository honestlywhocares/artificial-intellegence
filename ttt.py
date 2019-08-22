import numpy as np
import test_learn as tl

def shape(array):
 x = np.array(array)
 return(x.shape)  

board = ['.','.','.',
         '.','.','.',
         '.','.','.']
def show():
 print(str(board[0]) + ' | ' + str(board[1])+ ' | ' + str(board[2]))
 print('----------')
 print(str(board[3]) + ' | ' + str(board[4])+ ' | ' + str(board[5]))
 print('----------')
 print(str(board[6]) + ' | ' + str(board[7])+ ' | ' + str(board[8]))

def move(pos,p):
 board[pos] = p
 show()
 
def eval(board):
 val = 0
 n = 0
 for i in board:
  if i == 'x' and n in [0,2,6,8]:
   val = val + 2
   n = n + 1
  elif i == 'x' and n == 4:
   val = val + 3
   n = n + 1
  elif i == 'x' and n in [1,3,5,7]:
   val = val + 1
   n = n + 1
  elif i == 'o' and n in [0,2,6,8]:
   val = val - 2
   n = n + 1
  elif i == 'o' and n == 4:
   val = val - 3
   n = n + 1
  elif i == 'o' and n in [1,3,5,7]:
   val = val - 1
   n = n + 1
  elif i == '.':
   val = val + 0
   n = n + 1
 return(val)

def legal_moves(board):
 l = []
 n = 0
 for i in board:
  if i == 'x' or i == 'o':
   n = n + 1
  else:
   l.append(n)
   n = n + 1

def trans(board):
 n = 0
 new_board = [] 
 for i in board:
  if i == 'x':
   new_board.append(1)
   n = n + 1
  elif i == 'o':
   new_board.append(-1)
   n = n + 1
  elif i == '.':
   new_board.append(0)
   n = n + 1
 return(new_board) 

def free(board):
 n = 0
 l = []
 for i in board:
  if i == '.':
   l.append(n)
  else:
   n = n
  n = n + 1
 return(l,len(l))
 
def minimax(start,depth):
 k = 0
 if depth % 2 == 0:
  end = 'min'
 else:
  end = 'max'
 moves = legal_moves(start)
 vboard = start
   
def go(board):
 output = free(board)[1]
 inp = trans(board)
 print(output)
 print(inp)
 print(shape(output))
 print(shape(inp))
 return(tl.model(inp,output))






