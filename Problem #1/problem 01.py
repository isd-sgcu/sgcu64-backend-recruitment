def x1(n,c):
  if(x=='1' or x=='4'):
    c=c+'    '
  else:
    c=c+' __ '
  return c
def x2(n,c):
  if(x=='0'):
    c=c+'|  |'
  elif(x=='1' or x=='7'):
    c=c+'   |'
  elif(x=='2' or x=='3'):
    c=c+' __|'
  elif(x=='4' or x=='8' or x=='9'):
    c=c+'|__|'
  elif(x=='5' or x=='6'):
    c=c+'|__ '
  return c
def x3(n,c):
  if(x=='0' or x=='6' or x=='8'):
    c=c+'|__|'
  elif(x=='1' or x=='4' or x=='7'):
    c=c+'   |'
  elif(x=='2'):
    c=c+'|__ '
  elif(x=='3' or x=='5' or x=='9'):
    c=c+' __|'
  return c
a=input('Input: ').split(':')
b=['','','','','','']
b[0]=a[0][0]
b[1]=a[0][1]
b[2]=a[1][0]
b[3]=a[1][1]
b[4]=a[2][0]
b[5]=a[2][1]

