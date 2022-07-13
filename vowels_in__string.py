a=input()
s=[]
for i in a:
    if i in 'aeiouAEIOU'and i not in s:
        s.append(i)
if(s==[]):
    print('-1')
else:
    print(*s)