def xor(a):
  x=a[0]
  for i in range(1,len(a)):
    x=x^a[i]
  return x
n=list(map(int,input().split()))
x=list(map(int,input().split()))
l=list()
sum1=list()
for i in range(n[1]):
  l=input().split()
  a=list()
  for j in range(int(l[0])-1,int(l[1])):
    a.append(x[j])
  sum1.append(xor(a))

for i in sum1:
  print(i)



