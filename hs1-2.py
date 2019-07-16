a=list()
b=input()
a = list(map(int,input().split()))
a.sort()
x=0
i=len(a)-1
while(i>=0):
    x=x+pow(10,i)*a[i]
    i=i-1

print(x)
