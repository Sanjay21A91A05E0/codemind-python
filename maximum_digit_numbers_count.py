a=int(input())
s=list(map(int,input().split()))
g=[]
c=0
for i in s:
    i=list(str(i))
    d=len(i)
    g.append(d)
f=max(g)
for i in s:
    i=list(str(i))
    if(len(i)==f):
        i=''.join(i)
        print(i,end=' ')