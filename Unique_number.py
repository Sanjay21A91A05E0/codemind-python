a=int(input())
s=[]
c=0
while(a):
    d=a%10
    s.append(d)
    a//=10
for i in s:
    if(s.count(i)>1):
        print('Not Unique Number')
        break
    else:
        c+=1
if(c==len(s)):
    print('Unique Number')