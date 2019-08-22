nodespace = []
connect_space = []
inboxes = []
password_space = {}

def node(name,password):
 password_space[password] = name
 nodespace.append(name)
 inboxes.append([name])
 print('your node has been added')
 return(nodespace)

def num_nodespace():
 return(len(nodespace))

def num_connection_space():
 return(len(connect_space))

def connect(node1,node2):
 connect_space.append([node1,node2])
 print('your connection has been added')
 return(connect_space)

def friends(name):
 return(len(friend_names(name)))

def send(sender,reciever,message):
 for i in inboxes:
  if i[0] == reciever:
   i.append(sender + ' to ' + reciever +':'+ message)
  else:
   continue

def open_inbox(name,password):
 if password_space[password] == name:
  for i in inboxes:
   if i[0] == name:
    print(i)
   else:
    continue

def delete_message(name,password,message):
 if password_space[password] == name:
  for i in inboxes:
   if i[0] == name:
    i.remove(message)
   else:
    continue

def clear_message(name,password):
 if password_space[password] == name:
  for i in inboxes:
   if i[0] == name:
    for t in i:
     if t == name:
      continue
     else:
      i.remove(t)
   else:
    continue

def recommended_friend(name):
 r = None
 for i in connect_space:
  if i[0] == name:
   sol = i[1]
  elif i[1] == name:
   sol = [0]
 for t in connect_space:
  if t[0] == sol and t[1] != name:
   r = t[1]
  elif t[1] == sol and t[0] != name:
   r = t[0]
  else:
   continue
 if r == None:
  return
 else:
  send('system',name,'you have 1 recommended_friend: '+r)

def friend_names(name):
 li = []
 for i in connect_space:
  if i[0] == name:
   li.append(i[1])
  elif i[1] == name:
   li.append(i[0])
  else:
   continue
 return(li)

def sprawl(name):
 k = friend_names(name)
 li = []
 for i in k:
  li.append(i) 
 return(li)
