def prime(a):
    if(a==1):
        return 0
    elif(a==2):
        return 1
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    else:
        return 1
a=int(input())
s=list(map(int,input().split()))
k=s.index(min(s))
d=s.index(max(s))
if(k>d):
    t=k
    k=d
    d=t
c=0
for i in range(k,d+1):
    if(prime(s[i])):
        c+=1
print(c)