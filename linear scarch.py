print("linear scarch")
mylist = [1,2,3,4,5,6,3,6,0]
n = len(mylist)
key = int(input("Enter the value to search\n"))
i=0
while (i<n):
    if (key==mylist[i]):
        print("The element is found at",i)
        break
    i+=1
else:
    print("Element not found")