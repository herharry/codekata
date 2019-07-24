n=input().split()
k=int(n[1])
a=list(map(int,input().split()))
flag=1
for j in range(len(a)):
  summ=0
  if(flag==0):
    break
  for i in range(j,len(a)-1):
    summ=summ+a[i]+a[i+1]
    if(summ==k):
      print("yes")
      flag=0
      break
if(flag):
  print("no")
