a=int(input())
s=list(map(int,input().split()))
d=sum(s)//a
c=[]
for i in s:
    if(i<=d):
        c.append(i)
print(len(c))