s=input().split()
k=s[0]
r=[]
f=0
for i in k:
    l=0
    for j in s:
        if i in j:
            l+=1
    if(l==len(s)and i.islower()):
        f=1
        r.append(i)
if(f==0):
    print("-1")
else:
    print(min(r))