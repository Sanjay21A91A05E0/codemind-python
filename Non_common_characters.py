a=list(input().lower().replace(' ',''))
b=list(input().lower().replace(' ',''))
d=[]
# a=set(a)
# b=set(b)
for i in a:
    if i not in b and i not in d:
        d.append(i)
for i in b:
    if i not in a and i not in d:
        d.append(i)
print(len(d))
