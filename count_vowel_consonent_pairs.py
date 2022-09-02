s=input().lower()
g='aeiou'
c=0
k=len(s)
for i in range(k//2):
    if(s[i]!=' ' and s[k-i-1]!=' '):
        if(s[i] in g and s[k-i-1] not in g) or(s[i]not in g and s[k-i-1] in g):
            c+=1
print(c)