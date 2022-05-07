a=int(input())
i=0
s=0
while(s<=a):
    s=2**i
    i+=1
k=s//2
x=abs(a-s)
y=abs(a-k)
print(x) if (x<y) else print(y)