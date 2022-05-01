a=int(input())
for i in range(a,0,-1):
    for j in range(i,0,-1):
         k=64+i
         print("%c"%k,end=" ")
    print()
    