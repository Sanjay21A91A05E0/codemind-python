a=int(input())
while(a):
    m=int(input())
    s=list(map(int,input().split()))
    if(m%2):
        for i in range(m//2):
            print(s[m-1-i],s[i],end=' ')
        print(s[m//2],end='
')
    else:
        for i in range((m//2)-1):
            print(s[m-1-i],s[i],end=' ')
        print(s[m//2],end=' ')
        print(s[(m//2)-1],end='
')
    a-=1