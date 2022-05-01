a=int(input())
for i in range (1,a+1):
    for j in range(1,a+1):
        j=64+i
        print("%c"%j,end=' ')
    print()