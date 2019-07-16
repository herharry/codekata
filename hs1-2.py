a=list()
b=input()
b=int(b)
for i in range(b):
    l=input()
    a.append(int(l))
a.sort()
x=0
i=b-1
while(i>=0):
    x=x+pow(10,i)*a[i]
    i=i-1

print(x)
