a=input().lower().split()
s='aeiou'
d=[]
for i in a:
    c=0
    for j in i:
        if j in s:
            c+=1
    d.append(c)
print(*d)