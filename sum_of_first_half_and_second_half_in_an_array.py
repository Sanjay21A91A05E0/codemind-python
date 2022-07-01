a=int(input())
s=list(map(int,input().split()))
d=a//2
l=sum(s[:d])
r=sum(s[d:])
print(l)
print(r)