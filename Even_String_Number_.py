a=input()
s=[]
for i in a:
    if i.isdigit():
        if i not in s:
            s.append(i)
s.sort()
s=s[::-1]
l=3289440394
f=0
for i in range(len(s)):
    s[i]=int(s[i])
    if(s[i]%2==0 and s[i]<l):
        l=s[i]
        h=i
        f=1
if(f==0):
    print("-1")
else:
    t=s[-1]
    s[-1]=s[h]
    s[h]=t
    for i in s:
        print(i,end='')
    