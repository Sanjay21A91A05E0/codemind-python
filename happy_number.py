a=int(input())
def happy(a):
    s=0
    while(a):
        d=a%10
        s+=d*d
        a//=10
    if(s==1):
        return 1
    elif(s==4):
        return 0
    else:
        return happy(s)
if(happy(a)):
    print('True')
else:
    print("False")