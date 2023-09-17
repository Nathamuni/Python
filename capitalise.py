ch = input("Enter any charactor: ")
if ch >='A' and ch<="Z":
    ch =ch.lower()
    print("the charectors on lower case are " , ch )
elif ch >='a' and ch<="z":
    ch = ch.upper()
    print("the charectors on case are "+ch)

else:
    print('wrong input')