import os
import subprocess

def scan():
 execute_command('''wmic service get name,displayname,pathname,startmode |findstr /i "Auto" |findstr /i /v "C:\Windows\\" |findstr /i /v """''',False,True) 

def remote_execute(ip,username,password,command):
 exec_string = 'psexec \\\\{}'.format(ip)+' -u {}'.format(username)+' -p {}'.format(password)+" "+command
 execute_command(exec_string,False,False)

def execute_command(command,kill,ret):
# command has to look different depending on if it retained or not(either regular string or subprocess check_output form) 
 if ret == False:
  execute_commands([command],kill) 
 else:
  out=subprocess.check_output(command)
  return(out)
 
def scan_network():
 def find_ip(s):
  iplist = []
  c = ['1','9','2'] 
  for i in range(len(s)-13):
   n_3 = [s[i],s[i+1],s[i+2]]
   ip = s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]+s[i+6]+s[i+7]+s[i+8]+s[i+9]+s[i+10]+s[i+11]+s[i+12]+s[i+13]
   if n_3 == c:
    iplist.append(ip)
   else:
    continue
  return(iplist)    

 def ip_clean(l):
  n_l = []
  def ip_clean1(o):
   l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','/','-','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',':','''"''','\\']
   for i in o:
    if i in l:
     o = o.replace(i,'')
    else:
     continue 
   return(o)
  for t in l:
   n_l.append(ip_clean1(t))
  return(n_l)
  
 ip_list = (ip_clean(find_ip(str(execute_command('arp -a',False,True)))))
 number = 0
 for i in ip_list:
  number = number + 1
  print('ip no.'+str(number) + ' is '+str(i))

def port_scan_over_network():
 def find_ip(s):
  iplist = []
  c = ['1','9','2'] 
  for i in range(len(s)-13):
   n_3 = [s[i],s[i+1],s[i+2]]
   ip = s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]+s[i+6]+s[i+7]+s[i+8]+s[i+9]+s[i+10]+s[i+11]+s[i+12]+s[i+13]
   if n_3 == c:
    iplist.append(ip)
   else:
    continue
  return(iplist)    

 def ip_clean(l):
  n_l = []
  def ip_clean1(o):
   l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','/','-','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',':','''"''','\\']
   for i in o:
    if i in l:
     o = o.replace(i,'')
    else:
     continue 
   return(o)
  for t in l:
   n_l.append(ip_clean1(t))
  return(n_l)
  
 ip_list = (ip_clean(find_ip(str(execute_command('arp -a',False,True)))))
 for q in ip_list:
  print('scaning ip-'+q+' for open ports')
  execute_command('nmap -vv -sS -O '+q,False,False)
  print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def execute_commands(commands,kill):
 if kill == False:
  exec_string = 'cmd /k "'
  for i in range(len(commands)):
   exec_string = exec_string + str(commands[i]) + ' & '
  exec_string = exec_string + '"'
  os.system(exec_string)
 else:
  exec_string = 'cmd /c "'
  for i in range(len(commands)):
   exec_string = exec_string + str(commands[i]) + ' & '
  exec_string = exec_string + '"'
  os.system(exec_string)