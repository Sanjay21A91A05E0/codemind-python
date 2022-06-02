a=int(input())
s=[]
c=[]
l=list(map(int,input().split()))
for i in l:
    if(i==0):
        s.append(i)
    else:
        c.append(i)
v=s+c
print(*v)