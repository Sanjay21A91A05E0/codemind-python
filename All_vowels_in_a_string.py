a=input()
s='aeiou'
d=[]
f=0
for i in a:
    if i  in s and i not in d:
        d.append(i)
d.sort()
d=''.join(d)
print(d==s)