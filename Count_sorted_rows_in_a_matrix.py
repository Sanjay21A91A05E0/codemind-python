a,b=map(int,input().split())
s=[list(map(int,input().split())) for i in range(a)]
c=0
for i in s:
    if(i==sorted(i) or i[::-1]==sorted(i)):
        c+=1
print(c)