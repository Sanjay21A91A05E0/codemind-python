a=input().split()
for i in a:
    k=max(i)
    n=min(i)
    print(abs(ord(k)-ord(n)),end=' ')