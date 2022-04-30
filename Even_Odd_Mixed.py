a=int(input())
ec=0
oc=0
dc=0
while a>0:
    d=a%10
    if(d%2):
        oc+=1
    else:
        ec+=1
    a//=10
    dc+=1
if(dc==oc):
    print("Odd")
elif(dc==ec):
    print("Even")
else:
    print("Mixed")