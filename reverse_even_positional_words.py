a=input().split()
for i in range(len(a)):
    if(i%2==0):
        k=a[i]
        print(k[::-1],end=' ')
    else:
        print(a[i],end=' ')