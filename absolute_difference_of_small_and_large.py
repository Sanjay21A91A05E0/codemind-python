a=list(map(str,input().split()))
for i in a:
    s=0
    p=0
    s+=ord(max(i))
    p+=ord(min(i))
    print(s-p,end=' ')