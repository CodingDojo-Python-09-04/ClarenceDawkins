num = [2,3,1,7,4,12]
stringList = ['magical','unicorns']
list_mixed = ['magical unicorns',19,'hello',98.98,'world']


def listType(list1):
   
    string = '';
    sum = 0;

    for value in list1:
        if instance(value,int) or instance(value,float):
            total = total + value
        elif instance(value, str):
            string = string + value

    if string and sum:
        print 'The list you entered is of mixed type'
        print 'String: ', string
        print 'Total ', sum

    elif string:
        print 'The list you enterd is of inteer type '
        print 'Total: ',sum

    else:
        print 'The list you entered is of string type '
        print 'String: ', string

print listType(num)
print listType(stringList)
print listType(list_mixed)
