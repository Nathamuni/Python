n = int(input("Enter a Number : "))
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
result = fact(n)
print(result)
