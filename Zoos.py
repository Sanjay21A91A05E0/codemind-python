a=input()
zc=0
oc=0
for i in range(len(a)):
    if(a[i]=='z'):
        zc+=1
    elif(a[i]=='o'):
        oc+=1
if(oc==2*zc):
    print('Yes')
else:
    print('No')