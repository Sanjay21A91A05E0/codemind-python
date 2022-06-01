import itertools
a=input()
s=itertools.permutations(a)
for i in s:
    for j in i:
        print(j,end='')
    print()