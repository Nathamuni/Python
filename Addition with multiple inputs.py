# * here means get multiple values [as tuple]
#we have to fetch one one values from the tuple and add

try:
    def sum(*a):
        b = 0
        for i in a:
            b += i
        print(b)


    sum(1, 2, 3, 4, 5, 121,)

except:
    print('invalid input')