a=int(input())
s=0
while(a):
    d=a%10
    s=s*10+d
    a//=10
print(s)