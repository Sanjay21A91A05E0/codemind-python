a=int(input())
s=list(map(int,input().split()))
d=[]
for i in range(1,len(s)-1):
    if((s[i-1]%2 and s[i+1]%2==0)or(s[i-1]%2==0 and s[i+1]%2)):
        d.append(s[i])
if(s[len(s)-2]%2 and s[0]%2==0) or s[len(s)-1]%2==0 and s[0]%2:
    d.append(s[len(s)-1])
if(s[1]%2 and s[len(s)-1]%2==0) or s[1]%2==0 and s[len(s)-1]%2:
    d.append(s[0])
print(len(d))