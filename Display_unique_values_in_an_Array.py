n=int(input())
a=list(map(int,input().strip().split()))
f=0
for i in range(n):
    c=0
    for j in range(n):
        if(i!=j):
            if(a[i]==a[j]):
                c+=1
    if(c==0):
        f=1
        print(a[i],end=' ')
if(f==0):
    print('-1')
    
