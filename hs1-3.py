a=list()
b=input()
a = list(map(int,input().split()))
c=list()
flag=1
for i in range(len(a)):
    if(a[i]==i):
        print(i)
        flag=0
if(flag):
    print(-1)
