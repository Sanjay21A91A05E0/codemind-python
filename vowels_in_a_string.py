a=input()
v=input()
s='aeiou'
d=[]
f=0
for i in range(len(a)):
    if(a[i]==v):
        print(True)
        print(i)
        quit()
print(False)