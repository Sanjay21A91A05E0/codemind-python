a,b=map(int,input().split())
s=[list(map(int,input().split()))for i in range(a)]
d=[]
for j in range(b):
    c=0
    for i in range(a):
        c+=s[i][j]
    d.append(c)
print(max(d))
    