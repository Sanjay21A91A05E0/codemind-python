a=int(input())
d=list(map(int,input().split()))
s=0
c=0
k=list(set(d))
for i in k:
    if(d.count(i)>s):
        s=d.count(i)
        c=i
print(c)