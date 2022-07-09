a=int(input())
s=list(map(int,input().split()))
d=[]
c=[]
for i in s:
    if(i%2==0):
        d.append(i)
    else:
        c.append(i)

print(*(d+c))