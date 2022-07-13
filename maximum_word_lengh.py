a=input().split()
d=[]
for i in a:
    i=list(i)
    d.append(len(i))
print(max(d))