a=int(input())
for i in range(a):
    s=input()
    c=0
    for j in range(len(s)):
        if(s[j].isdigit()):
            c+=1
    if(c==len(s)):
        print(True)
    else:
        print(False)