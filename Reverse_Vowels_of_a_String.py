s=input()
k='aeiouAEIOU'
d=[]
for i in s:
    if i in k:
        d.append(i)
d=d[::-1]
j=0
for i in s:
    if i in k:
        print(d[j],end='')
        j+=1
    else:
        print(i,end='')