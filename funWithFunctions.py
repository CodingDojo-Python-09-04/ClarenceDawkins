#Fun with Functions
import math

def oddEven():
    for x in range(1,2001):
        if x%2==0:
            print 'Number is ' + str(x) +'.  This is an even number. '
        else:
            print 'Number is ' + str(x) +'.  This is an odd number. '

#oddEven()

arr = [2,4,10,16]

def multiply(arr,num):
    
    for x in range(0,len(a)):
        num = (arr[x]*num);
        return num

multiply(arr,5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
        
    
