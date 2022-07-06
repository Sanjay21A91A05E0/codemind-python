a=int(input())
s=list(map(int,input().split()))
m,n=map(int,input().split())
d=[]
for i in s:
    if i<m or i>n:
        d.append(i)
if(d==[]):
    print('-1')
else:
    print(*d)