n=int(input())
for i in range((2**n)):
    s=bin(i)
    s=s[2:]
    while(len(s)<n):
        s='0'+s
    print(s)