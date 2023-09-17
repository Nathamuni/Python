n=int(input())
flag = 0
i=2
while n>i:
    if n%i==0:
        flag =1
        break
    i+=1
if flag ==0:
    print(n," is prime")
else:
    print(n," is not prime")