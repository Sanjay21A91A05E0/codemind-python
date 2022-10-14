n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if i%2:
        c+=1
if(c>2):
    print("NO")
else:
    print("YES")