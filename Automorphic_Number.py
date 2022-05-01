a=int(input())
t=a
c=1
sq=a*a
while(a!=0):
    c*=10
    a//=10
if(sq%c==t):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")