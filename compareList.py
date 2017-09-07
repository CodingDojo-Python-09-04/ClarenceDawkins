
def compare():
    length1 = len(L1)
    length2 = len(L2)

    if length1 == length2:
        for i in range(0,length1):
            if L1[i]==L2[i]:            
                i=i+1;
                if i == length1:
                    print "The list are the same. ";            
            else:
                print "The list are not the same. "
                break;

    else:
        print "The list are not the same. "


L1 = [1,2,5,6,2]
L2 = [1,2,5,6,2]

compare()

L1 = [1,2,5,6,2]
L2 = [1,2,5,6,2,3]

compare()

L1 = [1,2,5,6,5,16]
L2 = [1,2,5,6,5]

compare()

L1 = ['celery','carrots','bread','milk']
L2 = ['celery','carrots','bread','milk']

compare()
    
   

