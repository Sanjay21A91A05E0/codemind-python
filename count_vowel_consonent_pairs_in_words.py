s=input().lower().split()
g='aeiou'
c=0
for i in s:
    k=len(i)
    for j in range(k//2):
        if (i[j] in g and i[k-j-1] not in g) or(i[j]not in g and i[k-j-1] in g):
            c+=1
print(c)