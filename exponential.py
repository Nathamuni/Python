b = int(input("Enter base value : "))
e = int(input("exponential value : "))
res = b
while e>1:
    res = res*b
    e-=1
print("result =",res)