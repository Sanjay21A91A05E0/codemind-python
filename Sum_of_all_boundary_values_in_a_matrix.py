a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
c=0
for i in range(a):
    for j in range(b):
        if(i==0 or j==0 or i==a-1 or j==b-1):
            c+=s[i][j]
print(c)