a=int(input())
b=int(input())
sa=0
sb=0
for i in range(1,a):
    if(a%i==0):
        sa+=i
for j in range(1,b):
    if(b%j==0):
        sb+=j
print('Amicable')if a==sb  and b==sa else print('Not Amicable')