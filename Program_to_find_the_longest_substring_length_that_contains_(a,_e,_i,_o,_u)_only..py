a=input()
c=0
f=0
s=[]
for i in a:
    if(i in 'aeiou'):
        c+=1
    else:
        if(c>f):
            f=c
            c=0
print(f)