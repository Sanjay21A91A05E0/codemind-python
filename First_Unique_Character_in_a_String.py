a=input()
for i in range(len(a)):
    c=0
    f=0
    for j in range(len(a)):
        if(i!=j):
            if(a[i]==a[j]):
                c+=1
    if(c==0):
        f=1
        print(i)
        break
if(f==0):
    print('-1')