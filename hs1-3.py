a=list()
b=input()
a = list(map(int,input().split()))
c=list()
flag=0
for i in range(len(a)):
    if(a[i]==i):
        c.append(i)
        flag=1
if(flag):
    c.sort()
    print(c)
else:
    print(-1)
