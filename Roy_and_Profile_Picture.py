a=int(input())
s=int(input())
while(s):
    x,y=map(int,input().split())
    if(x<a or y<a):
        print("UPLOAD ANOTHER")
    else:
        if(x==y):
            print('ACCEPTED')
        else:
            print("CROP IT")
    s-=1