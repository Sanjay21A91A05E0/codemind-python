a=input()
s=0
for i in range(len(a)):
    if(a[i].isdigit()):
        s+=int(a[i])
print(s)