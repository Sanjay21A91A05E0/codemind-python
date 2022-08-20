a=int(input())
s=list(map(int,input().split()))
d,l=[],[]
for i in range(0,len(s),2):
    d.append(s[i])
    l.append(s[i+1])
for i in range(len(d)):
    for j in range(l[i]):
        print(d[i],end=' ')