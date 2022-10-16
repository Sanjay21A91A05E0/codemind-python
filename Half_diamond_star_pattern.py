n=int(input())
if(n<3 or n>100):
    print("The pattern is not possible")
    quit()
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print()
n-=1
for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print()