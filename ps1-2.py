def combine(a):
  val=0
  j=len(a)-1
  for i in range(len(a)):
    val=val+pow(10,j)*a[i]
    j=j-1
  return val


a=input()
b=input()
x=list(map(int,a))
y=int(b)
temp=list(x)
temp.sort()
j=0
l=list()
newa = list()

if(y==0):
  print(a)
else:    
  for i in range(len(x)):
    if(x[i]==temp[j]):
      if(i+len(x)-y<=len(x)):
        for k in range(i,len(x)-y+i):
          newa.append(x[k])
        break;
      else:
        j=j+1
        i=0;
    if(j>=len(x)):
      break
  
  print(combine(newa))



