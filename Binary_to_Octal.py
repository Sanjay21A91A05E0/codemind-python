for i in range(int(input())):
    n=input()
    k=int(n,2)
    s=''
    while(k):
        s+=str(k%8)
        k//=8
    print(s[::-1])