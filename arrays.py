from array import *

vals = array('i',[5,6,8,9,2])

newArray = array(vals.typecode, (a*a for a in vals))
print(newArray)

i = 0
while i<len(newArray):
    print(newArray[i])
    i+=1

