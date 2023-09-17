# break statement is used to get out of the condition after performing the process

try:
    av = 5
    x = int(input("How many candies you want? "))
    i = 1
    while i <= x:
        if i <= av:
            print("candy")
            i += 1
        else:
            print("Sorry bro we are out of stock")
            break

except:
    print ("Something went wrong...")
    print ("TRY WITH PROPER INPUT")







