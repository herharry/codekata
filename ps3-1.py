a=input().split()
word1=a[0]
word2=a[1]
if(len(a[0]) < len(a[1])):
  word1=a[1]
  word2=a[0]
else:
  word1=a[0]
  word2=a[1]
temp=word1.find(word2)
if(temp!=-1):
  xc=len(word1)-len(word2)
  print(xc)
else:
  j=0
  xc=0
  for i in range(len(word2)):
      if(word1[j]!=word2[i]):
        xc=xc+1
      j=j+1
  xc=xc+len(word1)-len(word2)
  print(xc)
