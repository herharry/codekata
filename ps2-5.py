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
for i in range(len(b)):
  x.append(binary(b[i]))
print(x)
