a=int(input())
s=list(map(int,input().split()))
d=[]
for i in s:
    if i not in d:
        d.append(i)
k=[]
for i in d:
    if(i==s.count(i)):
        k.append(i)
if(k==[]):
    print('-1')
else:
    print(*k)