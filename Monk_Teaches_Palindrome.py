a=int(input())
for i in range(a):
    s=input()
    k=s[::-1]
    if(s!=k):
         print('NO')
    elif(s==k and len(s)%2):
        print('YES ODD')
    elif(s==k and len(s)%2==0):
        print('YES EVEN')