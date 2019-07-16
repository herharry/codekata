a=list()
b=input()

a=list(map(int,input().split()))
c=set(a)
for i in c:
    if(a.count(i)<2):
        print(i)
