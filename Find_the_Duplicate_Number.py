n=int(input())
a=list(map(int,input().strip().split()))
for i in range(n):
    c=0
    for j in range(n):
        if(i!=j):
            if(a[i]==a[j]):
                c+=1
    if(c>0):
        print(a[i])
        a[i]=0