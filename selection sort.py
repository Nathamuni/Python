
mylist=[1,2,4,3,5,9,3,1,0]
n=len(mylist)
print('bef sorting',mylist)
for i in range(0,n-1):
   for j in range (i+1,n):
       if mylist[i]>mylist[j]:
           mylist[i],mylist[j]=mylist[j],mylist[i]

print("elements sfter sorting\n",mylist)


