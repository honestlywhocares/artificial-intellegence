print ("welcome to fluidity")
print ("heres a quick guide to what the symbols represent:")
print (". : still fuid")
print ('* : slow fluid')
print ('- : fast moving fluid')

graph = [['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','',''],
         ['','','','','','','','','','','']]

def velocity_graph(x,y,t):
 f1 = x+t
 f2 = y+t
 #vector = 2x+1i+y-1j
 #length = (f1**2+f2**2)**(1/2)
 mag = (f1**2+f2**2)**(1/2)
 return(mag)

def d_graph(x,y,t):
 f1 = x+t
 f2 = y+t
 if f1 > f2:
  mag = '>'
 elif f1 < f2:
  mag = '^'
 elif f1 == f2:
  mag = '*'

def show():
 print("______________________________________________________________________________________________________________________________________________________")
 print(graph[0][0],graph[0][1],graph[0][2],graph[0][3],graph[0][4],graph[0][5],graph[0][6],graph[0][7],graph[0][8],graph[0][9],graph[0][10])
 print(graph[1][0],graph[1][1],graph[1][2],graph[1][3],graph[1][4],graph[1][5],graph[1][6],graph[1][7],graph[1][8],graph[1][9],graph[1][10])
 print(graph[2][0],graph[2][1],graph[2][2],graph[2][3],graph[2][4],graph[2][5],graph[2][6],graph[2][7],graph[2][8],graph[2][9],graph[2][10])
 print(graph[3][0],graph[3][1],graph[3][2],graph[3][3],graph[3][4],graph[3][5],graph[3][6],graph[3][7],graph[3][8],graph[3][9],graph[3][10])
 print(graph[4][0],graph[4][1],graph[4][2],graph[4][3],graph[4][4],graph[4][5],graph[4][6],graph[4][7],graph[4][8],graph[4][9],graph[4][10])
 print(graph[5][0],graph[5][1],graph[5][2],graph[5][3],graph[5][4],graph[5][5],graph[5][6],graph[5][7],graph[5][8],graph[5][9],graph[5][10])
 print(graph[6][0],graph[6][1],graph[6][2],graph[6][3],graph[6][4],graph[6][5],graph[6][6],graph[6][7],graph[6][8],graph[6][9],graph[6][10])
 print(graph[7][0],graph[7][1],graph[7][2],graph[7][3],graph[7][4],graph[7][5],graph[7][6],graph[7][7],graph[7][8],graph[7][9],graph[7][10])
 print(graph[8][0],graph[8][1],graph[8][2],graph[8][3],graph[8][4],graph[8][5],graph[8][6],graph[8][7],graph[8][8],graph[8][9],graph[8][10])
 print(graph[9][0],graph[9][1],graph[9][2],graph[9][3],graph[9][4],graph[9][5],graph[9][6],graph[9][7],graph[9][8],graph[9][9],graph[9][10])
 print(graph[10][0],graph[10][1],graph[10][2],graph[10][3],graph[10][4],graph[10][5],graph[10][6],graph[10][7],graph[10][8],graph[10][9],graph[10][10])
 print("______________________________________________________________________________________________________________________________________________________")

def line_calc(line_num,t):
 for i in range(11):
  mag = velocity_graph(i,line_num,t)
  if mag >= 10:
   graph[line_num][i] = '-'
  elif mag == 0:
   graph[line_num][i] = '.'
  elif 0<mag<10:
   graph[line_num][i] = '*'

def dir_calc(line_num,t):
 for i in range(11):
  mag = d_graph(i,line_num,t)
  if mag >= 10:
   graph[line_num][i] = '-'
  elif mag == 0:
   graph[line_num][i] = '.'
  elif 0<mag<10:
   graph[line_num][i] = '*'


def fluid_speed(t):
 for q in range(11):
  line_calc(q,t)
 show()
 

def speed_sim(timesteps):
 t = 0 
 for i in range(timesteps):
  fluid_speed(t)
  t = t + 1

def fluid_dir(t):
 for q in range(11):
  dir_calc(q,t)
 show()

def direction_sim(timesteps):
 t = 0 
 for i in range(timesteps):
  fluid_dir(t)
  t = t + 1





