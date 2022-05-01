a,b=map(int,input().split())
if(a>b):
    lcm=a
else:
    lcm=b
i=1
while(1):
    if(i%a==0 and i%b==0):
        print(i)
        break
    else:
        i+=1