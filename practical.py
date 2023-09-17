import operator
filename = input("Enter the file name : ")
fin = open(filename,'r')
mydict= {}
print("content in the file : ")
for i in fin.read().split():
    if i in mydict.keys():
        mydict[i]=mydict[i]+1
    else:
        mydict[i]=1

sorted_mydict=sorted(mydict.items(),key=operator.itemgetter(1),trverse=True)
for i in sorted_mydict:
 print(i[0] , " => " , i[1])
print(sorted_mydict[0][0], " has appeared for ",
sorted_mydict[0][1], " no. of times" )
