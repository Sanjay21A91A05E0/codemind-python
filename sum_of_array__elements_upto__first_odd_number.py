a=int(input())
s=list(map(int,input().split()))
d=0
for i in s:
    if(i%2):
        break
    d+=i
print(d)