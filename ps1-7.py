import math
n=input()
n=int(n)
a=math.sqrt(n)
b=int(a)
if(a==b):
  print(0)
else:
  x=b+1
  count=pow(2,x)-n
  count1=pow(2,b)-n
  if(count<count1):
    print(abs(count))
  else:
    print(abs(count1))
