mylist=[22,3,14,5]
n = len(mylist)
print('before sorting\n',mylist)
for i in range(1,n):
    val = mylist[i]
    h = i
    while (h>0) and (mylist[h-1]>val):
        mylist[h]=mylist[h-1]
        h=h-1

    if (h != i):
        mylist[h]=val
print("After sorting\n",mylist)