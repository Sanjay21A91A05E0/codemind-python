a=input().split(",")
res=''
for i in a:
    i=i.split(':')
    k=i[1]
    h=i[0]
    s=list(k)
    s.sort()
    f=0
    for j in range(1,len(s)):
        if(int(s[-j])<=len(h)):
            n=int(s[-j])
            f=1
            break
    if(f==0):
        res+='X'
    else:
        res+=h[n-1]
print(res)
            