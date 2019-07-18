from itertools import combinations

def findtriplet(a):
  if(a[0]<a[1]<a[2]):
    return 1
  else:
    return 0

n=input()
n=int(n)
a=list(map(int,input().split()))
x=list(combinations(a,3))
x1=set(x)
acount=0
for i in x1:
  acount=acount+findtriplet(i)
print(acount)