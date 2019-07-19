a=int(input())
sum=0
b=input().split()
for i in range(len(b)):
  x=int(b[i])
  for j in range(i):
      if(int(b[j])<x):
        sum=sum+int(b[j])

print(sum)