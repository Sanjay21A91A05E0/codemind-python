a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
c=0
for i in range(a):
    for j in range(b):
        if(i==j or i==a-j-1):
            c+=s[i][j]
print(c)