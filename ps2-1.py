from itertools import combinations
a=int(input())
x=list()
for i in range(a):
  x.append(i)

print(len(list(combinations(x,2))))