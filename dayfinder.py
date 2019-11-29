tdd = '09/12/2019'
# format = mm/dd/yyyy
tdw = 'thursday'

print('please enter your date in mm/dd/yyyy form')
print('                                         ')

def check_m(m,y):
 if m == 1:
  return(31)   
 elif m == 2:
  if check_leap(y)==True:
   return(29)
  else:
   return(28)
 elif m == 3:
  return(31)
 elif m == 4:
  return(30)
 elif m == 5:
  return(31)
 elif m == 6:
  return(30)
 elif m == 7:
  return(31)
 elif m == 8:
  return(31)
 elif m == 9:
  return(30)
 elif m == 10:
  return(31)
 elif m == 11:
  return(30)
 elif m == 12:
  return(31)

def check_leap(y):
 if y % 4 == 0 and y % 100 != 0:
  return(True)
 else:
  return(False)

def clean(date):
 m = int(date[0]+date[1])
 d = int(date[3]+date[4])
 y = int(date[6]+date[7]+date[8]+date[9])
 return(m,d,y)

def rev_clean(m,d,y):
 nd = ''
 if len(str(m)) == 2:
  nd = nd + str(m)
 elif len(str(m)) == 1:
  nd = nd + '0' + str(m)
 nd = nd + '/'   
 if len(str(d)) == 2:
  nd = nd + str(d)
 elif len(str(d)) == 1:
  nd = nd + '0' + str(d)   
 nd = nd + '/'
 nd = nd + str(y)
 return(nd)  

def add(date):
 day = clean(date)[1]
 month = clean(date)[0]
 year = clean(date)[2]
 if check_leap(year) == True: 
  days_in_year = 366
 else:
  days_in_year = 365
 days_in_month = check_m(month,year)
 if day == days_in_month and month != 12:
  month = month + 1
  day = 1
 elif day == days_in_month and month == 12: 
  year = year + 1
  month = 1
  day = 1
 elif day != days_in_month:
  day = day + 1
 return(rev_clean(month,day,year))

def addweek(d):
 if d == 'sunday':
  return('monday')
 if d == 'monday':
  return('tuesday')
 if d == 'tuesday':
  return('wensday')
 if d == 'wensday':
  return('thursday')
 if d == 'thursday':
  return('friday')
 if d == 'friday':
  return('saturday')
 if d == 'saturday':
  return('sunday')

def day_of_week(date):
 start = tdd
 s = tdw
 while start != date:
  start = add(start)
  s = addweek(s)
 return(s)
 
# do mod 7

