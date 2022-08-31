def prime(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
a=int(input())
s=list(map(int,input().split()))
k=s.index(min(s))
f=s.index(max(s))
c=0
if(k>f):
    t=k
    k=f
    f=t
for i in range(k,f+1):
    if prime(s[i]):
        c+=1
print(c)