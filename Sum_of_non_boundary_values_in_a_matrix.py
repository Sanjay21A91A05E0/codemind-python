a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
c=0
for i in range(a):
    for j in range(b):
        if(i!=0 and j!=0 and i!=a-1 and j!=b-1):
            c+=s[i][j]
print(c)