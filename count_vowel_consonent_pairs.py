a=input()
s='aeiou'
c=0
n=0
d=len(a)-1
for n in range(len(a)//2):
    if(a[n] in s and a[d]not in s and a[n]!=' ' and a[d]!=' '):
        #print(a[n],a[d])
        c+=1
    elif(a[n] not in s and a[d] in s and a[n]!=' ' and a[d]!=' '):
        #print(a[n],a[d])
        c+=1
    d-=1
print(c)