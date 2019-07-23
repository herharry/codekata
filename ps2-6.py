a=int(input())
x=list(map(int,input().split()))
x.sort(reverse=True)
l=set(x)
ab=1
sums=0
for j in l:
  for i in range(len(x)):
    if(j==x[i]):
      sums=sums+ab
  ab=ab+1
print(sums)
