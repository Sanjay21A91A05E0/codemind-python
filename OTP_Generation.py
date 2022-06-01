a=input()
a=list(str(a))
s=[]
for i in a:
    if(int(i)%2):
        s.append(int(i)**2)
for i in s:
    print(i,end='')