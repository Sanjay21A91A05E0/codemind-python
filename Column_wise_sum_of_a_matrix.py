a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
for i in range(b):
    c=0
    for j in range(a):
        c+=s[j][i]
    print(c,end=' ')