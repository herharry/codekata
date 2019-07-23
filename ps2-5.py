def binary(x):
  bform=list()
  while(x>0):
    bform.append(int(x%2))
    x=int(x/2)
  bform.reverse()
  return bform

a=int(input())
x=list()
b=list(map(int,input().split()))
b.sort(reverse=True)
for i in range(len(b)):
  x.append(binary(b[i]))
l=list()
for i in range(len(x)):
  l.append(x[i].count(1))
l.sort(reverse=True)
j=l[0]
while(True):
  for i in range(len(x)):
    if(x[i].count(1)==j):
      print(b[i])
  j=j-1
  if(j==0):
    break;
