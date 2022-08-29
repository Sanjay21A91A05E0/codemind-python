n=int(input())
s=list(map(int,input().split()))
f,d=[],[]
for i in s:
    if(i%2!=0):
        f.append(i)
    else:
        d.append(i)
i,c=0,0
while(i<len(f) and i<len(d)):
    print(f[i],d[i],end=' ')
    i+=1
    c+=2
while(i<len(f)):
    print(f[i],end=' ')
    i+=1
    c+=1
while(i<len(d)):
    print(d[i],end=' ')
    i+=1
    c+=1
if(c%2):
    print("0")