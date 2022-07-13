a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
c=0
for i in s:
    print(sum(i),end=' ')