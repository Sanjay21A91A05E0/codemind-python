a=input()
b=input()
k=[]
for i in range(len(a)):
    k.append(a[i])
for i in range(len(b)):
    k.append(b[i])
k.sort()
for i in range(len(k)):
    print(k[i],end='')