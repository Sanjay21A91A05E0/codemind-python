import math
def fun(a):
    s=int(math.sqrt(a))
    if(a==s*s):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().strip().split()))
s=0
for i in range(n):
    if(fun(a[i])):
        s+=a[i]
print(s)
        