from itertools import combinations

def combine(a):
  val=0
  j=len(a)-1
  for i in range(len(a)):
    val=val+pow(10,j)*a[i]
    j=j-1
  return val

a=input().split()
x=list(map(int,a[0]))
y=int(a[1])
if(len(x)<y):
  print("error")
else:
  final=list()
  reml=len(x)-y
  newl = list(combinations(x,reml))
  for i in newl:
    final.append(combine(i))
  final.sort()
  print(final[0])


