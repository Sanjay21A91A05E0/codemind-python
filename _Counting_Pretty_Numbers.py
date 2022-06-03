def pretty(i):
    if(i%10==2 or i%10==3 or i%10==9):
        return 1
    else:
        return 0
a=int(input())
while(a):
    c=0
    m,n=map(int,input().split())
    for i in range(m,n+1):
        if(pretty(i)):
            c+=1
    print(c)
    a-=1