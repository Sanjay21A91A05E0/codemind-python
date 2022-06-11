a=list(map(str,input().split()))
s=0
p=0
for i in a:
    s+=ord(max(i))
    p+=ord(min(i))
print(s-p)