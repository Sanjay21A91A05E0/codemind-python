m=input()
s=[]
j=[]
n=input()
for i in range(len(m)):
    if(m[i]=='#'):
        s.pop()
    else:
        s.append(m[i])
for i in range(len(n)):
    if(n[i]=='#'):
        j.pop()
    else:
        j.append(n[i])
print(s==j)