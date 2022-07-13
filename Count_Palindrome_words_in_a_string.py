a=input().lower().split()
c=0
for i in a:
    i=list(i)
    if i==i[::-1]:
        c+=1
print(c)