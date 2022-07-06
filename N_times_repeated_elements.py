a=int(input())
s=list(map(int,input().split()))
m=int(input())
k=set(s)
d=[]
for i in k:
    if s.count(i)==m:
        d.append(i)
if(d==[]):
    print('-1')
else:
    print(*d)