import sys
print("Command-line arguments")
print("number of arguments: ",len(sys.argv),"arguments")
i =1
print("Argument list:")
for arg in sys.argv:
    print(i,")",arg)
    i=i+1

