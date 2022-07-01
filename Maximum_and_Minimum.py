a=int(input())
s=list(map(int,input().split()))
d=list(set(s))
k=[]
for i in d:
    if(i==s.count(i)):
        k.append(i)
if(k==[]):
    print('-1')
else:
    print(min(k),max(k))