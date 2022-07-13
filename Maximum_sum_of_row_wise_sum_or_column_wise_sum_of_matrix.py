a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
r,c=0,0
for i in s:
    if(r<sum(i)):
        r=sum(i)
print(r)