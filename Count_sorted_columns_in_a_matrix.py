a,b=map(int,input().split())
s=[list(map(int,input().split()))for i in range(a)]
c=0
for i in range(b):
    d=[]
    for j in range(a):
        d.append(s[j][i])
    if(d==sorted(d) or d[::-1]==sorted(d)):
        c+=1
print(c)