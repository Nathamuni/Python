mylist =[1,2,3,4,5,7,89]
n = len(mylist)
key = int(input('Enter the value to search : '))
low =0
high=n-1
while(low<high):
    i=1
    mid = (low + high) // 2
    if (key == mylist[mid]):
        print("Key is found")
        break
    elif(key < mylist[mid]):
        high = mid - 1
    else:
        low = mid + 1
else:
    print('key not found')
