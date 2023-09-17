n = int(input("Enter the n.o of stars to print : "))
for i in range(n,0,-1):
    print(i*'*')
    i = i-1

for i in range(n+1):
    print(i*'*')
    i = i-1
