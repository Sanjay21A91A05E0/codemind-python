a=input()
c=0
f=0
for i in range(len(a)):
    if(a[i].isdigit()):
        c+=1
        f=1
print('Contains %d digit'%c) if f else print("Doesn't contain digit")