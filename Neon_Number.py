n=int(input())
s=0
p=n*n
while(p):
    d=p%10
    s+=d
    p//=10
if(n==s):
    print("Neon Number")
else:
    print("Not Neon Number")