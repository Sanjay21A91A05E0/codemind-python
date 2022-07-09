a=list(input())
f=[]
for i in a:
    if i in 'aeiouAEIOU':
        if i not in f:
            f.append(i)
if(f==[]):
    print('-1')
else:
    print(*f)