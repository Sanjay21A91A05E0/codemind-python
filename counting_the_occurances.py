a=input()
s=input()
d=0
c=0
for i in range(len(a)):
    if(a[i]==s):
        d=i
        c+=1
if(d==0):
    print('-1')
else:
    print(c)