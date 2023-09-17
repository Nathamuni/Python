def check_prime(n):
     flag = 0
     for j in range(2,n):
         if (n%j==0):
             flag = 1
     return flag
print("Print first 'N' Prime Numbers")
n = int(input("Enter N Value : "))
i = 0
j = 1
while (i<n):
     flag = check_prime(j)
     if (flag==0):
         print(j)
         i = i + 1
     j = j + 1
