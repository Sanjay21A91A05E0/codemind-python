a=int(input())
s=list(map(int,input().strip().split()))
m,n=map(int,input().split())
k=[]
f=0
for i in range(a):
    if(s[i]>=m and s[i]<=n):
        f=1
        k.append(s[i])
print(min(k)) if f else print('-1')