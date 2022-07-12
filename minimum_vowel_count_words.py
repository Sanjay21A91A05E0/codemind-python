a=input().lower().split()
s='aeiou'
d=[]
for i in a:
    c=0
    for j in i:
        if j in s:
            c+=1
    d.append(c)
l=min(d)
k=0
for i in d:
    if(i<=l):
        k+=1
print(k)