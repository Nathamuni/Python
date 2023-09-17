n = int(input("Enter a n.o: "))
temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
if temp==rev:
    print("Your entered n.o is a palindrome! ",temp )
else:
    print("The n.o is not a palindrome")

print("bye")