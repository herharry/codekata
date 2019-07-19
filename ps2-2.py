n=list(map(int,input().split()))
x=list(map(int,input().split()))
l=list()
sum1=list()
for i in range(n[1]):
  l=input().split()
  a=list()
  for j in range(int(l[0])-1,int(l[1])):
    a.append(x[j])
  sum1.append(sum(a))

for i in sum1:
  print(i)