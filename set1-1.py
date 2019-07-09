a=input() 
arr=list()
a=int(a)
for i in range(a):
  n=int(input())
  arr.append(n)
doop =list()

for i in range(a):
  count=0
  for j in range(a):
    if(arr[i]==arr[j]):
      count=count+1
  if(count>1):
    if(arr[i] not in doop):
      doop.append(arr[i])

if(len(doop)==0):
  print("unique")
else:
  doop.sort()
  print(doop)