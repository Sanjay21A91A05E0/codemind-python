a=input()
s='#%$@!*&)(+_-.,<>?*/|\`~'
c=0
e=[]
o=[]
for i in a:
    if i in s:
        c+=1
    if(i.isdigit() and int(i)%2==0):
        e.append(int(i))
    elif(i.isdigit() and int(i)%2):
        o.append(int(i))
if(c%2==0):
    s1=e
    s2=o
else:
    s1=o
    s2=e
i=0
while(i<len(s1) and i<len(s2)):
    print(s1[i],end='')
    print(s2[i],end='')
    i+=1
while(i<len(s1)):
    print(s1[i],end='')
    i+=1
while(i<len(s2)):
    print(s2[i],end='')
    i+=1