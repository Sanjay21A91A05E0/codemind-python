a=input().lower().split()
b=input().lower().split()
c=0
for i in a:
    if i in b:
        if(a.count(i)==b.count(i)):
            c+=1
print(c)