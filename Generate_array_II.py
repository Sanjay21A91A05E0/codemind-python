n=int(input())
s=list(map(int,input().split()))
f,d=[],[]
for i in range(n):
    if(i%2==0):
        f.append(s[i])
    else:
        d.append(s[i])
for i in range(len(f)):
    for j in range(d[i]):
        print(f[i],end=' ')