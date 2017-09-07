
## Odd Numbers

for x in range(0,1001):
    if x%2 != 0:
        print x;

## Multiples of 5's

for x in range(5,1000000):
    if x%5 == 0:
        print x;      


##Sum Array 

a=[1,2,5,10,55,3]

def sumArray():
    sum = 0;
    i=0;
    x = len(a)-1;
    while (i <=x):
        sum = sum + a[i];
        i=i+1;
    print sum;

sumArray()


##Average List

def avgArray():
    sum = 0;
    i=0;
    x = len(a)-1;
    while (i <=x):
        sum = sum + a[i];
        i=i+1;
    avg = sum/len(a);
    print avg;
    
avgArray()
