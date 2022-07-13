a=list(input().split())
b = []
for i in range(len(a)):
    x = list(a[i])
    b.append(len(x))
print(min(b))