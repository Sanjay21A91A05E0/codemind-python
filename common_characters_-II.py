a=list(input().lower().replace(' ',''))
b=list(input().lower().replace(' ',''))
d=[]
for i in a:
    if i in b and i not in d:
        d.append(i)
print(len(d))