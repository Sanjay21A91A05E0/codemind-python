a=input()
s='aeiouAEIOU'
d=[]
f=0
for i in a:
    if i  in s:
        d.append(i)
print(len(d))