reverse = 0

def palindrome(num):

    global reverse

    if(num > 0):

        reminder = num % 10
        reverse = (reverse * 10) + reminder
        palindrome(num // 10)
    return reverse

num = int(input("Enter a n.o : "))

rev = palindrome(num)
print("the reverse of the given n.0 is %d " % rev)

if num == rev:
    print("It is a palindrome n.o " , num)

else:
    print("It is not a PALINDROME " , num)
