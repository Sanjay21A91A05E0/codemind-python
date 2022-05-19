a=int(input())
s=list(map(int,input().strip().split()))
a=[i*i for i in s]
print(*sorted(a))