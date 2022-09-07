a=input()
k=[]
for i in a:
    if i.isalpha():
        k.append(i)
k=k[::-1]
l=0
for i in a:
    if i.isalpha():
        print(k[l],end='')
        l+=1
    else:
        print(i,end='')