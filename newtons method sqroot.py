a = int(input('enter value a: '))
b = int(input('enter value b : '))
if a>b:
    a,b=b,a
remainder = a%b
while remainder !=0:
    a=b
    b=remainder
    remainder = a%b

print("the GDP ",b)